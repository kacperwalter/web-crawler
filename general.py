import os

# setting different "projects" for every different crawled website
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.mkdir(directory)

# creating queue and crawled files (if not crawled)
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt' #queue.txt => list on links that will be creawled
    crawled = project_name + '/crawled.txt'

    #checking if file exist before we create them
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '') # creating empty file

# creating new file ('w' is write mode)
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

# adding data onto an existing file ('a' means append file)
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

# delete the contents of file
def delete_file_contents(path):
    with open(path, 'w'):
        pass

# read a file and convert each line to set items (in sets items cannot be duplicated)
# 'rt' means read text
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        # looping through each line
        for line in f:
            results.add(line.replace('\n', ''))



