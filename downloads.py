import os

print(os.getcwd())

download_path = '/home/rory/Downloads'
os.chdir(download_path)
print(os.getcwd())

print(os.listdir(os.getcwd()))
for filename in os.listdir():
    print("Deleting file: " + filename)
    os.remove(filename)

print("Done")
