# Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Using the information given below, determine the number of apples and oranges that land on Sam's house.

# In the diagram below:

# The red region denotes the house, where  is the start point, and  is the endpoint. The apple tree is to the left of the house, and the orange tree is to its right.
# Assume the trees are located on a single point, where the apple tree is at point , and the orange tree is at point .
# When a fruit falls from its tree, it lands  units of distance from its tree of origin along the -axis. *A negative value of  means the fruit fell  units to the tree's left, and a positive value of  means it falls  units to the tree's right. *
# Apple and orange(2).png

# Given the value of  for  apples and  oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range )?

# For example, Sam's house is between  and . The apple tree is located at  and the orange at . There are  apples and  oranges. Apples are thrown  units distance from , and  units distance. Adding each apple distance to the position of the tree, they land at . Oranges land at . One apple and two oranges land in the inclusive range  so we print

# 1
# 2
# Function Description

# Complete the countApplesAndOranges function in the editor below. It should print the number of apples and oranges that land on Sam's house, each on a separate line.

# countApplesAndOranges has the following parameter(s):

# s: integer, starting point of Sam's house location.
# t: integer, ending location of Sam's house location.
# a: integer, location of the Apple tree.
# b: integer, location of the Orange tree.
# apples: integer array, distances at which each apple falls from the tree.
# oranges: integer array, distances at which each orange falls from the tree.
# Input Format

# The first line contains two space-separated integers denoting the respective values of  and .
# The second line contains two space-separated integers denoting the respective values of  and .
# The third line contains two space-separated integers denoting the respective values of  and .
# The fourth line contains  space-separated integers denoting the respective distances that each apple falls from point .
# The fifth line contains  space-separated integers denoting the respective distances that each orange falls from point .

# Constraints

# Output Format

# Print two integers on two different lines:

# The first integer: the number of apples that fall on Sam's house.
# The second integer: the number of oranges that fall on Sam's house.
# Sample Input 0

# 7 11
# 5 15
# 3 2
# -2 2 1
# 5 -6
# Sample Output 0

# 1
# 1
# Explanation 0

# The first apple falls at position .
# The second apple falls at position .
# The third apple falls at position .
# The first orange falls at position .
# The second orange falls at position .
# Only one fruit (the second apple) falls within the region between  and , so we print  as our first line of output.
# Only the second orange falls within the region between  and , so we print  as our second line of output.

def countApplesAndOranges(s, t, a, b, apples, oranges):
    v1=apples
    ca=0
    cb=0
    v2=oranges
    for i in range(len(v1)):
        v1[i]+=a
        if v1[i] in range(s,t+1):
            ca+=1
    print(ca)
    for i in range(len(v2)):
        v2[i]+=b
        if v2[i] in range(s,t+1):
            cb+=1
    print(cb)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
