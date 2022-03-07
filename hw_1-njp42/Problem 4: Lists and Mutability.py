# Create a list, named yours, to store my favorite schools
yours = ["Yale", "MIT", "Berkeley"]
mine = ["Yale", "Clemson", "MIT"]
ours1 = mine + yours

# Create a 2nd list.
ours2 = []
ours2.append(mine)
ours2.append(yours)
# creating ours 2 in a different memory slot, and append is pointing to mine and yours
print(ours1)
print(ours2)
# Ours1 prints a concatenated new list of both the 'yours' list and the 'mine' list from memory, which is now stored
# in variable 'ours1,' maintaining the order of the previous lists. Ours2 is a blank list that leverages the append
# function to retrieve the 'yours' and 'mine' lists from memory. Due to this process, the two lists print separately,
# though order is maintained.

yours[1] = "USC"
print(ours1)
print(ours2)

# Every time a variable is created, it is stored in memory. In this situation, the lists created are stored in memory in
# a specific location - 'yours' and 'mine'. Yet, when a variable is changed, the previous memory location stays the
# same. Ours1 resulted in a concatenated list of 'yours' and 'mine' that was stored in a specific memory location. Thus,
# when changing the second term of 'yours' to USC, the print of ours1 remains the same given that it is leverages the
# same memory location from the previous run of the code. Given that ours2 leverages the append function, it points to
# the current location of ours1 and ours2, reflecting the change in the list 'yours.' Given that ours1 is stored in the
# previous location and ours2 is stored in a different location, we see the differences in the printed lists.
