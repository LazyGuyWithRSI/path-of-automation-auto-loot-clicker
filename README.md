
# Path of Automation: Loot Clicker

Tired of clicking on those endless stacks of currency, vendor items, divination cards and more? Now you don't have to! This script will click on a piece of loot for you whenever you hit the hotkey!

[Video of the auto-looter in action](https://youtu.be/I2eDgYkn_vU)

No sketchy memory access. It just uses screen caps, then moves and clicks the mouse.

### 
---
## Getting Started

   *This is WINDOWS ONLY currently*
   
1. download the [latest release](https://github.com/LazyGuyWithRSI/path-of-automation-auto-loot-clicker/releases)
2. load up the provided loot filter ( or make your own, see lootfilter section below)

   [tutorial on installing a loot filter in PoE](https://filterblast.xyz/how-to-install-and-use-poe-item-filter.html)
3. run poe-auto-loot.exe

 *NOTE: currently the game needs to be fullscreen or borderless window, as long as the game mostly fills your screen it will work*
 
4. press the hotkey (default 'space bar') when loot drops to grab it!

**Important**: The script uses your mouse, so you cannot be pressing a mouse button when you press the hotkey. If you are clicking, the script can't click for you!

---
## FAQ

   ### How does it work?
   - The script uses computer vision to find loot with a specific color, and moves the
   mouse to click on it.

   ### Is it safe?
   - Yes. If you are concerned, just read the source.

   ### Does this violate Path of Exile's Terms of Service?
   - Yes. It technically is a form of automation, which is not allowed. Can they detect it? Maybe. This was mostly an academic pursuit.
      ### *I am not responsible if use of this script results in action from GGG*

---
### The Loot Filter

In order for the script to see loot to click on, it needs to be a color that stands out.
I have provided my own custom loot filter that turns many items to a stand out color, which happens to be pink.

---
### -- Advanced users --

   It is possible to use your own filter, but you need to make sure the things you want to
pick up are all colored the same, and that the color stands out. Then, edit the .ini to use
that color.

---

## Built With
- pyinstaller - for distribution

## Licensing

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Contributing

I haven't thought this far. Will update with guidelines in the future.
