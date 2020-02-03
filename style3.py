from MyQR import myqr
import os
import shutil
import re
import time
import globalvar


globalvar._init()
def make_qrcode(data,icon_path,save_path):
    localtime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    suffix = os.path.splitext(icon_path)[1]
    if suffix == '.gif':
        suffix == '.gif'
    else :
        suffix == '.png'

    qr_name = str(localtime) +suffix
    globalvar.set_value('key', qr_name)
    # print(qr_name)
    myqr.run(words=data,version=6,picture=icon_path,colorized=True,save_name=qr_name)
    qr_road=os.getcwd()
    qr_path=qr_road+'\\'+qr_name
    # print(qr_path)
    shutil.move(qr_path,save_path)

def is_Chinese(data):
    zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
    match = zhPattern.search(data)
    if match:
        return True
    return False
