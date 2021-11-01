import argparse
from argparse import RawTextHelpFormatter
from .graphics import graphics
graphics = graphics()

class arguments:

    mainFileArgs = argparse.ArgumentParser(description=graphics.lockGraphic+'\n'+graphics.description,formatter_class=RawTextHelpFormatter)

    mainFileArgs.add_argument('InputFile',help='Input Python File For Encryption',type=str)
    mainFileArgs.add_argument('OutputFile',help='Name Of New File',type=str)
    mainFileArgs.add_argument('Iterations',help='Rounds Of Encryption You Would Like',type=int)

    subArguments = mainFileArgs.add_argument_group('Sub Arguments')
    subArguments.add_argument('-v','--verbose',action='store_true',help='Enable Verbose Output')
    subArguments.add_argument('-b','--backup',action='store_true',help='Create A Backup Of Your InputFile')

    args = mainFileArgs.parse_args()
