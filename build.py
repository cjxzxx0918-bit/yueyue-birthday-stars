"""Build a standalone offline HTML from the editable source and local assets."""
import base64
import io
import json
from pathlib import Path
from PIL import Image

ROOT=Path(__file__).resolve().parent
ASSETS=ROOT/'assets'/'paper'
template=(ROOT/'src'/'index.template.html').read_text(encoding='utf-8')

def uri(path,mime):
    return 'data:'+mime+';base64,'+base64.b64encode(path.read_bytes()).decode()

# Re-encoding reduces delivery size while retaining the originals for editing.
paper=Image.open(ASSETS/'paper-texture.png').convert('RGB')
buffer=io.BytesIO();paper.save(buffer,format='JPEG',quality=90,optimize=True)
paper_data='data:image/jpeg;base64,'+base64.b64encode(buffer.getvalue()).decode()
signature=Image.open(ASSETS/'yueyue-signature.png').convert('RGBA')
bbox=signature.getchannel('A').getbbox()
left,top,right,bottom=bbox
replacements={'__PAPER_DATA__':paper_data,'__SIGNATURE_DATA__':uri(ASSETS/'yueyue-signature.png','image/png'),
              '__SIGNATURE_BBOX__':json.dumps([left,top,right-left,bottom-top]),
              '__FONT_DATA__':uri(ASSETS/'noto-serif-sc-subset.woff2','font/woff2'),
              '__MUSIC_ICON__':uri(ASSETS/'music.svg','image/svg+xml'),
              '__MUTED_ICON__':uri(ASSETS/'muted.svg','image/svg+xml'),
              '__PAUSE_ICON__':uri(ASSETS/'pause.svg','image/svg+xml'),
              '__PLAY_ICON__':uri(ASSETS/'play.svg','image/svg+xml')}
for marker,value in replacements.items():template=template.replace(marker,value)
if '__' in template:
    raise RuntimeError('Unresolved asset marker')
(ROOT/'index.html').write_text(template,encoding='utf-8')
print(json.dumps({'built':'index.html','bytes':len(template.encode()),'signature_bbox':bbox,'paper_jpeg_bytes':len(buffer.getvalue())}))
