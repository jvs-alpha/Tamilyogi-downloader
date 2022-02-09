# '''
# THis is the FUn project for downloading the movies from a website known as
# tamilyogi.cool this is a nice website without the SSL encryption for playing
# movie which means we can get the movie from the website which is more fun
# than have to stream the movie
# '''
# regex expression http:\/\/[0-9a-zA-Z.\/]+v\.mp4
# regex for M3U8 http:\/\/[0-9a-zA-Z.\/,]+master.m3u8
#!/usr/bin/env python3
import argparse
from bs4 import BeautifulSoup
import requests
import re
from fp.fp import FreeProxy

parser = argparse.ArgumentParser(description="This is TDownloader v1.0")
parser.add_argument("-v","--version",action="version",version="%(prog)s 1.0")
parser.add_argument("url",type=str,help="This is the url of the website")
parser.add_argument("filename",type=str,help="This is the file name to store it with")
argv = parser.parse_args()

url = argv.url

def get_proxies():
    return {"http": FreeProxy(rand=True).get()}
proxies = get_proxies()

response = requests.get(url, proxies=proxies)
parsed_data = BeautifulSoup(response.text,"html.parser")
iframes = parsed_data.find_all("iframe")
print(proxies)
print(parsed_data)
srcs = []
count = 0
for iframe in iframes:
    src = iframe.get("src")
    srcs.append(src)
    print("{} . {}".format(count,src))
    count += 1
choice = input("Enter the url to open: ")
response2 = requests.get(srcs[int(choice)], proxies=proxies)
parsed_data2 = BeautifulSoup(response2.text,"html.parser")
scripts = parsed_data2.find_all("script")
count = 0
for script in scripts:
    if "sources" in str(script):
        data = str(script)
        data = data.replace('"'," ")
        regex1 = re.compile(r"http:\/\/[0-9a-zA-Z.\/,]+master.m3u8")
        links = regex1.findall(data)
        print(links[0])
        r = requests.get(links[0], proxies=proxies, stream=True) 
        with open("{}.m3u8".format(argv.filename),"wb") as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
