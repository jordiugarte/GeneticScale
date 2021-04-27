import numpy as np

from random import randrange

from constants.default_settings import FILE, TRACK, VOLUME, CHANNEL
from constants.figures import *


def matrix_generation():
    random_input = np.empty([16, 36])
    for i in range(16):
        note = randrange(11, 47)
        # print(note)
        for j in range(36):
            if note == j:
                random_input[i][j] = 1
            elif note == 37:
                random_input[i][j] = 0
            else:
                random_input[i][j] = 0
    music_generation(random_input)


def music_generation(matrix):
    for beat in range(16):
        for i in range(36):
            if matrix[beat][i] == 1:
                note = range(36)[i] + 45
                FILE.addNote(TRACK, CHANNEL, note, beat, NEGRA, VOLUME)

    with open("output.mid", 'wb') as outf:
        FILE.writeFile(outf)


matrix_generation()
