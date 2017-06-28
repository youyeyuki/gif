@echo off
echo 输入要免疫的U盘 盘符
set /p c=

%c%:

md autorun.inf

cd autorun.inf

md U盘防疫目录不要用此目录装东西...\\

echo 建立防疫目录完成
pause