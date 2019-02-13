'''
Created on Feb 9, 2019

@author: S528358
'''
import math
def animate(speed, init):
    """
    Description:
            animate the movement of particles till they exit a linear chamber
            
    Required arguments:
            speed: number of positions each particle moves in one unit of time in either Right or Left direction
            init: initial position of the particle
            
    Optional arguments:
            NONE
            
    Return value:
            return list of strings where each string represents the position of particle at each time step
    """
    
    number_strings = count_strings_animate(speed,init)
    result = []
    #create list of strings possible
    temp_strings = [['.' for i in range(len(init))] for j in range(number_strings)]
    #update the strings in the list
    for i in range(len(init)):
        j = i
        if init[i] == 'L':
            for i in range(len(temp_strings)):
                if j >= 0:
                    temp_strings[i][j] = 'X'
                else:
                    break
                j = j - speed
        elif init[i] == 'R':
            for i in range(len(temp_strings)):
                if j < len(temp_strings[i]):
                    temp_strings[i][j] = 'X'
                else:
                    break
                j = j + speed

    for i in temp_strings:
        result.append(''.join(i))
    
    return result                
    
def count_strings_animate(speed,init):
    """
    Description:
            count all possible strings
            
    Required arguments:
            speed: number of positions each particle moves in one unit of time in either Right or Left direction
            init: initial position of the particle
            
    Optional arguments:
            NONE
            
    Return value:
            return count of animated strings
    
    """
    count_strings = 0
    
    for i in range(len(init)):
        if init[i] == 'R':
            count_strings = max(count_strings, math.ceil((len(init)-i)/speed))
        elif init[i] == 'L':
            count_strings = max(count_strings, math.ceil((i+1)/speed))
    return count_strings+1

#read input from file and write output to file
with open('C:/Users/s528358/eclipse-workspace/LI_CodeTest/output2.txt','w') as output:
    with open('C:/Users/s528358/eclipse-workspace/LI_CodeTest/input2.txt','r') as input:
        for line in input: 
            line_split = line.strip().split(',')            
            speed = int(line_split[0])
            init = line_split[1].strip()                      
            output.write("%s \n" %animate(speed, init))