import os
import requests
import bs4

name = input("Search :")
max_save = int(input("No. of Images you want to Download : "))
download = input("Enter File Name : ")

searchUrl = 'https://imgur.com/search'
queryUrl = searchUrl+'?q='+name

abs_output_path = os.path.abspath(download)
os.makedirs(abs_output_path, exist_ok=True)

res1 = requests.get(queryUrl)

try:
    res1.raise_for_status()

    imugurSoup = bs4.BeautifulSoup(res1.text, 'html.parser')
    images = imugurSoup.select('.image-list-link img')


    num_to_save = min(max_save, len(images))
    download_links = ['https:'+img.get('src') for img in images[:num_to_save]]


    for link in download_links:


        res2 = requests.get(link)

        try:
            res2.raise_for_status()


            imgFile = open(os.path.join(abs_output_path, os.path.basename(link)), 'wb')
            for chunk in res2.iter_content(100000):
                imgFile.write(chunk)
            imgFile.close()
        except Exception as exc:
                print('There was a problem: %s' % (exc))

except Exception as exc:
    print('There was a problem: %s' % (exc))
