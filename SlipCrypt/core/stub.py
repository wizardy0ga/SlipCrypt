from .encoder import scrambler

scrambler = scrambler()

class stub:

    def createBackup(self,inputFile):
        with open(inputFile,'r') as backup:
            backupData = backup.read()
            backup.close()

        with open(f"{inputFile}.backup",'w') as backupfile:
            backupfile.write(backupData)
            backup.close()
        print(f'[*] Backup File Saved As {inputFile}.backup')

    def createNewStub(self,key,encryptedData,inputFile):

        algoKeyScrambled = scrambler.scrambleVar()
        fernetScrambled = scrambler.scrambleVar()
        decrypterScrambled = scrambler.scrambleVar()
        cryptedDataScrambled = scrambler.scrambleVar()
        decryptedData = scrambler.scrambleVar()

        with open(inputFile,'w') as output:
            output.write(f"""
from cryptography.fernet import Fernet as {fernetScrambled}
{algoKeyScrambled} = {key}
{decrypterScrambled} = {fernetScrambled}({algoKeyScrambled})
{cryptedDataScrambled} = {encryptedData}
{decryptedData} = {decrypterScrambled}.decrypt({cryptedDataScrambled})
exec({decryptedData})
""")
