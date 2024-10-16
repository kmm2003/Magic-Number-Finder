#!/usr/bin/env python3

import sys

def find_magic(file_path, magic_dict):
    with open(file_path, 'rb') as f:
        data = f.read()
    for fs_name, magics in magic_dict.items():
        for magic in magics:
            index = data.find(magic)
            if index != -1:
                print(f"{fs_name} file system found at offset {index} (0x{index:X})")
                break

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 find_fs.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    magic_numbers = {
        'SquashFS': [b'hsqs', b'sqsh'],
        'EXT': [b'\x53\xEF'],
        'NTFS': [b'\xEB\x52\x90\x4E\x54\x46\x53\x20'],
        'FAT32': [b'\x55\xAA'],
        'JFFS2': [b'\x19\x85'],
        'UBIFS': [b'UBI#'],
    }

    find_magic(file_path, magic_numbers)