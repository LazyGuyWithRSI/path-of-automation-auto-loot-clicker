
# Path of Automation: Loot Clicker!

Tired of clicking on those endless stacks of currency, vendor items, divination cards and more? Now you don't have to! This script will click on a piece of loot for you whenever you hit the hotkey!

[Video of the auto-looter in action](https://youtu.be/I2eDgYkn_vU)


### 
---
## Getting Started

   *This is WINDOWS ONLY currently*

- download the [latest release from the releases page](https://github.com/LazyGuyWithRSI/path-of-automation-auto-loot-clicker/releases)
- load up the provided loot filter ( or make your own, see lootfilter section below)
- run clicker.exe
- *NOTE: currently the game needs to be fullscreen or borderless window, as long as the game mostly fills your screen it will work*
- press the hotkey (default 'space bar') when loot drops to grab it!

---
## FAQ

   ### How does it work?
   - The script uses computer vision to find loot with a specific color, and moves the
   mouse to click on it.

   ### Is it safe?
   - yes. If you are concerned, just read the source.

   ### Does this violate Path of Exile's Terms of Service?
   - Only GGG knows. All I know is that marcos are allowed if they result in one action, which is true for this script. So most likely, yes. If anything, it will show if GGG is ever willing to implement an auto-loot feature.

---
### The Loot Filter

In order for the script to see loot to click on, it needs to be a color that stands out.
I have provided my own custom loot filter that turns many items to a stand out color, which happens to be pink.

---
### -- Advanced users --

   It is possible to use your own filter, but you need to make sure the things you want to
pick up are all colored the same, and with a stand out color. Then, edit the .ini to use
that color.

---
## Contributing