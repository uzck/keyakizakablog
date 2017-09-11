'''每个月发博日期集合'''
import requests
from bs4 import BeautifulSoup

class PostDateGetter:
    '''发博日期获取类'''

    def __init__(self, month=0):
        self._month = month
        self._days = []

    @property
    def month(self):
        '''月份'''
        return self._month

    @property
    def days(self):
        '''每个月发博的日期'''
        return self._days

    @month.setter
    def month(self, month):
        self._month = month

    @days.setter
    def days(self, days):
        self._days = days

    def get_days(self, member_id, year_month):
        '''根据月份获取该月发博的时间
        2017年8月的格式为201708'''
        # 服务器地址
        host = 'http://www.keyakizaka46.com/s/k46o/diary/member/list?ima=0000'
        # 拼接为博客列表地址
        final_link = host + '&ct=' + str(member_id) + '&dy=' + year_month

        browser = requests.get(final_link)
        if browser.status_code != 200:
            # 获取页面失败
            return
        # with open('text.txt', 'wb') as f:
        #     f.write(browser.text.encode('utf-8'))
        document = BeautifulSoup(browser.text, 'lxml')
        # 页面的日历部分
        # days_class = 'cale_day'
        calender = document.find('table', class_='cale_table')
        trs = calender.find_all('tr')
        trs = trs[2:]
        for tr in trs:
            tds = tr.find_all('td')
            # 含有超链接的td标签里的内容是发博的日期
            for td in tds:
                if td.find('a') != None:
                    self._days.append(year_month + td.find('a').text)

