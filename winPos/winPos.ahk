;说明
;  记录指定程序窗口位置；恢复指定程序窗口位置
;参数
;  className operate
;      className - 程序名; 可以使用Window Spy查看
;      operate - 操作类型； [save 记录程序窗口位置;关闭程序] [recover 打开程序;恢复窗口位置]
#SingleInstance,Force
if(%0%<2)
    return

className = %1%
operate = %2%
tempPath = %A_ScriptDir%\%A_ScriptName%.ini
if (operate="save") {
    IfWinExist ahk_class %className%
    {
        WinGetPos, X, Y
        if (X=-32000 and Y=-32000) { ;程序最小化时
            X = NULL
            Y = NULL
        }
        WinClose
    }
    else
    {
        X := A_ScreenWidth/2
        Y := A_ScreenHeight/2
    }
    IniWrite, %X%, %tempPath%, %className%, x
    IniWrite, %y%, %tempPath%, %className%, y
    
} else if (operate=="recover") {
    IniRead, X, %tempPath%, %className%, x
    IniRead, y, %tempPath%, %className%, y
    if (X="ERROR" or Y="ERROR")
        return ;指定的程序未记录窗口位置

    Run, cloudmusic
    if (X!="NULL" or Y!="NULL") {
        WinWaitActive, ahk_class %className%
        WinMove, %X%, %Y%
    }
}



