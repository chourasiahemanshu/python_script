import os

from sys import platform

print(platform)
if platform == "linux" or platform == "linux2":
    print("Linux")
elif platform == "darwin":
    print("OS x")
elif platform == "win32" or platform == "Windows":
    print("windows")

