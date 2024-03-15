
from implementation import MCMD5
from schematic import generateSchematic

folderPath = "C:/Users/user/AppData/Roaming/.minecraft/config/worldedit/schematics"
fileName = "test"

messageToHash = 'Hello World'

def main():
    hashedMessage = MCMD5(messageToHash.encode())
    schematicFile = generateSchematic(fileName, folderPath)
    print('"%s" = %s' % (messageToHash, hashedMessage))
    print('Schematic file saved with name: "%s" in folder: %s' % (fileName, folderPath))

if __name__ == '__main__':
	main()