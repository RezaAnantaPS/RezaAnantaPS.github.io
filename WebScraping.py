# Import package request dan BeautifulSoup 
import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime
#Requst ke website
page = requests.get("http://www.republika.co.id/")

#Extract konten menjadi objek BeautifulSoup
obj = BeautifulSoup(page.text,'html.parser');

#print ('Menampilkan objek html')
#print ('=======================')
#print (obj)

#print ('\nMenampilkan title browser dengan tag')
#print ('======================================')
#print (obj.title)

#print ('\nMenampilkan title browser tanpa tag')
#print ('=====================================')
#print (obj.title.text)

#print ('\nMenampilkan semua tag h2')
#print ('=====================================')
#print (obj.find_all('h2'))

#print ('\nMenampilkan semua teks h2')
#print ('=====================================')
#for headline in obj.find_all('h2'):
#    print (headline.text)

#print ('\nMenampilkan headline berdasarkan div class')
#print ('===========================================')
#print (obj.find_all('div',class_='bungkus_txt_headline_center'))

print ('\nMenampilkan semua teks headline')
print ('=================================')
for headline in obj.find_all('div',class_='conten1'):
    print (headline.find('h2').text)
    
print('\nMenampilkan kategori')
print('========================')
for publish in obj.find_all('div',class_='teaser_conten1_center'):
        print(publish.find('a').text)

print('\nMenampilkan waktu publish')
print('========================')
for publish in obj.find_all('div',class_='date'):
        print(publish.text)

print ('\nMenampilkan headline pada file text')
print ('=====================================')
divtag = obj.find_all('div',class_='conten1')
createnote = open('D:\scraping\headline.text','w')
for headline in divtag:
    createnote.write(headline.find('h2').text)
    for tag in divtag:
        tdtag = tag.find_all('div',class_='date')
        for dateP in tdtag:
            createnote.write(dateP.text)
            break
        break
    createnote.write('\n')
createnote.close()


# Deklarasi list kosong
data=[]
now = datetime.now()
# Lokasi file json
f=open('D:\scraping\scraping.json','w')
for publish in obj.find_all('div',class_='conten1'):
    # append headline ke variable data
    data.append({"Judul":publish.find('h2').text,"Kategori":publish.find('a').text,"Waktu_publish":publish.find('div',class_='date').text,"Waktu_scraping":now.strftime("%Y-%m-%d %H:%M:%S")})
# dump list dictionary menjadi json
jdumps = json.dumps(data, indent=1)
f.writelines(jdumps)
f.close()