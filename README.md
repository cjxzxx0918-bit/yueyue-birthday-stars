# Yueyue Birthday Stars

送给悦悦的一份生日祝福：星光在暗色烛光中聚成三层奶油蛋糕，许愿后，金粉缓缓落成米白纸笺上的手写名字。

**在线观看：[yueyue-birthday-stars.pages.dev](https://yueyue-birthday-stars.pages.dev/)**

链接不含账号名，无需登录。复制到微信，对方打开后点击「展开这份祝福」即可观看。

![新版粒子蛋糕与手写纸笺的实际浏览器画面](assets/preview.jpg)

## 体验

约 34 秒：纸笺开场、蛋糕逐层成形、烛光许愿、星光散开、金粉汇成「悦悦」，最后留下「生日快乐」与「愿新的一岁，自在、明亮。」。

三层蛋糕具有奶油顶面、波浪边饰、裱花和香槟金侧面，以 WebGL 绘制高密度粒子；不支持 WebGL 时回退到 Canvas。结尾采用真实纸纹与透明手写字迹资产。

经典《生日快乐》采用轻柔音乐盒编曲，由 Web Audio 合成，包含两遍旋律、分解和弦与混响。点击开始后播放声音。支持静音、暂停、继续和重播；切换到其他标签页时同时暂停动画与音乐。

## 使用

直接下载 index.html，用 Chrome、Edge 或 Safari 打开即可，离线可用。图片、字体、图标和音乐均内置，无需安装依赖或构建。手机分享请发送已托管网页的 HTTPS 链接。

## 编辑与重新构建

编辑 src/index.template.html；原始纸纹、字迹、字体和图标位于 assets/paper/。

```sh
python -m pip install -r requirements.txt
python build.py
```

构建结果是独立的 index.html。修改祝福文字时，请同步检查页面标题、开场、无障碍说明和字体字形覆盖。替换名字还需要替换 assets/paper/yueyue-signature.png，并调整配置中的名字；仅修改文字不会改变手写图片。构建器会自动计算透明字迹边界。

## 验证

已在 Chrome 浏览器中检查手机竖屏、电脑和横屏画面，以及开始播放、音频状态、暂停同步、继续、静音、重播和单文件离线播放。没有捕获到页面运行错误。微信内置浏览器尚未在实体手机上验证。

线上网页通过 Cloudflare Pages 发布。此仓库没有自动部署工作流，后续源文件修改需构建并重新发布。

## 许可

代码、生成的纸纹/手写字迹与预览图采用 MIT License。Noto Serif SC 字体采用 SIL Open Font License 1.1，Phosphor Icons 图标采用 MIT；第三方许可文件保存在 assets/paper/。音乐由程序合成，仓库不包含参考视频或第三方录音。
