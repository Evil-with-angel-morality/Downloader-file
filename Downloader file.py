import requests

def download(link,name):
    file = requests.get(link)
    if file.status_code != 200:
        return False
    f = open(name,"wb")
    f.write(file.content)
    f.close()
    return True

def downloadlist(link,name):
    file = requests.get(link)
    if file.status_code != 200:
        return False
    f = open(name,"wb")
    f.write(file.content)
    f.close()
    return True

def gg (linkt,namet):
    file = requests.get(linkt)
    if file.status_code != 200:
        return False
    f = open(namet,"wb")
    f.write(file.content)
    f.close()
    return True


li = input("  Danlowd list or one ?")
lis = li.lower()

if lis == ("one"):
    link = input("Link : ")
    name = input("Name : ")
    result = download(link,name)
    if result:
        print ("Ok !")
    else:
        print("Error !")


if lis == ("list"):
    link = input("Link 1 : ")
    name = input("Name 1 : ")
    linkt = input("Link 2 : ")
    namet = input("Name 2 : ")
    result = downloadlist(link,name)
    result = gg(linkt,namet)