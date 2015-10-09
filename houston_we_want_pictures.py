from sys import argv
from time import sleep
from os import path, makedirs
from csv import DictReader
from urllib import urlretrieve
from threading import Thread
from Queue import Queue
from glob import glob

# This class is a slightly-adapted version of http://stackoverflow.com/a/18883984/3174773 

class DownloadThread(Thread):
    def __init__(self, queue, destfolder):
        super(DownloadThread, self).__init__()
        self.queue = queue
        self.destfolder = destfolder
        self.daemon = True

    def run(self):
        while True:
            url, name = self.queue.get()
            try:
                self.download_url(url, name)
            except Exception,e:
                print "   Error: %s"%e
            self.queue.task_done()

    def download_url(self, url, name):
        dest = path.join(self.destfolder, name+'.jpg')
        print "[%s] Downloading %s"%(self.ident, name)
        urlretrieve(url, dest)

def download(urls, names, destfolder, numthreads):
    queue = Queue()

    for num, url in enumerate(urls):
        queue.put((url,names[num]))

    for i in range(numthreads):
        t = DownloadThread(queue, destfolder)
        t.start()

    queue.join()

default_directory=path.join(path.expanduser('~/Desktop'),'NASA_Apollo_Project')
default_threads=4

if __name__ == "__main__":
    #Download to the same place for everybody, only the pictures left
    print "-----------------------------------------------------------------------"
    for i in range(2): print ' '
    if len(argv)==1:
        destfolder=default_directory
        threads=default_threads
        print "#######################################################################"
        print "##       Using the default folder: %s"%(default_directory)
        print "##       Using %d threads."%(default_threads)
        print "#######################################################################"
    else:
        if path.isdir(argv[1]):
            print "#######################################################################"
            print "##       Using the folder: %s"%(arg[1])
            destfolder=argv[1]
        else:
            print "#######################################################################"
            print "##       The folder %s do not exists. Using the default folder: %s"%(argv[1],default_directory)
            destfolder=default_directory
        if len(argv)==3 and argv[2].isdigit and int(argv[2])<10:
            threads=int(argv[2])
            print "##       Using %d threads."%(threads)
            print "#######################################################################"
        else:
            print "##       Empty, wrong or huge number of threads. Using just %d."%(default_threads)
            print "#######################################################################"
            threads=default_threads
    for i in range(2): print ' '        
    print "-----------------------------------------------------------------------"
    try:
        with open('intro','r') as intro:
            saturn=intro.readlines()
            for i in range(5): print " "
            sleep(0.5)
            for el,row in enumerate(saturn[1:]):
                print row[:-1]
                sleep(abs(0.1-0.00025*(el+1)))
            for i in range(2): print " "
    except:
        print "Is better if you download 'intro' as well ;)"
        print "-----------------------------------------------------------------------"

    if not path.exists(destfolder):
        makedirs(destfolder)
    done = glob(path.join(destfolder,'*.jpg'))

    filename='photo_links'
    if path.exists(filename):
        op = open(filename, 'r')
        reader=DictReader(op)
        urls=[row['url_original'] for row in reader]
        op.seek(0)
        reader.next()
        names=[row['name'] for row in reader]
        op.close()
    
        tengui=[]
        for el,name in enumerate(names):
            if name in [d.split('/')[-1].split('.')[0] for d in done]:
                tengui.append(el)
            
        names = [i for j, i in enumerate(names) if j not in tengui]
        urls = [i for j, i in enumerate(urls) if j not in tengui]
    else:
        print 'Need picture links. Go find photo_links on my github  ;) https://github.com/dieguico/Project_Apollo_Archive'
    
    download(urls, names, destfolder, 4)