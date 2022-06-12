# Audio files formats
# .mp3
# .flac
# .wav
import wave 

# Audio signal parameter
# - number of channels
# - sample width 
# - framerate/sample-rate : 44,100 Hz
# - number of frames
# - values of a frame 

obj = wave.open("patrick.wav", "rb")

print("Number of channels", obj)
