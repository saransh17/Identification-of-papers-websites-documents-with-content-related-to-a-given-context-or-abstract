import urllib.request as libreq
from os import path
import os.path
# from bs4 import BeautifulSoup

from multiprocessing.pool import ThreadPool

ids = [
 '1909.12238',
'1909.12200',
'1909.12152',
'1909.12142',
'1909.12135',
'1909.12111',
'1909.12104',
'1909.12086',
'1909.12072',
'1909.12066',
'1909.12063',
'1909.12032',
'1909.11994',
'1909.11980',
'1909.11700',
'1909.11291',
'1909.12289',   
'1909.12286',
'1909.12272',
'1909.12271',
'1909.12243',
'1909.12229',
'1909.12224',
'1909.12220',
'1909.12153',
'1909.12116',
'1909.12114',
'1909.12077',
'1909.12038',
'1909.11974',
'1909.11968',
'1909.11942',
'1909.11912',
'1909.11890',
'1909.11851',
'1909.11840',
'1909.11830',
'1909.11766',
'1909.11765',
'1909.11766'
]

for i in ids:
    response = libreq.urlopen(f"https://arxiv.org/pdf/{i}.pdf")
    file = open(f"AbstractScrapedFiles1/{i}.pdf", 'wb')
    file.write(response.read())
    file.close()
    print("Completed")