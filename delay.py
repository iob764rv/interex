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

stream = p.open(
    format    = PA_FORMAT,
    channels  = CHANNELS,
    rate      = RATE,
    input     = True,
    output    = True)

for i in range(0, TotalBlocks):

    # input frames
    input_string = stream.read(BLOCKSIZE, exception_on_overflow = False)   # BLOCKSIZE = number of frames read
     input_tuple = struct.unpack('h' * BLOCKSIZE, input_string)
    # Go through block
    for n in range(0, 1024):
        #chart
        output_block[n] = int( input_tuple[n] * 1 )
