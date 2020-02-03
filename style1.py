import qrcode
import os
import shutil
import time
import globalvar


globalvar._init()
def make_qrcode(data,save_path):
    global  code_name
    qr = qrcode.QRCode(version=5, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=8, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    img = img.convert("RGBA")

    img_w, img_h = img.size
    factor = 4
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)

    # img.show()
    localtime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    qr_name = str(localtime)+'.png'
    globalvar.set_value('key', qr_name)
    img.save(qr_name)
    # print(qr_name)
    qr_road = os.getcwd()#C:\Code-Py\Qt
    qr_path = qr_road+'\\'+qr_name
    # print(qr_path)
    shutil.move(qr_path,save_path)
