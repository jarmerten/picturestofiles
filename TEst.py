import zipfile
from PIL import Image
import os
import glob
import sys
import shutil
import json


def main():
    filelocation = sys.argv[1]
    with zipfile.ZipFile(filelocation) as myzip:
        filepath = os.path.splitext(filelocation)[0]
        print(filepath)
        myzip.extractall(filepath)
        print('starting......')
        run1(filepath)


def run1(filepath):
    with open((filepath + '\\manifest.json')) as f:
        data = []
        data = json.load(f)
        run10(f, data, filepath)
    run4(data,filepath)

def run2(filepath,lining,silverlining,liningthisup):
    size = 100, 100
    im = Image.open(filepath + '\\' + liningthisup)
    im.thumbnail(size)
    im.save(filepath + '\\' + lining + '\\' + silverlining + '\\' + liningthisup + ".thumbnail.jpg")
    shutil.move(filepath + '\\' + liningthisup, filepath + '\\' + lining + '\\' + silverlining + '\\' + liningthisup)

def run3(filepath,lining,silverlining,liningthisup, linemeupnow):
    size = 100, 100
    im = Image.open(filepath + '\\' + linemeupnow)
    im.thumbnail(size)
    im.save(filepath + '\\' + lining + '\\' + silverlining + '\\' + liningthisup + '\\' + linemeupnow + ".thumbnail.jpg")
    shutil.move(filepath + '\\' + linemeupnow,filepath + '\\' + lining + '\\' + silverlining + '\\' + liningthisup + '\\' + linemeupnow)

def run4(data,filepath):
    filename = data['zip_name']
    storefilename = os.path.splitext(filename)[0]
    os.remove(filepath + '\\manifest.json')
    shutil.make_archive(os.path.dirname(filepath) + '\\' + storefilename, "zip", filepath)
    shutil.rmtree(filepath)
    print('finished')

def run5(filepath,linemeupnow,lining,silverlining,liningthisup):
    if (linemeupnow.endswith('jpg') or linemeupnow.endswith('jpeg')):
        run3(filepath, lining, silverlining, liningthisup, linemeupnow)
    else:
        pass

def run6(data,filepath,liningthisup,lining,silverlining):
    if (liningthisup.endswith('jpg') or liningthisup.endswith('jpeg')):
        run2(filepath, lining, silverlining, liningthisup)
    else:
        os.makedirs(filepath + '\\' + lining + '\\' + silverlining + '\\' + liningthisup)
        for linemeupnow in data['directory_structure'][lining][silverlining][liningthisup]:
            run5(filepath, linemeupnow, lining, silverlining, liningthisup)

def run7(data,lining,silverlining,filepath):
    for liningthisup in data['directory_structure'][lining][silverlining]:
        run6(data, filepath, liningthisup, lining, silverlining)

def run8(data,lining,filepath):
    for silverlining in data['directory_structure'][lining]:
        os.makedirs(filepath + '\\' + lining + '\\' + silverlining)
        run7(data, lining, silverlining, filepath)

def run9(data,filepath):
    for lining in data['directory_structure']:
        os.makedirs(filepath + '\\' + lining)
        run8(data, lining, filepath)

def run10(f,data,filepath):
    for line in f:
        data.append(json.loads(line))
    run9(data, filepath)
if __name__ == "__main__": main()


