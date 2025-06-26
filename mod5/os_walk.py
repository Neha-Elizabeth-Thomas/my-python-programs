import os

for dirpath, dirnames, filenames in os.walk("c:/Users/nelso/OneDrive/Desktop/Python"):
    print("Current directory:", dirpath)
    print("Subdirectories:", dirnames)
    print("Files:", filenames)
    print("------")
