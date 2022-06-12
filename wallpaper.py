from sqlite3 import Timestamp
import psutil, datetime
import ctypes
import datetime
from PIL import Image,ImageFont,ImageDraw


# CPU使用率
cpu = psutil.cpu_percent(interval=1)
cputext = "cpu:" + str(cpu) + "%"

# メモリ使用率
mem = psutil.virtual_memory() 
memResult = str((mem.percent /100)* 7.7)
memtext = "ram:" + memResult[:4] + "GB/7.70GB (" + str(mem.percent) + "%)"

# バッテリー使用率
battery = psutil.sensors_battery()
if battery == None:
    batterytext = "battery:None"
else:
    batterytext = "battery:" + str(battery.percent) + "%"

# 起動時間
bootTime = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
boottext = "boot-time:" + bootTime

#更新時間
JST = datetime.timezone(datetime.timedelta(hours=9), 'JST')
now = datetime.datetime.now(JST)
Time = now.strftime('%Y-%m-%d %H:%M:%S')
Timestamp = "road-time:" + Time

image_path = "<path>copy.jpg"
font_path = "<path>"
font_size = 80 #文字の大きさ
color = (255,255,255)#文字の色
result_path = "<path>result.jpg"
 
image = Image.open(image_path)
font = ImageFont.truetype(font_path,font_size)#フォントの指定
draw = ImageDraw.Draw(image)
draw.text((6900,3800),"- - - - - - - - STATUES - - - - - - - -",font=font,fill=(0,255,255))
draw.text((6900,3890),cputext,font=font,fill=color)
draw.text((6900,3980),memtext,font=font,fill=color)
draw.text((6900,4070),batterytext,font=font,fill=color)
draw.text((6900,4160),boottext,font=font,fill=color)
draw.text((6900,4250),Timestamp,font=font,fill=(255, 110, 226))
image.save(result_path)


ctypes.windll.user32.SystemParametersInfoW(20, 0, "<path>result.jpg" , 0)
