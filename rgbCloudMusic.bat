@echo off& call loadF.bat _params& title ���������ֶ�̬����
:::˵��
:::  �޸���������������ɫ��ƥ�䵱ǰ��ֽ
:::����
:::  [-h help]
:::      help - ��ӡע����Ϣ
call %_params% %*
if defined _param-h (python rgbCloudMusic.py --help& goto :EOF)
if defined _param-help (python rgbCloudMusic.py --help& goto :EOF)
python rgbCloudMusic.py %*