#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pyrgb
import subprocess
import re
import sqlite3
import os
import sys
import random
local_appdata = os.environ.get('LOCALAPPDATA')


def get_desk_wallpaper():
    sub = subprocess.Popen('''reg query "HKEY_CURRENT_USER\Control Panel\Desktop" /v WallPaper''', shell=True, stdout=subprocess.PIPE)
    desk_wallpaper = sub.communicate()[0]
    desk_wallpaper = str(desk_wallpaper,'gb2312')
    desk_wallpaper = re.split('    |\r\n', desk_wallpaper)
    return desk_wallpaper[5]

def get_img_dominant_color(img_path):
    convert_path = os.getcwd() + '\\imagemagick\\imagemagick-convert.exe'
    sub = subprocess.Popen(convert_path + ' \"' + img_path + '\" -scale 1x1 -format %[pixel:u] info:-', shell=True, stdout=subprocess.PIPE)
    rgbStr = sub.communicate()[0]
    rgbStr = str(rgbStr,'utf-8')
    [color_temp, color_r, color_g, color_b, color_temp] = re.split('\(|\)|,', rgbStr)
    return [int(color_r), int(color_g), int(color_b)]

def get_random_color():
    return [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

def rgb_2_hsl(rgb):
    return tuple(pyrgb.rgb_hsl(rgb[0], rgb[1], rgb[2]))

def cloud_music_close():
    os.system(os.getcwd() + '\\winPos\\winPos.ahk OrpheusBrowserHost save')

def cloud_music_open():
    os.system(os.getcwd() + '\\winPos\\winPos.ahk OrpheusBrowserHost recover')

def cloud_music_update_skin(hsl):
    conn = sqlite3.connect(local_appdata + '\\Netease\\CloudMusic\\webapp\\Local Storage\\orpheus_orpheus_0.localstorage')
    cursor = conn.cursor()
    skin_key = 'NM_SETTING_SKIN'
    skin_value = '{"isCustomed":true,"type":"default","name":"default","selected":{"type":"color","name":"hsl' + str(hsl) + '"},"colorSkin":{"preset":[{"type":"color","name":"hsl(343, 100%, 68%)"},{"type":"color","name":"hsl(344, 100%, 74%)"},{"type":"color","name":"hsl(324, 99%, 73%)"},{"type":"color","name":"hsl(234, 92%, 71%)"},{"type":"color","name":"hsl(213, 80%, 60%)"},{"type":"color","name":"hsl(200, 81%, 57%)"},{"type":"color","name":"hsl(147, 62%, 44%)"},{"type":"color","name":"hsl(93, 78%, 45%)"},{"type":"color","name":"hsl(44, 85%, 48%)"},{"type":"color","name":"hsl(20, 100%, 67%)"},{"type":"color","name":"hsl(2, 97%, 71%)"},{"type":"color","name":"hsl(2, 98%, 65%)"}]}}'
    cursor.execute('UPDATE ItemTable SET value=? WHERE key=?', (skin_value, skin_key))
    conn.commit()
    cursor.close()
    conn.close()


def process(argv):
    if len(argv) == 0:
        mode = 2
    else:
        mode = int(argv[0])


    if mode == 0:
        rgb = [int(argv[1]), int(argv[2]), int(argv[3])]
    elif mode == 1:
        rgb = get_random_color()
    elif mode == 2:
        desk_wallpaper = get_desk_wallpaper()
        rgb = get_img_dominant_color(desk_wallpaper)
    else:
        rgb = get_random_color()

    hsl = rgb_2_hsl(rgb)
    cloud_music_close()
    cloud_music_update_skin(hsl)
    cloud_music_open()


if __name__=="__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] in ['/?', '-h', '--help', 'help']:
            print('''mode [R] [G] [B]
    mode - 模式[0|color] [1|random] [2|desk] 默认值为2
        0|color - specifiedColor需要指定RGB值
        1|random - randomColor随机颜色
        2|desk - deskWallpaperColor桌面壁纸主色''')
            sys.exit()

    process(sys.argv[1:])