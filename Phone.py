#!/usr/bin/env python
# coding=utf-8
import time
import commands
import os
usb=commands.getstatusoutput('lsusb |head -n 1|grep -E -o [A-Za-z0-9]{4}:[A-Za-z0-9]{4}')
while 1 :
    us2=commands.getstatusoutput('lsusb|head -n 1|grep -E -o [A-Za-z0-9]{4}:[A-Za-Z0-9]{4}')
    if us2 == usb:
        continue
    else:
        str=us2[1]
        id=str.partition(':')[0]
        file=open('/etc/udev/rules.d/51-Android.rules','w')
        file.write("SUBSYSTEM==\"usb\", ATTR{idVendor}==\""+id+"\", MODE=\"0666\"")
        file.close()
	str='0x'+id
        fil=open('adb_usb.ini','w')
        fil.write("0x"+id)
        fil.close()
	ls=commands.getstatusoutput("cp adb_usb.ini ~/.android/adb_usb.ini")
    	us2=commands.getstatusoutput('chmod 755 ~/.android/adb_usb.ini')
        adb=commands.getstatusoutput('adb kill-server|adb start-server|adb devices')	
	print 'ready'
	pull=commands.getstatusoutput('adb pull /sdcard/DCIM/Camera/ /home/a/Desktop/ ')
	print 'OK'
