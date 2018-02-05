import logging
import requests


def get_page(url, headers=None):
    """通过uri获取网页"""
    try:
        # 完整的头部信息
        headers = headers or {'Upgrade-Insecure-Requests': '1',
                              'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                              'Accept-Encoding': 'gzip, deflate, sdch, br',
                              'Accept-Language': 'zh-CN,zh;q=0.8'
                              }

        # requests的Session可以自动保持cookie,不需要自己维护cookie内容
        session = requests.Session()

        req = session.get(url, headers=headers)
        req.raise_for_status()
        req.encoding = "utf-8"
        page = req.text
    except Exception as err:
        logging.warning(err)
        page = ""
    return page
