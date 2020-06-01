'''
THis is the FUn project for downloading the movies from a website known as
tamilyogi.cool this is a nice website without the SSL encryption for playing
movie which means we can get the movie from the website which is more fun
than have to stream the movie
'''
#!/usr/bin/python3
import argparse
from bs4 import BeautifulSoup
import requests
import sys

parser = argparse.ArgumentParser(description="This is TDownloader v1.0")
parser.add_argument("-v","--version",action="version",version="%(prog)s 1.0")
parser.add_argument("url",type=str,help="This is the url of the website")
argv = parser.parse_args()

url = argv.url

response = requests.get(url)
parsed_data = BeautifulSoup(response.text,"html.parser")
iframes = parsed_data.find_all("iframe")
srcs = []
count = 0
for iframe in iframes:
    src = iframe.get("src")
    srcs.append(src)
    print("{} . {}".format(count,src))
    count += 1
choice = input("Enter the url to open: ")
response2 = requests.get(srcs[int(choice)])
parsed_data2 = BeautifulSoup(response2.text,"html.parser")
scripts = parsed_data2.find_all("script")
try:
    for script in scripts:
        if "jwplayer" in script.text:
            print(script.text)
except:
    print("test")
