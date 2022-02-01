#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
import os
import subprocess
from typing import Dict, List


class Settings:
    ALLOWED_FORMATS = ["png", "jpeg", "jpg", "svg"]
    TEMP_FILE = ".theme_temp.png"
    THEMES_DIRECTORY = "themes"
    THEMES_SUFFIX = ".json"


class ImageDoesNotExist(Exception):
    """The inserted image does not exist"""


class ColorPaletteDoesNotExist(Exception):
    """Color palette does not exist"""


class InvalidFileFormat(Exception):
    """Invalid file format"""


class ThemesNotFound(Exception):
    """The themes directory was not found"""


class ColorPaletteNotRemoved(Exception):
    """Color palette could not be removed"""


class OutputFileAlreadyExists(Exception):
    """Output file already exists"""


def get_args() -> Dict[str, str]:
    parser = argparse.ArgumentParser()
    parser.add_argument("image", type=str, help="Base image")
    parser.add_argument("-t", "--theme", type=str, required=True, help="Color palette")
    parser.add_argument(
        "-b",
        "--bright-colors",
        action="store_true",
        default=False,
        help="Use bright colors",
    ),
    parser.add_argument(
        "-B",
        "--only-bright-colors",
        action="store_true",
        default=False,
        help="Only use bright colors",
    )
    parser.add_argument("-o", "--output", type=str, required=True, help="Output file")
    args = parser.parse_args()
    return vars(args)


def verify_existence_of_files(current_image: str, new_image: str) -> None:
    if not os.path.isfile(current_image):
        raise ImageDoesNotExist
    if os.path.isfile(new_image):
        raise OutputFileAlreadyExists


def check_file_format(
    current_image: str, new_image: str, allowed_formats: List[str]
) -> None:
    if current_image.split(".")[-1] not in allowed_formats:
        raise InvalidFileFormat
    if new_image.split(".")[-1] not in allowed_formats:
        raise InvalidFileFormat


def get_available_themes() -> List[str]:
    if os.path.isdir("themes"):
        files = os.listdir("themes")
        themes: List[str] = []
        for file in files:
            if file.endswith(".json"):
                themes.append(file.removesuffix(".json"))
        if len(themes) == 0:
            raise ThemesNotFound
        return themes
    else:
        raise ThemesNotFound


def create_color_palette(theme: Dict[str, str], file_output: str) -> None:
    count = 0
    for color in theme.values():
        if count == 0:
            subprocess.call(f"convert xc:{color} {file_output}".split())
        else:
            subprocess.call(
                f"convert {file_output} xc:{color} +append {file_output}".split()
            )
        count += 1


def create_new_image(current_image: str, color_palette: str, file_output: str) -> None:
    subprocess.call(
        f"convert {current_image} -dither None -remap {color_palette} {file_output}".split()
    )


def delete_color_palette(color_palette: str) -> None:
    if os.path.isfile(color_palette):
        os.remove(color_palette)
    else:
        raise ColorPaletteNotRemoved


def main() -> None:
    settings = Settings()

    args = get_args()
    current_image = args["image"]
    new_image = args["output"]

    # Verify that the entered files exist
    verify_existence_of_files(current_image, new_image)

    # Verify that the formats of the files entered are correct
    check_file_format(current_image, new_image, settings.ALLOWED_FORMATS)

    themes = get_available_themes()

    # Show available themes if the user selects the wrong one
    if args.get("theme") not in themes:
        print("Available themes:")
        for theme in themes:
            print(theme)
        exit(0)

    # Obtaining colors
    with open(
        f"{settings.THEMES_DIRECTORY}/{args.get('theme')}.json", "r"
    ) as theme_file:
        content = json.loads(theme_file.read())
        if args.get("only_bright_colors"):
            colors = content.get("bright")
        elif args.get("bright_colors"):
            colors = content.get("normal")
            bright_colors = content.get("bright")
            for color in bright_colors.keys():
                colors[f"B{color}"] = bright_colors.get(color)
        else:
            colors = content.get("normal")

    # Create the color palette (temp file)
    create_color_palette(colors, settings.TEMP_FILE)

    # Create the new image
    create_new_image(current_image, settings.TEMP_FILE, new_image)

    # Delete color palette (temp file)
    delete_color_palette(settings.TEMP_FILE)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("Exiting...")
        exit(0)
