#!/usr/bin/env python
import random

def encrypt():
        key = []; #random integers that We created are kept here

        messageIn = raw_input("what is it that you want to encrypt?:");
        sliced = list(messageIn); #We now can manipulate the string by letter. we need this for encryption with random integers
        a = 0 # variable is set so we can go through each letter and assign it a key in for loop
        manipulate = [] # We keep the numbers we get from ord() here
        prechr =[]

        for letter in sliced:
            newKeyEntry = random.randint(1,110);
            key.append(newKeyEntry);
            newData = ord(sliced[a]);
            manipulate.append(newData);
            a = a + 1;
        
        a = 0
        
        for data in manipulate :
            newNum = manipulate[a] + key[a]; # we add the numbers so we can convert them back using chr()
            if newNum > 255:
                print ("woah there the number is too long,brother!"); #placeholder. need to figure out how to properly get a new number between 1 and 255
            
            
           
        return

encrypt();
