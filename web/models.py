import datetime

from app import db


class Job(db.Model):
    pid = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(30))
    company = db.Column(db.String(30))
    salary = db.Column(db.String(20))
    city = db.Column(db.String(10))
    date = db.Column(db.String(8))
    details = db.Column(db.Text)

    def __init__(self, pid, name, company, salary, city, date, details):
        self.pid = pid
        self.name = name
        self.company = company
        self.salary = salary
        self.city = city
        self.date = date
        self.details = details

    def __repr__(self):
        return '<Job %r>' % self.name

    def save(self):
        db.session.add(self)
        db.session.commit()


class JobUrl(db.Model):
    pid = db.Column(db.String(25), primary_key=True)
    url = db.Column(db.String(70), unique=True)
    has = db.Column(db.Integer, default=0)  # 是否已经爬取网页
    source = db.Column(db.Integer)  # 来源(1.智联 2.boss直聘)

    def __init__(self, url, source):
        self.pid = url[24:]
        self.url = url
        self.source = source

    def __repr__(self):
        return '<JobUrl %r>' % self.url

    def save(self):
        db.session.add(self)
        db.session.commit()
