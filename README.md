# Web scraper for CV extraction
Tool is adapted for www.work.ua (soon will be configured for other Ukrainian job search websites).

## General info
After program starts, all CVs with PRO label (from pages `https://www.work.ua/resumes/?page={1..n}`) will be downloaded to "path" directory in `parse_resume` method. To increase/decrease number of pages for crawling, change range in `parse` method.

## How to use?
Install Scrapy and its dependencies from PyPI with:
```sh
pip install Scrapy
```
> Note: sometimes this may require solving compilation issues for some Scrapy dependencies depending on your operating system, so be sure to check the [Platform specific installation notes](https://docs.scrapy.org/en/latest/intro/install.html#intro-install-platform-notes).

For more details: [Scrapy installation guide](https://docs.scrapy.org/en/latest/intro/install.html#installation-guide)


To start crawler:
```sh
cd resume_spider
```
```sh
scrapy crawl work_spider
```
For more details: [Spiders — Scrapy 2.7.1 documentation](https://docs.scrapy.org/en/latest/topics/spiders.html)
