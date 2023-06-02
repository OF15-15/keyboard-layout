# Create personalized keyboard layout with Karabiner Elements

## Description
I use the [adnw](http://adnw.de/) keyboard layout, a variation of neo. On my Mac, I encountered the issue that the option key was used as the level-3 modifier. Since at least some applications use option-key commands and I still wanted the ability to use them, I decided to use another key as level-3 mod. Also, my level-4 mod wasn't always working as expected. First, I tried to achieve these goals with [Ukelele](https://software.sil.org/ukelele/), but MacOS wasn't distinguishing between right and left shift, command, option and control keys, so I was unable to just remap my level-3 mod to one of these. After some trying and failing I decided to do (almost) everything with carabiner. This program currently just takes the keys defined in keys.json and saves them as a complex modification for carabiner, but it is intended to grow over time.

## How to use
First of all, you need to have [Karabiner Elements](https://karabiner-elements.pqrs.org/) installed. Then you run the python skript to save a json file in the `/Users/[user_name]/.config/karabiner/assets/complex_modifications/` folder. After this, you can add the complex modification in the Karabiner-Elements settings and add the following simple modifications:
- `caps_lock` => `fn` (layer 2 - symbols)
- `right_shift` => `left_shift` (layer 1 - capital letters)
- ``grave_accent_and_tilde (`)`` => `right_shift` (layer 4 - cursor block & key pad)
- `backslash (\\)` => `right_shift` (layer 4 - cursor block & key pad)

You can redefine your keys or add other keys in the `keys.json` file. It is a list of mappings each key. Every list item is a dictionary consisting of the key that needs to be mapped, a list of modifiers, a list of resulting keys and a list of lists of resulting modifiers. You can get the keycode for the `from_key` field from the Karabiner-EventViewer. The result can change if you press this original key together with one of the modifiers mentioned in `from_modifiers`. In `to_keys` and `to_modifiers`, you list the keystrokes that shall result if you press the original key and the one of the modifiers.