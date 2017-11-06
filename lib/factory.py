#!/usr/bin/python
# __author__ = 'jasonsheh'
# -*- coding:utf-8 -*-

from database.database import Database

from lib.subdomain import AllDomain
from lib.sendir import SenDir
from lib.crawler import Crawler
from lib.port import Port
from lib.vul import Vul

import requests


def site_scan(domain):
    if domain.startswith('http://www.'):
        domain = domain[11:]
    if domain.startswith('https://www.'):
        domain = domain[12:]
    if domain.startswith('http://'):
        domain = domain[7:]
    if domain.startswith('https://'):
        domain = domain[8:]
    if domain.startswith('www.'):
        domain = domain[4:]
    if domain.endswith('/'):
        domain = domain[:-1]

    # id = Database().insert_task(domain)
    domains = AllDomain(domain).run()

    SenDir(domains).run()

    '''
    Port(domains, id).run()

    print('漏洞扫描')
    for domain in domains:
        url = Crawler(domain).scan()
        Vul(url, id).run()
    '''
