import librosa

def tempo(input_file):
    x, sr = librosa.load(input_file)
    tempo=librosa.beat.beat_track(x, sr=sr)[0]
    print(tempo)
    return tempo


def temp_retrieve(path):
    line_number = 0
    line_number_t = 0
    print("path to be retrieved: ")
    print(path)
    with open('C:/Users/AnyOneElse/GP_POP/Batot/music/music_paths.txt') as f:
        for line in f:
            line_number += 1
            try:
                if(path in line):
                    break  
            except:
                return 90
    with open('C:/Users/AnyOneElse/GP_POP/Batot/music/tempos.txt','r') as f:
        for line in f:
            line_number_t += 1
            if(line_number_t == line_number):
                return line


    return 90