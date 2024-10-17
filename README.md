# Magic-Number-Finder

Magic-Number-Finder is a Python script that finds file system magic numbers to identify which file systems exist at specific offsets within a given file.

## Features
- Supports multiple file systems (SquashFS, EXT, NTFS, FAT32, JFFS2, UBIFS).
- Simple execution with Python 3.

## Usage
1. **Install Python 3**.
2. **Download the source code**:
   ```sh
   git clone https://github.com/yourusername/Magic-Number-Finder.git
   cd Magic-Number-Finder
   ```
3. **Run the script**:
   ```sh
   python3 find_fs.py <file_path>
   ```

Example output:
```
SquashFS file system found at offset 123456 (0x1E240)
```

## Supported File Systems
- SquashFS, EXT, NTFS, FAT32, JFFS2, UBIFS.
