from PIL import Image
import qrcode
import os
import shutil
import time
import globalvar


globalvar._init()
def make_qrcode(data,icon_path,save_path):
    qr = qrcode.QRCode(version=5, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=8, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    img = img.convert("RGBA")
    icon = Image.open(icon_path)

    img_w, img_h = img.size
    factor = 4
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)

    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    icon = icon.convert("RGBA")
    img.paste(icon, (w, h), icon)
    # img.show()
    localtime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    qr_name = str(localtime)+'.png'
    globalvar.set_value('key', qr_name)
    img.save(qr_name)
    # print(qr_name)
    qr_road = os.getcwd()
    qr_path = qr_road+'\\'+qr_name
    # print(qr_path)
    shutil.move(qr_path,save_path)
