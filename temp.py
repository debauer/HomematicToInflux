from hm import Roomlist

import os

# List all files in a directory using os.listdir
basepath = 'testdata'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        print(entry)

xml = open('testdata/roomlist.xml', "r", encoding="ISO-8859-1")
rl = Roomlist(xml.read())
xml.close()
rl.print_all_rooms()
