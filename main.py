#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import sys
import warnings
warnings.filterwarnings("ignore")

yellow, green, blue, purple, bluedark, gray, difficulties = [], [], [], [], [], [], []
colors = { '1r': 0, '2o': 0, '3y': 0, '4g': 0, '5b': 0, '6p': 0, '7d': 0, '8g': 0 }
#topics = map(lambda x: x[1: -1], raw_input().split())
user = raw_input()
urlUser = 'https://www.luogu.org/space/show?uid=' + user
urlBase = 'https://www.luogu.org/problemnew/show/'
headers = {
    u'Referer': u'https://www.luogu.org/recordnew/lists?uid=10000',
    u'Accept': u'text/html, */*; q=0.01',
    u'Accept-Encoding': u'gzip, deflate, br',
    u'Accept-Language': u'zh-CN,zh;q=0.9',
    u'User-Agent': u'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'
}

# 搞搞 UTF-8
reload(sys)
sys.setdefaultencoding('utf-8')
type = sys.getfilesystemencoding()

f = open("d:\\LgData.txt", "w") # 仅用于统计这次爬虫运行耗费了多少流量

# 获取个人主页信息
v = requests.get(url = urlUser, headers = headers, verify = False)
soup1 = BeautifulSoup(v.text, 'lxml')
res = soup1.find('div', {'class': 'lg-article am-hide-sm'})
topics = map(lambda x: x[1: -1], res.text.split())

# 第一个元素不是题目
topics.pop(0)

finished = 0

for topic in topics:
    try:
        v = requests.get(url = urlBase + topic, headers = headers, verify = False, timeout = 10)
    except:
        #v = requests.get(url = urlBase + topic, headers = headers, verify = False, timeout = 10)
        #v = requests.get(url = urlBase + topic, headers = headers, verify = False, timeout = 10)
        print topic, "Error!"
        continue
    
    #f.write(v.text)
    v = v.text#.decode('utf-8').encode(type)

    soup = BeautifulSoup(v, 'lxml')
    try:
        difficulty = soup.findAll('span', {'class': 'lg-right'})[2].text # 获取难度
        difficulties.append(difficulty)
        # 不知道为什么，每次尝试用字典都爆异常，所以暴力 if 
        if difficulty == '普及/提高-':
            print topic, "Yellow"
            yellow.append(topic)
        elif difficulty == '普及+/提高':
            print topic, "Green!"
            green.append(topic)
        elif difficulty == '提高+/省选-':
            print topic, "Blue!!"
            blue.append(topic)
        elif difficulty == '省选/NOI-':
            print topic, "Purple!!!"
            purple.append(topic)
        elif difficulty == 'NOI/NOI+/CTSC':
            print topic, "BlueDark!!!!"
            bluedark.append(topic)
        elif difficulty == '尚无评定':
            print topic, "Gray??"
            gray.append(topic)
        else:
            print topic
    except:
        print topic, "Didn't allowed!" # 无权查看的题目
    
    finished += 1
    os.system('title U' + user + ': ' + str(finished) + '/' + str(len(topics)))

print('------------------------------------')

yellowPlus, greenPlus = 0, 0

difficulties.sort()
for i in difficulties:
    #print i#, d[i]
    if i == '入门难度':
        colors['1r'] += 1
    if i == '普及-':
        colors['2o'] += 1
    if i == '普及/提高-':
        colors['3y'] += 1
        yellowPlus += 1
    if i == '普及+/提高':
        colors['4g'] += 1
        yellowPlus += 1
        greenPlus += 1
    if i == '提高+/省选-':
        colors['5b'] += 1
        yellowPlus += 1
        greenPlus += 1
    if i == '省选/NOI-':
        colors['6p'] += 1
        yellowPlus += 1
        greenPlus += 1
    if i == 'NOI/NOI+/CTSC':
        colors['7d'] += 1
        yellowPlus += 1
        greenPlus += 1
    if i == '尚无评定':
        colors['8g'] += 1
print('------------------------------------')

print 'Red: ', colors['1r']
print 'Orange: ', colors['2o']
print 'Yellow: ', colors['3y']
print 'Green: ', colors['4g']
print 'Blue: ', colors['5b']
print 'Purple: ', colors['6p']
print 'Bluedark: ', colors['7d']
print 'Gray: ', colors['8g']

print('------------------------------------')

print '\n', str(colors['3y']), 'Yellow:'
for i in range(len(yellow)):
    print yellow[i], 
    if (i + 1) % 10 == 0:
        print '\n',
print '\n', str(colors['4g']), 'Green:'
for i in range(len(green)):
    print green[i],
    if (i + 1) % 10 == 0:
        print '\n',
print '\n', str(colors['5b']), 'Blue:'
for i in range(len(blue)):
    print blue[i], 
    if (i + 1) % 10 == 0:
        print '\n',
print '\n', str(colors['6p']), 'Purple:'
for i in range(len(purple)):
    print purple[i], 
    if (i + 1) % 10 == 0:
        print '\n',
print '\n', str(colors['7d']), 'Bluedark:'
for i in range(len(bluedark)):
    print bluedark[i], 
    if (i + 1) % 10 == 0:
        print '\n',
print '\n', str(colors['8g']), 'Gray:'
for i in range(len(gray)):
    print gray[i], 
    if (i + 1) % 10 == 0:
        print '\n',
print "\n"

print('------------------------------------')

print 'Yellow+: ', yellowPlus
print 'Green+: ', greenPlus
