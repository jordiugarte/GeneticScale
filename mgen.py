import numpy as np

from random import randrange
from random import randint
from random import uniform

from midiutil import MIDIFile

from constants.figures import *


def matrix_generation():
    # Initialization for new empty song section
    # Might update lenght depending on how "fast" this is played
    compas = np.zeros([16, 36])

    # Random input for the first iteration
    # Might swap this: random input and then see what it made so it knows where to go, look at a song constantly, look at a song first and then see where it goes, or look at a song and look where it is to see where it goes
    random_input = np.empty([16, 36])
    for i in range(16):
        note = randrange(37)
        print(note)
        for j in range(36):
            if note == j:
                random_input[i][j] = 1
            elif note == 37:
                random_input[i][j] = 0
            else:
                random_input[i][j] = 0

    # print(random_input)

    # PROCESS START THIS SHOULD BE IN A LOOP

    # FIRST HIDDEN LAYER
    # Initialize weights
    Weights_A = np.random.uniform(-1, 1, (18, 36))
    Weights_B = np.random.rand(18, 18)
    Weights_Out = np.random.rand(37, 18)
    # print(Weights_A)

    # INITIALIZE BIAS
    Bias_A = np.array([[0],
                       [0],
                       [0],
                       [0],
                       [0],
                       [0],
                       [0],
                       [0],
                       [0],
                       [0],
                       [0],
                       [0],
                       [0],
                       [0],
                       [0],
                       [0],
                       [0],
                       [0], ])  # np.random.rand(18,1)
    Bias_B = np.array([[0],
                       [0],
                       [0],
                       [0],
                       [0],
                       [0],
                       [0],
                       [0],
                       [0],
                       [0],
                       [0],
                       [0],
                       [0],
                       [0],
                       [0],
                       [0],
                       [0],
                       [0], ])
    Bias_Out = np.array([[0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0],
                         [0], ])
    # --------------------------------------------------------------------------------------------

    generations = 5
    Parent_A_WA = np.zeros([18, 36])
    Parent_A_WB = np.zeros([18, 18])
    Parent_A_WC = np.zeros([37, 18])
    Parent_B_WA = np.zeros([18, 36])
    Parent_B_WB = np.zeros([18, 18])
    Parent_B_WC = np.zeros([37, 18])
    for g in range(generations):
        Output_midi = np.zeros([36, 1])
        Storage_wA = np.empty([5, 18, 36])
        Storage_wB = np.empty([5, 18, 18])
        Storage_wC = np.empty([5, 37, 18])
        # GENETIC STEP Inclusdes Crossing and Randomization
        Best_Parent_Bias = 6  # Another parameter we can change, from 0 to 9
        Randomization_Bias = 3
        for l in range(5):
            if g == 0:
                Weights_A = np.random.uniform(-1, 1, (18, 36))
                Weights_B = np.random.uniform(-1, 1, (18, 18))
                Weights_Out = np.random.uniform(-1, 1, (37, 18))
            else:
                # Cross A
                for i in range(18):
                    for j in range(36):
                        if randint(0, 10) < Best_Parent_Bias:
                            Weights_A[i][j] = Parent_B_WA[i][j]
                        else:
                            Weights_A[i][j] = Parent_A_WA[i][j]
                        if randint(0, 10) < Randomization_Bias:
                            Weights_A[i][j] = uniform(-1, 1)
                # Cross B
                for i in range(18):
                    for j in range(18):
                        if randint(0, 10) < Best_Parent_Bias:
                            Weights_B[i][j] = Parent_B_WB[i][j]
                        else:
                            Weights_B[i][j] = Parent_A_WB[i][j]
                        if randint(0, 10) < Randomization_Bias:
                            Weights_B[i][j] = uniform(-1, 1)
                # Cross C
                for i in range(37):
                    for j in range(18):
                        if randint(0, 10) < Best_Parent_Bias:
                            Weights_Out[i][j] = Parent_B_WC[i][j]
                        else:
                            Weights_Out[i][j] = Parent_A_WC[i][j]
                        if randint(0, 10) < Randomization_Bias:
                            Weights_Out[i][j] = uniform(-1, 1)

            # print("These are the thoughts of gen ",l)
            #  print(Weights_A)
            #  print(Weights_B)
            #  print(Weights_Out)

            Storage_wA[l] = Weights_A
            Storage_wB[l] = Weights_B
            Storage_wC[l] = Weights_Out

            for k in range(16):
                # FIRST HIDDEN LAYER PROCESSING
                Hidden_A = np.zeros([18, 1])
                # print("this is hidden A")
                # print(Hidden_A)

                for i in range(18):
                    for j in range(36):
                        if k == 0:
                            Hidden_A[i][0] += Weights_A[i][j] * random_input[0][j]
                        else:
                            Hidden_A[i][0] += Weights_A[i][j] * Output_midi[i][0]
                    # this should eventually be in a loop, depending on the situation chose, ergo if this reads the entire random input
                    # print(i)
                    # print(j)
                    # print("Weights")
                    # print(Weights_A[0][j])
                    # print("random")
                    # print(random_input[0][j])
                    # print("Result")
                    # print(Hidden_A[i][0])
                    Hidden_A[i][0] += Bias_A[i][0]
                    # Hidden_A[i][0]=1/(1 + np.exp(-(Hidden_A[i][0]))) #using sigmoid rn, subject to change
                    Hidden_A[i][0] = np.tanh(Hidden_A[i][0])
                # print(Hidden_A)

                # SECOND HIDDEN LAYER PROCESSING
                Hidden_B = np.zeros([18, 1])
                for i in range(18):
                    for j in range(18):
                        Hidden_B[i][0] += Weights_B[i][j] * Hidden_A[j][0]
                    Hidden_B[i][0] += Bias_B[i][0]
                    # Hidden_B[i][0]=1/(1 + np.exp(-(Hidden_B[i][0])))
                    # Hidden_B[i][0]=np.maximum(0,Hidden_B[i][0])
                    Hidden_B[i][0] = np.tanh(Hidden_B[i][0])
                # print(Hidden_B)

                # OUTPUT LAYER PROCESSING
                Output_Layer = np.zeros([37, 1])
                max_val = 0
                max_val_index = -1
                for i in range(37):
                    for j in range(18):
                        Output_Layer[i][0] += Weights_Out[i][j] * Hidden_B[j][0]
                    Output_Layer[i][0] += Bias_Out[i][0]
                    # Output_Layer[i][0] = 1/(1 + np.exp(-(Output_Layer[i][0])))
                    Output_Layer[i][0] = np.maximum(0, Output_Layer[i][0])
                    # Output_Layer[i][0] = np.tanh(Output_Layer[i][0])
                    if Output_Layer[i][0] > max_val:
                        max_val = Output_Layer[i][0]
                        max_val_index = i
                # print(Output_Layer)

                # CREATE COMPASS REGION
                Output_midi = np.zeros([36, 1])
                # print(max_val)
                # print(max_val_index)
                for i in range(36):
                    if i == max_val_index:
                        Output_midi[i][0] = 1
                # print(Output_midi)

                # SAVE TO SONG
                for i in range(36):
                    compas[k][i] = Output_midi[i][0]
            music_generation(compas, l)
            print("song ", l + 1)
            print(compas)

        Best_Song = input("Index of the best song: ")
        Second_Best = input("Index of the second best song: ")

        Best_Song = int(Best_Song)
        Second_Best = int(Second_Best)

        Parent_A_WA = Storage_wA[Best_Song]
        Parent_A_WB = Storage_wB[Best_Song]
        Parent_A_WC = Storage_wC[Best_Song]
        Parent_B_WA = Storage_wA[Best_Song]
        Parent_B_WB = Storage_wB[Best_Song]
        Parent_B_WC = Storage_wC[Best_Song]
        # Needs genetic step
        # needs randomization step


def music_generation(matrix, index):
    FILE = MIDIFile(1)
    TRACK = 0
    TIME = 0
    FILE.addTrackName(TRACK, TIME, "Sample Track")
    FILE.addTempo(TRACK, TIME, 120)
    CHANNEL = 0
    VOLUME = 100
    for beat in range(16):
        for i in range(36):
            if matrix[beat][i] == 1:
                note = range(36)[i] + 45
                FILE.addNote(TRACK, CHANNEL, note, beat, NEGRA, VOLUME)

    with open("output" + str(index) + ".mid", 'wb') as outf:
        FILE.writeFile(outf)


matrix_generation()
