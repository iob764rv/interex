#pyaudio input

import pyaudio
import struct

WIDTH     = 2         # bytes
CHANNELS  = 2         #  channels
RATE      = 8000     # Sampling
BLOCKSIZE = 1024     
DURATION  = 10    
