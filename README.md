## 一个招聘信息的爬虫网站

定向爬取“智联招聘”、“Boss直聘”、“拉钩”等招聘网站的职位信息。

预期目标是获取、分析招聘信息。目前只完成第一步的第一步，就是获取一些信息，但是并没有进行处理。

## 用到的技术

- requests+BeautifulSoup
- sqlite数据库
- web框架：Flask
- python版本3.6

## 目前实现的功能

---
#### 2018-2-5

- 仅实现智联、Boss直聘网站中的部分python职位的信息爬取。
- 实现定向爬取，获取职位的基本信息，但是数据中存在脏数据。
- 保存数据。

