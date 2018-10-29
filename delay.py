#pyaudio input

import pyaudio
import struct

WIDTH     = 2         # bytes
CHANNELS  = 2         #  channels
RATE      = 8000     # Sampling
BLOCKSIZE = 1024     
DURATION  = 10    


TotalBlocks = int( DURATION * RATE / BLOCKSIZE )
output_block = [0 for i in range(0, BLOCKSIZE)]

output_block = [0 for i in range(0, BLOCKSIZE)]
SECONDS = 10
blocksrate = int(RATE / BLOCKSIZE * SECONDS)

p = pyaudio.PyAudio()
PA_FORMAT = p.get_format_from_width(WIDTH)

