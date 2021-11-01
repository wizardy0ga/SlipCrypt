from .stub import stub
from .encryption import encryption
from .arguments import arguments
from .graphics import graphics

graphics = graphics()
encryption = encryption()
stub = stub()
arguments = arguments.args

class program:

    def SlipCrypt(self):
        print(graphics.banner)
        if arguments.backup:
            stub.createBackup(arguments.InputFile)
        print(f'[*] Staring Encrypting Process On {arguments.InputFile}')
        encryption.encryptFile(arguments.InputFile)
        stub.createNewStub(encryption.key,encryption.encryptedData,arguments.OutputFile)

        for i in range(arguments.Iterations):
            if arguments.verbose:
                print(f'[*] Starting Encryption Round {str(i)}')
            encryption.encryptFile(arguments.OutputFile)
            stub.createNewStub(encryption.key,encryption.encryptedData,arguments.OutputFile)
        print(f'[*] Encryption Finished. File Saved As {arguments.OutputFile}')