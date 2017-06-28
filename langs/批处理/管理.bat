@echo off
color 0a
@rem 注析用
:menu 
echo 请输入下列数字进行操作 输入exit 退出 
echo create by youye
echo 1.5s后关机
echo 2.ipconfig
echo 3.清理回收站
echo 4.取消关机
echo 5.打开QQ
echo 6.海词词典
echo 7.idea
echo 8.FTP
echo 9.wamp
echo 10.processing
echo 11.AU
echo 12.AE
echo 13.Pr
echo 14.Q-dir
echo 15.Droid4
echo 16.360yun
echo 17.360浏览器
echo 18.vs
echo 19.vm
echo 20.v赤红
echo 21.qq旋风
echo 22.vncserver
echo --------------------------------------
echo 115.115

set /p c=  自己选一个吧:

if %c%==1 shutdown -s -t 5
if %c%==2 ipconfig
if %c%==3 nircmd emptybin >nul 

if %c%==4 shutdown -a 
if %c%==5  "D:\Program Files (x86)\Tencent\QQ\Bin\QQ.exe"
if %c%==6  "D:\Program Files (x86)\dict.cn\Dict4\Dict.exe"
if %c%==7  "D:\Program Files (x86)\JetBrains\IntelliJ IDEA 15.0.3\bin\idea64.exe"
if %c%==8  "F:\Xlight_FTP_Server_3.6.2\xlight.exe
if %c%==9  "F:\wamp\wampmanager.exe"
if %c%==10 "D:\processing-2.2.1\processing.exe"
if %c%==11 "D:\Program Files\Adobe\Adobe Audition CS6\Adobe Audition CS6.exe"
if %c%==12 "D:\Program Files\Adobe\Adobe After Effects CS6\Support Files\AfterFX.exe"
if %c%==13 "D:\Program Files\Adobe\Adobe Premiere Pro CS6\Adobe Premiere Pro.exe"
if %c%==14 "D:\Program Files\Tool\Q-Dirx64\Q-Dir.exe"
if %c%==15 "D:\Android\Droid4X\Droid4X.exe"
if %c%==115 "D:\115_inject\115Chrome\Application\115chrome.exe"
if %c%==16 "D:\Program Files (x86)\360\360WangPan\360WangPan.exe"
if %c%==17  "D:\360_inject\360se6\Application\360se.exe"
if %c%==18 "D:\Program Files (x86)\Microsoft Visual Studio 11.0\Common7\IDE\devenv.exe"
if %c%==19 "D:\VM\vmware.exe"
if %c%==20 "C:\Users\Wings\Desktop\ch\C H.exe"
if %c%==21 "D:\Program Files (x86)\Tencent\QQDownload\QQDownload.exe"
if %c%==22 "J:\tool\program\TightVNC\tvnserver.exe"
if %c%==q  exit


pause
cls
goto menu

