import re

import time
from bs4 import BeautifulSoup

from spider.pages import get_page
from web.models import Job, JobUrl


def get_job_urls(page):
    urls = re.compile(r'http://jobs.zhaopin.com/\w+?\.htm').findall(page)
    new_urls = []
    for url in urls:
        if not JobUrl.query.filter_by(url=url).first():
            new_urls.append(url)
            job_url = JobUrl(url, 1)
            job_url.save()
    return len(new_urls)


def get_new_details():
    urls = JobUrl.query.filter_by(has=0, source=1)
    for url in urls:
        if get_details(url.url):
            url.has = 1


def get_details(url):

    try:
        soup = BeautifulSoup(get_page(url), "html.parser")
        title = soup.find("div", attrs={"class": "inner-left fl"})
        pid = url.split("/")[-1][:-4]
        name = title.find("h1").string.strip()
        company = title.find("h2").get_text().strip()

        job_detail_html = soup.find("div", attrs={"class": "terminalpage-left"})
        job_li = job_detail_html.find("ul").find_all("li")

        salary = job_li[0].find("strong").get_text().strip()
        city = job_li[1].find("strong").get_text().strip()
        date = job_li[2].find("strong").get_text().strip()

        job_cont = soup.find("div", attrs={"class": "tab-inner-cont"})  # class="tab-inner-cont"的在界面中多次出现，但是第一次出现的却一直是需要的数据。
        detail = job_cont.get_text().strip().replace("\n", "")
        if not Job.query.filter_by(pid=pid).first():
            job = Job(pid, name, company, salary, city, date, detail)
            job.save()
        time.sleep(1)
        return True
    except Exception as err:
        print(err)
        return False


def main():
    base = "http://sou.zhaopin.com/jobs/searchresult.ashx?"

    # 参数设置
    city = "杭州"
    keyword = "python开发"

    url = base + "&jl=" + city + "&kw=" + keyword + "&p="

    for num in range(7):
        get_job_urls(get_page(url + str(num)))
        get_new_details()
        print("\r" + "-" * 10 + str(num) + "-" * 10, end="")

