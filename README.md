# PhoneMove
利用python脚本，偷偷地将手机里的数据迁移到电脑上
原理

1.安卓里的adb调试

2.对文件的读写

3.监控有无新设备的插入

4.打开设备文件

5.对设备进行shell调试

6.进行数据迁移

###########################

其中代码中的

pull=commands.getstatusoutput('adb pull /sdcard/DCIM/Camera/ /home/a/Desktop/ ')

我是将相册中的相片放在了桌面。

###########################

## 注意
使用步骤
  1.将代码拷贝到本地
  2.sudo python phone.py
  3.出现ready然后等待很久出现ok
  4.再看看桌面
### *前提是得打开调试者模式，因为这些都是adb调试
