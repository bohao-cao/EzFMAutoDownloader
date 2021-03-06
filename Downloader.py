__author__ = 'bcao'
from urllib import request
from urllib import error
import sys
import time
import os
from datetime import date, timedelta
import shutil
from os.path import isfile, join
import logging
import datetime
#http://mod.cri.cn/eng/ez/morning/2014/ezm140721.mp3

if sys.platform.startswith('win'):
    persistPath = 'D:\\EzFM\\'
elif sys.platform.startswith('darwin'):
    persistPath = '/Users/bohaocao/Dropbox/EzFm/'

logfileName= persistPath + 'log.log'
logging.basicConfig(filename=logfileName,format='%(asctime)s %(message)s', datefmt='%m/%d/%y %I:%M:%S %A',level=logging.INFO)
logfileSizeInBytes = len(open(logfileName,'rb').read())
#Bigger than 1MB
if logfileSizeInBytes > 1024 * 1024:
    open(logfileName,'w').truncate()

ezFmBaseUrl = 'http://mod.cri.cn/eng/ez/morning/2015/ezm'
mp3Suffix = '.mp3'

if not os.path.exists(persistPath):
    os.mkdir(persistPath)

todayDateTime = time.strftime("%y%m%d")
todayWeekday = time.strftime('%A')

#Stop working on weekends
if todayWeekday.startswith('Sun') or todayWeekday.startswith('Sat'):
    logging.info('Today is weekend, program will not run')
    exit()

#Delete files that are older than 7 days.
files = [f for f in os.listdir(persistPath) if isfile(join(persistPath, f))]
for f in files:
    createT = os.path.getctime(join(persistPath,f))
    lastOpenT = os.stat(join(persistPath,f)).st_atime
    #omit the ones that haven't been opened
    if createT == lastOpenT:
        continue
    if time.time() - createT> 7*60*60*24:
        logging.info('Remove old file ' + persistPath + f)
        os.remove(join(persistPath,f))


x = date.today()
# backdoor for hacking. this example: get yesterday's date
#x = x - timedelta(days = 1)
dateTimeToUse = x.strftime('%y%m%d')

url = ezFmBaseUrl + dateTimeToUse + mp3Suffix
fileN = dateTimeToUse + mp3Suffix


try:
    logging.info("Begin getting response from url: " + url)
    response = request.urlopen(url)
    logging.info('Downloading ' + persistPath + fileN + ' starts.')
except error.HTTPError as err:
    logging.error('Failed to open mp3 file at date: ' + dateTimeToUse + ' .HTTP error code: ' + str(err.code))
    exit()
except Exception as inst:
    logging.error(type(inst))
    exit()


if not os.path.exists(os.path.join(persistPath + fileN)):
    with open(os.path.join(persistPath + fileN), 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
        logging.info('SUCCESSFULLY Downloaded ' + fileN)
        exit()
else:
    logging.info('File '+ persistPath + fileN + ' already exits.')

