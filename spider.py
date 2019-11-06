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

    def __init__(self):
        pass
