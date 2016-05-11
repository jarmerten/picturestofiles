import zipfile
from PIL import Image
import os
import glob
import sys
import shutil
import json
filelocation = sys.argv[1]
with zipfile.ZipFile(filelocation) as myzip:
    filepath = os.path.splitext(filelocation)[0]
    print(filepath)
    myzip.extractall(filepath)
    data = []
    print('starting......')
    with open((filepath + '\\manifest.json')) as f:
            data = []
            data = json.load(f)
            for line in f:
                data.append(json.loads(line))
            for lining in data['directory_structure']:
                os.makedirs(filepath + '\\'+lining)
                for silverlining in data['directory_structure'][lining]:
                    os.makedirs(filepath+ '\\' + lining+'\\'+silverlining)
                    for liningthisup in data['directory_structure'][lining][silverlining]:
                        if (liningthisup.endswith('jpg') or liningthisup.endswith('jpeg')):
                            size = 100, 100
                            im = Image.open(filepath+'\\'+liningthisup)
                            im.thumbnail(size)
                            im.save(filepath+'\\'+lining+'\\'+silverlining+'\\'+liningthisup + ".thumbnail.jpg")
                            shutil.move(filepath+'\\'+liningthisup, filepath+'\\'+lining+'\\'+silverlining+'\\'+liningthisup)
                        else:
                            os.makedirs(filepath +'\\'+ lining + '\\' + silverlining + '\\' + liningthisup )
                            for linemeupnow in data['directory_structure'][lining][silverlining][liningthisup]:
                                if (linemeupnow.endswith('jpg') or linemeupnow.endswith('jpeg')):
                                    size = 100, 100
                                    im = Image.open(filepath +'\\'+ linemeupnow)
                                    im.thumbnail(size)
                                    im.save(filepath +'\\'+ lining + '\\' + silverlining + '\\' + liningthisup + '\\' + linemeupnow + ".thumbnail.jpg")
                                    shutil.move(filepath +'\\'+ linemeupnow, filepath +'\\'+ lining + '\\' + silverlining + '\\' + liningthisup + '\\' + linemeupnow)
                                else:
                                    pass
                    filename = data['zip_name']
                    storefilename = os.path.splitext(filename)[0]
os.remove(filepath+'\\manifest.json')
shutil.make_archive(os.path.dirname(filepath) + '\\' + storefilename, "zip", filepath)
shutil.rmtree(filepath)
print('finished')
