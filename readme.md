# minecraft-vocab
This repository contains the scripts used to generate an Anki deck
containing Japanese vocab cards for every block/item in Minecraft, using
the ID list here: https://n5v.net/block-item-id/

The deck can be found here: https://ankiweb.net/shared/info/1256711678 <br>
**If you just want the deck, there is no need to run the scripts, and you
don't need to read any further**

The scripts were written using a `Python 3.7.9` environment.

A lot of the cards are for unobtainable items etc. or are otherwise not
very useful, so I would really appreciate it if someone would be willing to
help me filter through the approximately 1200 cards to decide which 
cards should be deleted. If you can help, DM me on Discord (`negosaki#4243`)

## External requirements
* Anki 2.1.35 installed with a profile named `test` and a deck
called `maikura`
* The Migaku Japanese Vocabulary note type, which can be acquired from this
  deck: https://ankiweb.net/shared/info/1256711678

## Setup
1. Clone respository
2. `pip install -r requirements.txt` to install dependencies
3. Create a new directory called `images`
4. Run `download.py`
5. Run `make_cards.py`, making sure either that Anki is closed, or that
the currently selected profile is not `test`
6. The created cards should now be in your `maikura` deck
7. From here, I used the Migaku Japanese Anki add on
   (https://ankiweb.net/shared/info/278530045)
and the Migaku Dictionary add on (https://ankiweb.net/shared/info/1655992655)
to generate pitch accent colouring, furigana, dictionary definitions and audio
recordings for words that have that available (not many due to the specific
names of most items), etc. Note that these add ons should not be required to
view the cards if you just download the deck from Ankiweb, as it works on my
phone on AnkiDroid.
