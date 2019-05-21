#
#  kmlaon.py
#  Created by Sunghyun Cho on May 21 2019.
#  Copyright © 2019 Sunghyun Cho. All rights reserved.
#

COMMENT = 'testflight'
POSTURL = 'https://kmlaonline.net/board/all_announce/view/480865'
POSTID  = '480865'
DATFILE = open("userdat.txt", "r")
USERDAT = DATFILE.readlines()
USERID  = USERDAT[0][:-1]
USERPWD = USERDAT[1]
RUNTIME = 'May 21 2019 02:45:00 PM' # May 21 2019 12:50:15 PM

#--------------------------------------------------
from datetime import datetime, timedelta
from threading import Timer
from selenium import webdriver
#--------------------------------------------------
op = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
op.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome('./chromedriver', options = op)
#--------------------------------------------------
x = datetime.now()
y = datetime.strptime(RUNTIME, '%b %d %Y %I:%M:%S %p')
delta_t=y-x
#--------------------------------------------------

def prepare():
	driver.get(POSTURL)
	driver.find_element_by_name('id').send_keys(USERID)
	driver.find_element_by_name('pwd').send_keys(USERPWD + '\n')

def addcomment():
	print("Adding comment...", end = "")
	driver.execute_script('return board_putCommentForm('+POSTID+')')
	driver.find_element_by_id('article_comment_write_'+POSTID)
	t = driver.find_element_by_xpath('//*[@id="article_comment_write_' + POSTID + '"]/form/textarea')
	t.send_keys(COMMENT)
	t.submit()
	print("Done.")

print("[작성할 댓글]:", COMMENT)
print("[예약된 시간]:", str(RUNTIME))
print("[카운트 다운]:", delta_t)
print("[작성될 시간]:", str(datetime.now() + delta_t))

prepare()
secs=delta_t.total_seconds()
t = Timer(secs, addcomment)
t.start()