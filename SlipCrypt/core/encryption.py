from cryptography.fernet import Fernet

class encryption:

    def makeNewKey(self):
        key = Fernet.generate_key()
        return key

    def encryptFile(self,fileInput):

        self.key = self.makeNewKey()
        crypter = Fernet(self.key)

        with open(fileInput,'rb') as fileToEncrypt:
            fileData = fileToEncrypt.read()
            self.encryptedData = crypter.encrypt(fileData)
            fileToEncrypt.close()

        return self.encryptedData, self.key
