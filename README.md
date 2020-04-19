# QRCode
二维码生成器

PyQt5做界面

```
pip install pyqt5

```

[Pycharm配置PyQt5(QtDesigner)](https://blog.csdn.net/qq_43613793/article/details/104261911)

用到的二维码生成库有`qrcode`、`myqr`

```
# pip install qrcode
import qrcode
# pip install myqr
from MyQR import myqr
```

三种二维码样式，其中样式1和样式二用到的是qrcode库，样式三用到的是myqr库

其中qrcode可以生成普通二维码以及中间带有图标的二维码，二维码内容支持中英文；myqr可以生成以某张.png图片或.gif动态图为背景的二维码，但是二维码内容不支持中文，只支持英文以及一系列字符

另外为了方便与二维码的生成与界面进行交互，我设置了一个能跨多个文件(整个文件夹)的全局变量保存文件globalvar.py

还有为了防止图片路径更改后导致程序找不到，我们需要设置一个.qrc文件来保存所需图片，然后利用下面这行命令将这些图片都转为.py文件在程序中引用。它的本质就是将图片转化为base64格式进行保存，需要用的时候在引入读取。这样即使原图路径改变或将其打包为.exe文件在别的电脑上运行都不会丢失图片。（我这里引入的图片是文章开头程序运行截图里的样式1、样式2、样式3以及程序窗口左上角的图标还有生成的.exe文件图标）

```
pyrcc5 picture.qrc -o picture_re.py
```

由于样式三的图片用的myqr库不支持二维码内容为英文，所以我设置了一个翻译功能，检测到输入的内容为中文时将其自动转化成英文,这里采取的是爬取有道翻译的方式进行转化`translate.py`

## 效果图：

![](https://img-blog.csdnimg.cn/20200210170934560.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjEzNzkz,size_16,color_FFFFFF,t_70)

![](https://img-blog.csdnimg.cn/20200210171141910.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjEzNzkz,size_16,color_FFFFFF,t_70)

![](https://img-blog.csdnimg.cn/20200210171255775.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjEzNzkz,size_16,color_FFFFFF,t_70)

[视频演示地址](https://www.bilibili.com/video/BV15741157qW)

-----------------------------------------------------------------------------
题外闲话：...

尝试了无数次用pyinstaller打包，各种版本打包，在自己电脑上能运行，但是到了别的电脑上就不能运行了（不过那台电脑上面没有python环境）
不知道大火能不能

最终版本：
Anaconda3-4.8.1
python-3.7.4
pyqt5-5.13.0 
