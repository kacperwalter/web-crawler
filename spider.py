from urllib.request import urlopen
from link_finder import LinkFinder
from general import *

class Spider:

    # Class variables (shared among all instances)
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = '' # HDD
    crawled_file = '' # HDD
    queue = set() # waiting list (RAM)
    crawled = set() # crawled pages (RAM)

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.queue_file = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawled_page('First spider', Spider.base_url)



