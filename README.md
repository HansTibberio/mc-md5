
# mc-md5

mc-md5 is a hashing algorithm similar to MD5, implemented in Minecraft. This project aims to provide an 8-bit hash implementation within the game, utilizing Minecraft blocks and redstone mechanics.

**Note:** The download link for the Minecraft world will be available soon.

## Installation

To use mc-md5, you must first install the `mcschematic` module. You can do this via pip:

```bash
pip install mcschematic
```
    
## Features

- 32-bit digest
- 128-bit internal block size
- 16 words of 8 bits each
- 4 Word buffer


## Usage/Examples

1. Download the project and make sure you have the world set up. Use Minecraft version 1.18.2.
2. In the `main.py` file, you'll find the variables to modify:
   - `folderPath`: This is where you should put the location where your schematic files are saved in Minecraft.
   - `fileName`: This is the name of the schematic file to be saved.
   - `messageToHash`: This is the message to be hashed.
3. Within the Minecraft world, position yourself correctly over the glass block and use the WorldEdit command `//paste -a` to paste the previously generated schematic file.

## Contributing

Contributions are always welcome! If you wish to improve this project, please submit a pull request.


## License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
