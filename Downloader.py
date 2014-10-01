__author__ = 'bcao'
from urllib import request
from urllib import error
import time
import sys
import os
import shutil
#http://mod.cri.cn/eng/ez/morning/2014/ezm140721.mp3

def myprint():
    print('hello')

ezFmBaseUrl = 'http://mod.cri.cn/eng/ez/morning/2014/ezm'
mp3Suffix = '.mp3'

persistPath = 'D:\\EzFM\\'
if not os.path.exists(persistPath):
    os.mkdir(persistPath)


todayDateTime = time.strftime("%y%m%d")


dateTimeToUse = todayDateTime

url = ezFmBaseUrl + dateTimeToUse + mp3Suffix
fileN = dateTimeToUse + mp3Suffix


try:
    response = request.urlopen(url)
    myprint()
except error.HTTPError as err:
    print('Failed to open mp3 file at date:' + dateTimeToUse + ' .HTTP error code: ' + str(err.code))

    exit()
except Exception as inst:
    print(type(inst))
    exit()

if not os.path.exists(os.path.join(persistPath + fileN)):
    with open(os.path.join(persistPath + fileN), 'wb') as out_file:
        shutil.copyfileobj(response, out_file)




