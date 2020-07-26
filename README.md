# py-rgb-cloud-music
> 修改网易云音乐主题色，匹配当前壁纸



## 调用参数
* mode [R] [G] [B]
* mode - 模式[0\color] [1\random] [2\desk] 默认值为2
* &emsp;&emsp;&emsp;&emsp;0\color - specifiedColor需要指定RGB值
* &emsp;&emsp;&emsp;&emsp;1\random - randomColor随机颜色
* &emsp;&emsp;&emsp;&emsp;2\desk - deskWallpaperColor桌面壁纸主色调
* R - 红色代码[0-255], mode值为0时传递, 无则自动生成随机值
* G - 绿色代码[0-255], mode值为0时传递, 无则自动生成随机值
* B - 蓝色代码[0-255], mode值为0时传递, 无则自动生成随机值


## 注意
* 使用到第三方模块[pyrgb](https://github.com/Moduland/pyrgb), 需要先[pip install pyrgb]
* 为方便执行，使用[rgbCloudMusic.bat]
* 执行后，会自动关闭网易云音乐，设置成功后，自动重新打开




## 更新


## 演示
<div align=center><img src="https://github.com/bjc5233/py-rgb-cloud-music/raw/master/resources/demo.gif"/></div>


<div align=center><img src="https://github.com/bjc5233/py-rgb-cloud-music/raw/master/resources/demo.png"/></div>


<div align=center><img src="https://github.com/bjc5233/py-rgb-cloud-music/raw/master/resources/demo2.png"/></div>