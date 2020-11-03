import os, sys, re

f = open(sys.argv[1], 'r')

lines = f.readlines()
f.close()
tmp = {}
for line in lines:
    items = re.findall('avc: denied {(.*)}(.*)scontext=(.*) tcontext=(.*) tclass=(.*) permissive=(.*)',line)
    if len(items) > 0:
        if len(items[0]) == 6:
            tmp['allow '+items[0][2].split(':')[2]+' '+items[0][3].split(':')[2]+':'+items[0][4]+' {'+items[0][0]+'}'] = 0

for key in sorted(tmp.keys()):
    print key+';'
