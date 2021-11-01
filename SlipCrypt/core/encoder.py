import string
import random

class scrambler:

    def scrambleVar(self):
        letters = string.ascii_letters
        self.scrambled = (''.join(random.choice(letters) for i in range(1, 15)))
        return self.scrambled