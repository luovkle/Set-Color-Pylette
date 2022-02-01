# Set Color Pylette

## What it is

**set_color_pylette** is a script that aims to automate the process of setting a color palette from a terminal to an image.

## Usage

### Example 1

Base image

![base_image_1](examples/example_1.png)

solarized_dark (bright colors)

```sh
chmod +x set_color_pylette.py
./set_color_pylette example_1.png -t solarized_dark -B -o example_1_bright_colors.png
```

![solarized_dark](examples/example_1_bright_colors.png)

### Example 2

Base image

![base_image_2](examples/example_2.png)

gruvbox_dark (normal and bright colors)

```sh
chmod +x set_color_pylette.py
./set_color_pylette example_2.png -t gruvbox_dark -b -o example_2_normal_and_bright_colors.png
```

![gruvbox_dark](examples/example_2_normal_and_bright_colors.png)

## Included themes

* afterglow
* argonaut
* ayu_dark
* ayu_mirage
* base16_default_dark
* blood_moon
* breeze
* campbell
* cobalt_2
* darkside
* darktooth
* dracula
* github
* gnome_dark
* gnome_light
* gruvbox_dark
* gruvbox_light
* hybrid
* hyper
* iceberg_dark
* iceberg_light
* ir_black
* iterm_default
* jellybeans
* kitty
* material_theme
* molokai
* monokai
* monokai_pro
* monokai_soda
* new_moon
* night_owl
* nightfly
* nord
* nova
* oceanic_next
* oxide
* paper_colors
* pear
* pencil_dark
* pencil_light
* pop_os
* seabird
* seoul256
* seoul256_light
* snazzy
* solarized_dark
* solarized_light
* sourcerer
* spacemacs_light
* substrata
* taerminal
* tango
* tangoish
* tender
* terminal_app
* terminal_app_basic
* tomorrow_night
* tomorrow_night_bright
* ubuntu
* visual_studio_code_terminal
* wombat
* xterm
* zenburn

## Requirements

**set_color_pylette** uses **imagemagick** software to get the job done. It is for this reason that **imagemagick** must be installed on the system.

Archlinux

```sh
sudo pacman -S imagemagick
```

Debian 11

```sh
sudo apt install imagemagick
```
