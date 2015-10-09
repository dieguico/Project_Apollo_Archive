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
        print "[%s] Downloading %s\n"%(self.ident, name)
        urlretrieve(url, dest)

def download(urls, names, destfolder, numthreads=4):
    queue = Queue()
    for num, url in enumerate(urls):
        queue.put((url,names[num]))

    for i in range(numthreads):
        t = DownloadThread(queue, destfolder)
        t.start()

    queue.join()

#Download to the same place for everybody, only the pictures left
directory = path.join(path.expanduser('~/Desktop'),'NASA_Apollo_Project')
if not path.exists(directory):
    makedirs(directory)
done = glob(path.join(directory,'*.jpg'))

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


#4 parallel downloads should be enough ;)
download(urls, names, directory, 4) 