import re

import time

from bs4 import BeautifulSoup

from spider.pages import get_page
from web.models import JobUrl, Job


def get_job_urls(page):
    urls = re.compile(r'/job_detail/\d+?.html').findall(page)
    prefix = "https://www.zhipin.com"
    new_urls = []
    for url in urls:
        full_url = prefix + url
        if not JobUrl.query.filter_by(url=full_url).first():
            new_urls.append(full_url)
            job_url = JobUrl(full_url, 2)  # boss直聘代码为2
            job_url.save()
    return len(new_urls)


def get_new_details():
    urls = JobUrl.query.filter_by(has=0, source=2)
    for url in urls:
        if get_details(url.url):
            url.has = 1


def get_details(url):
    time.sleep(5)
    try:
        soup = BeautifulSoup(get_page(url), "html.parser")
        title = soup.find("div", attrs={"class": "info-primary"})
        pid = url.split("/")[-1][:-5]
        name, salary = list(title.find("div", attrs={"class": "name"}).stripped_strings)
        date = title.find("span", "time").get_text().strip()[3:]
        company = soup.find("div", attrs={"class": "info-company"}).get_text().strip().split("\n")[0]
        detail = soup.find("div", attrs={"class": "text"}).get_text().strip()
        city = list(title.find("p").stripped_strings)[0].split("：")[1].strip()
        if not Job.query.filter_by(pid=pid).first():
            job = Job(pid, name, company, salary, city, date, detail)
            job.save()
            return True
    except Exception as err:
        print(err)
        return False


def main():
    base = "https://www.zhipin.com/c101210100/h_101210100/?query=python&page="

    for i in range(7):

        get_job_urls(get_page(base + str(i)))
        get_new_details()

