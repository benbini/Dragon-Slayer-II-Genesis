#!/usr/bin/bash

ROM=$1

if [ ! -d font ]
then
    mkdir font
fi

python3 font.py unpack "$ROM" "font/font_kanji_14_14.bin" 0xf4fbe 0x108eea
python3 font.py unpack "$ROM" "font/font_main_8_14.bin" 0x108eea 0x109d42
python3 font.py unpack "$ROM" "font/font_ascii_8_8.bin" 0x109d42 0x109fc6
python3 font.py unpack "$ROM" "font/font_ascii_8_12.bin" 0x109fc6 0x10a35a
python3 font.py unpack "$ROM" "font/font_kanji_12_12.bin" 0x10a35a 0x10b380
