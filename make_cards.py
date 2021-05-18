#!/usr/bin/env python

# author: negosaki

# this script makes anki cards for every
# image file listed in the images diretory. Note you must
# run the download.py script located in the same directory as this
# script first to download the images, or this script will not work
# You must also have a profile in Anki called 'test',
# and the Migaku Japanese Vocabulary note type, which you can
# get from this deck at Ankiweb: https://ankiweb.net/shared/info/1256711678

# Note also that you can not run this script while you have your
# 'test' profile open in Anki, as the Anki API needs to access
# that profile  

import sys, os
import anki
from anki.storage import Collection
import time

filenames = list(filter(lambda filename: '.jpg' in filename, os.listdir('images')))

PROFILE_HOME = os.path.expanduser('~/AppData/Roaming/Anki2/test')
cpath = os.path.join(PROFILE_HOME, 'collection.anki2')

# opening collection
collection = Collection(cpath, log=True)


# getting right note type
model_basic = collection.models.byName('Migaku Japanese Vocabulary')

# finding the right deck
deck = collection.decks.byName('maikura')

# switching to right note type
deck['mid'] = model_basic['id']


start = time.process_time()
# making a new note
for i, filename in enumerate(filenames):
    word = filename.replace('.jpg', '')
    image_HTML = fr'<img src="{filename}">'
   
    # create a new note
    note = collection.newNote()

    # put the note in the right deck
    note.model()['did'] = deck['id']

    # set the word field on the card
    note.fields[0] = word
    
    # set the image field on the card
    note.fields[4] = image_HTML

    # set tags on card
    tags = 'minecraft'
    note.tags = collection.tags.canonify(collection.tags.split(tags))
    model = note.model()
    model['tags'] = note.tags

    # sacing model
    collection.models.save(model)

    # adding note to collection
    collection.addNote(note)
    if i % 100 == 0:
        print(f'added card for word {word}, {i+1}/{len(filenames)}')

##
collection.save()
end = time.process_time()
print(f'ran in {end - start} seconds')
