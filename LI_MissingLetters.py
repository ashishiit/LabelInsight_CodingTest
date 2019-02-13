'''
Created on Feb 9, 2019

@author: S528358
'''
import string
import math
def getMissingLetters(input_string):
    """
    Description:
            Find missing letters from pangram sentences
    
    Required arguments:
            string containing a sentence
            
    Optional arguments:
            NONE
            
    Return value:
            return letters preventing a sentence from being a pangram
    """
    #only lower case alphabets allowed        
    letters_allowed = list(string.ascii_lowercase)
    #base condition when input string contains no letters
    if input_string == '':
        return ''.join(letters_allowed)
    result = ''
    letter_present = [False for i in range(26)]
    input_string = input_string.lower()
    #mark the presence of letters with respect to their index respectively
    for i in input_string:
        if i in letters_allowed:
            letter_present[ord(i)-ord('a')] = True
    
    for i in range(26):
        if letter_present[i] == False:
            result = result + chr(i+ord('a'))
            
    return result
#read input from file and write output to another file
with open('C:/Users/s528358/eclipse-workspace/LI_CodeTest/output1.txt','w') as output:
    with open('C:/Users/s528358/eclipse-workspace/LI_CodeTest/input1.txt','r') as input:
        for line in input:                        
            output.write(getMissingLetters(line)+'\n')