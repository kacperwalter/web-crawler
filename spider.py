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
        self.crawl_page('First spider', Spider.base_url)
        
    @staticmethod #"this is a static method so we dont need to pass the self arg"
    def boot(): # first spider is making project dir
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file) # first time spider is booted is taking links and saving them into a set
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url): # while crawling a page its good to display what page we are currently crawling
        # if for making sure if we didnt already crawled this page
        if page_url not in Spider.crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled ' + str(len(Spider.crawled))) # how many links in a waiting list and how many links already has been crawled
            Spider.add_links_to_queue(Spider.gather_link(page_url)) # adding sets of links to waitinglist | gather_link method is connecting to webpage and its gonna return a set of all of the links on webpage




