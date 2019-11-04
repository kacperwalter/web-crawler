import os

# setting different "projects" for every different crawled website
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.mkdir(directory)


# creating queue and crawled files (if not crawled)
def create_data_files(project_name, base_url):
    queue = project_name + 'queue.txt' #queue.txt => list on links that will be creawled
    crawled = project_name + 'crawled.txt'

    #checking if file exist before we create them
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '') # creating empty file

# creating new file
def write_file(path, data):
    f = open(path, 'w')
    f.writable(data)
    f.close()




