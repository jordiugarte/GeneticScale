from constants.default_settings import *
from constants.figures import *
from constants.notes import *


def metronome(duration, frequency):
    beat = 0
    while beat <= duration:
        FILE.addNote(TRACK, CHANNEL, A3, beat, SEMIFUSA, VOLUME)
        beat += frequency
    with open("output.mid", 'wb') as outf:
        FILE.writeFile(outf)

#   Duration in
metronome(30, 1)