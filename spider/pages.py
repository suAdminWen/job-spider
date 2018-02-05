import logging
import requests


def get_page(url, headers=None):
    """通过uri获取网页"""
    page = ""
    try:
        headers = {
            'user-agent': "Mozilla/5.0",
        }
        req = requests.get(url, headers=headers)
        req.raise_for_status()
        req.encoding = req.apparent_encoding
        page = req.text
    except Exception as err:
        logging.warning(err)
    return page
