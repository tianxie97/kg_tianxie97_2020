class Solution(object):
    def mapping(self, s1, s2):
        #Define the total number of the characters.
        Num_of_Char = 256
        #If these two strings don't have the same length, we cannot do a one-to-one mapping.
        if len(s1) != len(s2):
            return False
        #For characters in s1, initialize the mapping status to -1.
        mapped = [-1] * Num_of_Char

        for i in range(len(s1)):
            if mapped[ord(s1[i])] == -1:
                #Map this character to s2[i]
                mapped[ord(s1[i])] = s2[i]
            #If s1[i] has been mapped before and it should be mapped to the same character in s2.
            # If not, return false.
            elif mapped[ord(s1[i])] != s2[i]:
                return False
        return True