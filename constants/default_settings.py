from midiutil.MidiFile import MIDIFile

FILE = MIDIFile(1)
TRACK = 0
TIME = 0
FILE.addTrackName(TRACK, TIME, "Sample Track")
FILE.addTempo(TRACK, TIME, 120)
CHANNEL = 0
VOLUME = 100