from midiutil.MidiFile import MIDIFile

from notes import *
mf = MIDIFile(1)
track = 0
time = 0
mf.addTrackName(track, time, "Sample Track")
mf.addTempo(track, time, 120)
channel = 0
volume = 100

pitch = G5
time = 0
duration = 1
mf.addNote(track, channel, pitch, time, duration, volume)

pitch = Bb5
time = 2
duration = 1
mf.addNote(track, channel, pitch, time, duration, volume)

pitch = C5
time = 4
duration = 1
mf.addNote(track, channel, pitch, time, duration, volume)

with open("output.mid", 'wb') as outf:
    mf.writeFile(outf)