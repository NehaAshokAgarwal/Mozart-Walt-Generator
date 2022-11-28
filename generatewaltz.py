import stdarray
import stdrandom
import stdio

# Creating a 2D list 'minuet' of 11 by 16.
minuet = stdarray.create2D(11, 16, 0)
for i in range(11):
    for j in range(16):
        minuet[i][j] = stdio.readInt()
        # Reading the minuet measures from the standard input and changing the measure from
        # the initial value '0' in the table 'minuet' created

# Creating a 2D list 'trio' table of 6 by 16 .
trio = stdarray.create2D(6, 16, 0)
for i in range(6):
    for j in range(16):
        trio[i][j] = stdio.readInt()
        # Reading the trio measure from the standard input and changing the measure from
        #  the initial value '0' in the table 'trio' created

# Determining the minuet measure out of the 176 possible minuet measure by rolling a two fair dice.
# for a random sequence of 16 measure, accepting the random number from [1, 6] twice and adding
# them.
for j in range(16):
    measure1 = stdrandom.uniformInt(1, 7) + stdrandom.uniformInt(1, 7) - 2
    # Subtracting 2, as in the python, index starts from 0 in the list. While in the original
    # minuet table, the row index start from 2. Thus subtracting the 2  as to point out the
    # correct minuet measure.
    stdio.write(str(minuet[measure1][j]) + ' ')
    # Printing the standard output - minuet measure.

# Determining the trio measure out of the 96 possible trio measure rolling a two fair dice.
# For a random sequence of 16 measure, accepting the random number from [1, 6].
for j in range(16):
    measure2 = stdrandom.uniformInt(1, 7) - 1
    # Subtracting 1, as in python, index starts from 0 in the list. While in the original trio
    # table, index start from 1. Thus subtracting the 1 as to point out the correct trio measure.
    stdio.write(str(trio[measure2][j]) + ' ')
    # Printing the standard output - trio measure.
stdio.writeln()
