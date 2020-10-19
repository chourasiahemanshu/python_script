import os

import urllib



from sys import platform

print(platform)
if platform == "linux" or platform == "linux2":
    print("Linux")
elif platform == "darwin":
    print("OS x")
elif platform == "win32" or platform == "Windows":
    print("windows")


def download(cookie, license, url, filename):
    print (url)
    print (filename)
    opener = urllib.build_opener()
    opener.addheaders.append((cookie, license))
    f = opener.open(url)
    with open(filename, 'wb+') as save:
        save.write(f.read())


cookie = 'Cookie'
license = 'oraclelicense=accept-securebackup-cookie'
url = 'http://download.oracle.com/otn-pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-windows-x64.exe'
filename = 'jdk-8u131-windows-x64.exe'
download(cookie, license, url, filename)