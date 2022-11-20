# Web scraper for CV extraction
Tool is adapted for www.work.ua (soon will be configured for other Ukrainian job search websites).
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
