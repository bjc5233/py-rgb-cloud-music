#!/usr/bin/python
#! -*- coding: utf8 -*-
# 说明
#   修改网易云音乐主题色，匹配当前壁纸
# 注意py命名规范
#   1、变量
#       每个单词都使用小写字母；单词与单词之间用_连接；例如：num, file_name
#   2、常量
#       全部单词大写；单词之间用_连接；例如：COUNT，FIRST_NAME
#   3、函数
#       每个单词都使用小写字母；单词之间用_连接；例如：def eat([形参]):    def shou_top([形参]):
#   4、类
#       大驼峰命名法(每个单词首字母大写)；例如：class MyClass(object):    class Persion(object):
#   5、全局变量
#       全局变量：采用gl_或g_加变量名
# external
#   date       2020-07-26 12:09:48
#   face       ●﹏●
#   weather    Tiantai Cloudy 30℃
import pyrgb
import subprocess
import re
import sqlite3
import os
import sys
import random
import time
import win32gui
import win32con

def get_desk_wallpaper():
    sub = subprocess.Popen('''reg query "HKEY_CURRENT_USER\Control Panel\Desktop" /v WallPaper''', shell=True, stdout=subprocess.PIPE)
    desk_wallpaper = sub.communicate()[0]
    desk_wallpaper = str(desk_wallpaper,'gb2312')
    desk_wallpaper = re.split('    |\r\n', desk_wallpaper)
    return desk_wallpaper[5]

def get_img_dominant_color(img_path):
    convert_path = os.getcwd() + '\\resources\\imagemagick\\imagemagick-convert.exe'
    sub = subprocess.Popen(convert_path + ' \"' + img_path + '\" -scale 1x1 -format %[pixel:u] info:-', shell=True, stdout=subprocess.PIPE)
    rgb_str = sub.communicate()[0]
    rgb_str = str(rgb_str,'utf-8')
    [color_temp, color_r, color_g, color_b, color_temp] = re.split('\(|\)|,', rgb_str)
    return [int(color_r), int(color_g), int(color_b)]

def get_random_color():
    return [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

def RGB_2_HSL(rgb):
    return tuple(pyrgb.rgb_hsl(rgb[0], rgb[1], rgb[2]))

def close_cloud_music():
    print('cloud music close')
    handle = win32gui.FindWindow("OrpheusBrowserHost", None)
    if handle != 0:
        win32gui.PostMessage(handle, win32con.WM_CLOSE, 0, 0)

def open_cloud_music():
    print('cloud music open')
    os.startfile(os.environ.get('PROGRAMFILES(X86)') + "\\Netease\\CloudMusic\\cloudmusic.exe")

def update_cloud_music_skin(hsl):
    local_app_data = os.environ.get('LOCALAPPDATA')
    conn = sqlite3.connect(local_app_data + '\\Netease\\CloudMusic\\webapp\\Local Storage\\orpheus_orpheus_0.localstorage')
    cursor = conn.cursor()
    skin_key = 'NM_SETTING_SKIN'
    skin_value = '{"isCustomed":true,"type":"default","name":"default","selected":{"type":"color","name":"hsl' + str(hsl) + '"},"colorSkin":{"preset":[{"type":"color","name":"hsl(343, 100%, 68%)"},{"type":"color","name":"hsl(344, 100%, 74%)"},{"type":"color","name":"hsl(324, 99%, 73%)"},{"type":"color","name":"hsl(234, 92%, 71%)"},{"type":"color","name":"hsl(213, 80%, 60%)"},{"type":"color","name":"hsl(200, 81%, 57%)"},{"type":"color","name":"hsl(147, 62%, 44%)"},{"type":"color","name":"hsl(93, 78%, 45%)"},{"type":"color","name":"hsl(44, 85%, 48%)"},{"type":"color","name":"hsl(20, 100%, 67%)"},{"type":"color","name":"hsl(2, 97%, 71%)"},{"type":"color","name":"hsl(2, 98%, 65%)"}]}}'
    cursor.execute('UPDATE ItemTable SET value=? WHERE key=?', (skin_key, skin_value))
    conn.commit()
    cursor.close()
    conn.close()


def process(argv):
    if len(argv) == 0:
        mode = 2
    else:
        mode = int(argv[0])


    print('mode:', mode)
    if mode == 0:
        rgb = [int(argv[1]), int(argv[2]), int(argv[3])]
    elif mode == 1:
        rgb = get_random_color()
    elif mode == 2:
        desk_wallpaper = get_desk_wallpaper()
        rgb = get_img_dominant_color(desk_wallpaper)
    else:
        rgb = get_random_color()
    print('rgb:', rgb)

    hsl = RGB_2_HSL(rgb)
    print('hsl:', hsl)
    close_cloud_music()
    update_cloud_music_skin(hsl)
    time.sleep(1)
    open_cloud_music()


if __name__=="__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] in ['/?', '-h', '--help', 'help']:
            print('''[mode] [R] [G] [B]
    mode - 模式[0|color] [1|random] [2|desk] 默认值为2
        0|color - specifiedColor需要指定RGB值
        1|random - randomColor随机颜色
        2|desk - deskWallpaperColor桌面壁纸主色''')
            sys.exit()

    process(sys.argv[1:])
    exit(0)