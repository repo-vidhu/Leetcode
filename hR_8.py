# Given a time in -hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

# Example


# Return '12:01:00'.


# Return '00:01:00'.

# Function Description

# Complete the  function with the following parameter(s):

# : a time in  hour format
# Returns

# : the time in  hour format
# Input Format

# A single string  that represents a time in -hour clock format (i.e.:  or ).

# Constraints

# All input times are valid
# Sample Input 0

# 07:05:45PM
# Sample Output 0

# 19:05:45

import os
def timeConversion(s):
    k=s.split(sep=":")
    if "PM" in k[2] and k[0] !="12":
        k[0]=str(int(k[0])+12)
        value=str(k[0]+":"+k[1]+":"+k[2][0:2])
    elif "AM" in k[2] and k[0]=="12":
        k[0]="00"
        value=str(k[0]+":"+k[1]+":"+k[2][0:2])
    else:
        value=str(k[0]+":"+k[1]+":"+k[2][0:2])
    return value 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
