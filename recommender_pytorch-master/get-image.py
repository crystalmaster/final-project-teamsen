import re
import requests
from bs4 import BeautifulSoup

#site = 'https://www.sendo.vn/tim-kiem?q=dien%20thoai'

def get_img_usr(site):
    response = requests.get(site)

    soup = BeautifulSoup(response.text, 'html.parser')

    img_tags = soup.find_all('img')

    return img_tags[1]['src']
# response = requests.get(site)

# soup = BeautifulSoup(response.text, 'html.parser')

# #img_tags = soup.find_all('img')

# for x in soup.find_all('subCategories'):
#     print(x)
#     print('-------------------------------------------------')
# #print(img_tags[1]['src'])
def get_url(url):

    try:
        return get_img_usr(url)
    except:
        return 'https://cdn.itviec.com/employers/sendo-vn/logo/social/LdDQX1mXSSRgfoH9DRCfxU3t/sendo-vn-logo.jpg'