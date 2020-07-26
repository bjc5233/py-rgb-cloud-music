@echo off& call loadF.bat _params& title 网易云音乐动态主题
:::说明
:::  修改网易云音乐主题色，匹配当前壁纸
:::参数
:::  [-h help]
:::      help - 打印注释信息
call %_params% %*
if defined _param-h (python rgbCloudMusic.py --help& goto :EOF)
if defined _param-help (python rgbCloudMusic.py --help& goto :EOF)
python rgbCloudMusic.py %*