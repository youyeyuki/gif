@echo off
rem  解包D:\Program Files (x86)\Tencent\QQ\Plugin\Com.Tencent.Advertisement 到一个目录运行bat 删除 重新打包 替换

echo "删除QQ聊天窗口广告"
rm Bundle\I18N\2052\UrlBundle.xml.enc

echo "QQ视频广告"
rm Bundle\Themes\Default\com.tencent.advertisement\RSLinkADNode.gmd
rm Bundle\Themes\Default\com.tencent.advertisement\RSLinkGDTADNode.gmd
rm Bundle\Themes\Default\com.tencent.advertisement\RSVedioADNode.gmd

echo "如果以上任意执行错误 可能是版本不同 记住删除前备份"
pause