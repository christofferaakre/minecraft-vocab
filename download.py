#!/usr/bin/env python

# author: negosaki

# this script downloads images for all the minecraft
# blocks and items listed on https://n5v.net/block-item-id/,
# and saves them with the filename {block_or_item_name}.jpg
# (the japanese block/item names)

import requests
import urllib
import time
from bs4 import BeautifulSoup
root_url = 'https://n5v.net/block-item-id/'

soup = BeautifulSoup(urllib.request.urlopen(root_url).read())

img_tags = soup.select('img.fl-l')
print(f'number of items: {len(img_tags)}')

items = [{'text': img['alt'], 'image_url': root_url + img['src']} for img in img_tags]

save_folder = 'images/'
failed_count = 0

start = time.process_time()
for i, item in enumerate(items):
    if i % 25 == 0:
        print(f'{i}/{len(items)}')
        
    text = item['text']
    image_url = item['image_url']
    try:
        urllib.request.urlretrieve(image_url, save_folder + text + '.jpg')
    except Exception as e:
        failed_count += 1
        print(f'failed to retrieve image at {image_url}, failed {failed_count} times out of {i + 1} so far')

end = time.process_time()
print(f'ran in {end - start} seconds')
