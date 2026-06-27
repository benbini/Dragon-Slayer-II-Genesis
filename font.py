#!/usr/bin/env python3

import argparse
from pathlib import Path

def dump_font(rom_path,font_path,start,end):
    with open(rom_path,"rb") as rom, open(font_path,"wb") as font:
        rom.seek(start)
        tile_types  = int.from_bytes(rom.read(1))
        tile_width  = int.from_bytes(rom.read(1))
        tile_height = int.from_bytes(rom.read(1))
        tile_bytes  = int.from_bytes(rom.read(1))
        while rom.tell() < end:
            bitmaps = row = col = 0
            for bitmaps in  range(tile_types+1):
                tile_map = [ [b"\x00",b"\x00"] for _ in range(16) ]

                for row in range(tile_height):
                    for col in range(0,tile_width,8):
                        tile_map[row][col//8] = rom.read(1)
                if tile_height > 0:
                    if tile_width > 0:
                        for row in range(8):
                            font.write(tile_map[row][0])
                    if tile_width > 8:
                        for row in range(8):
                            font.write(tile_map[row][1])
                
                if tile_height > 8:
                    if tile_width > 0:
                        for row in range(8):                            
                            font.write(tile_map[row+8][0])
                            
                    if tile_width > 8:
                        for row in range(8):
                            font.write(tile_map[row+8][1])

parser = argparse.ArgumentParser()
sub    = parser.add_subparsers(dest="command",required=True)
dump   = sub.add_parser("unpack",help="unpack font data")
dump.add_argument("path_to_rom",type=Path)
dump.add_argument("path_to_dumped_font",type=Path)
dump.add_argument("start_offset",type=lambda value: int(value,16),help="specify as 0x... hex")
dump.add_argument("end_offset",type=lambda value: int(value,16),help="specify as 0x... hex")

args = parser.parse_args()
dump_font(args.path_to_rom,args.path_to_dumped_font,args.start_offset,args.end_offset)

