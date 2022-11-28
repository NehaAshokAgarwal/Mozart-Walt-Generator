import stdaudio
import stdio
import sys

waltz = stdio.readAllInts()
# If number of measure of waltz  is not 32, then exit the program with the given message.
if len(waltz) != 32:
    sys.exit(" A waltz must contain exactly 32 measures.")

# If the minuet measure is not from [1, 176], then  exit the program with the given message.
for m in waltz[0:16]:
    if m < 1 or m > 176:
        sys.exit("A minuet measure must be from [1, 176]")

# If the trio measure is not from [1, 96], then exit the program with the given message.
for t in waltz[16:32]:
    if t < 1 or t > 96:
        sys.exit(" A trio measure must be from [1, 96]")

# Reading the minuet measure of waltz from the standard input and playing the file.
for m in waltz[0:16]:
    file = 'data/M' + str(m)
    stdaudio.playFile(file)

# Reading the trio measure of the waltz from the standard input and playing the file.
for t in waltz[16:32]:
    file = 'data/T' + str(t)
    stdaudio.playFile(file)
