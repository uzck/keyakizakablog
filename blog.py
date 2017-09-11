'''博客实体模块'''

class Blog:
    '''博客实体类'''

    def __init__(self, title='', memberid=0, membername='', date=''):
        '''初始化参数'''
        self._title = title
        self._memberid = memberid
        self._membername = membername
        self._date = date
        self._content = ''
        self._images = []

    @property
    def title(self):
        '''获取博客名称'''
        return self._title

    @property
    def memberid(self):
        '''获取成员id'''
        return self._memberid

    @property
    def membername(self):
        ''''获取成员姓名'''
        return self._membername

    @property
    def date(self):
        '''获取日期'''
        return self._date

    @property
    def content(self):
        '''获取博客内容'''
        return self._content

    @property
    def images(self):
        '''获取博客图片列表'''
        return self._images

    @title.setter
    def title(self, title):
        self._title = title

    @memberid.setter
    def memberid(self, member_id):
        self._memberid = member_id

    @membername.setter
    def membername(self, member_name):
        self._membername = member_name

    @date.setter
    def date(self, date):
        self._date = date

    @content.setter
    def content(self, content):
        self._content = content

    @images.setter
    def images(self, images):
        self._images = images

