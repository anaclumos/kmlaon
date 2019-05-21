#
#  kmlaon.py
#  Created by Sunghyun Cho on May 21 2019.
#  Copyright © 2019 Sunghyun Cho. All rights reserved.
#

COMMENT = ''
POSTID  = ''
POSTURL = ''
USERID  = ''
USERPWD = ''
RUNTIME = '' # May 21 2019 12:50:15 PM

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
	driver.execute_script('return board_putCommentForm('+POSTID+')')
	driver.find_element_by_id('article_comment_write_'+POSTID)
	text_area = driver.find_element_by_xpath('//*[@id=\"article_comment_write_' + POSTID + '\"]/form/textarea').send_keys(COMMENT)
	driver.find_element_by_xpath('//*[@id="article_comment_write_' + POSTID + '"]/form/input[6]').click()

print("[댓글]:", COMMENT)
print("[타겟]:", str(RUNTIME))
print("[잔여]:", delta_t)
print("[예상]:", str(datetime.now() + delta_t))

prepare()
secs=delta_t.total_seconds()
t = Timer(secs, addcomment)
t.start()