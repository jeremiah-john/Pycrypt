#!/usr/bin/env python
import os
import hashlib
import cPickle as pickle
import random

def encrypt():
        key = []; #random integers that We created are kept here

        messageIn = raw_input("what is it that you want to encrypt?:");
        sliced = list(messageIn); #We now can manipulate the string by letter. we need this for encryption with random integers
        a = 0;  # variable is set so we can go through each letter and assign it a key in for loop

        crypted = []; # where we will store the encrypted message so we can write to a text file
        
	outputFile = raw_input("what is the name of the file you want to write the encrypted message to?(file extensions also compatible(.txt,.torrent,etc)):"); #now the user can specify the name of the file to write the encrypted message to
	newMsg = open(outputFile,"wb+"); # the text file to write the encrypted message
        for letter in sliced:
            newKeyEntry = random.randint(1,110); # a random number to shift each letter in the string
            key.append(newKeyEntry); # appending each random key number to use for decryption later
            newData = ord(sliced[a]); # returns an ASCII value for a character
            newNum = newData + key[a]; # we shift the letter by a random key number
	    newLetter = chr(newNum); # we get the new character from the sum of the key number and the unencrypted letter's ASCII value
            crypted.append(newLetter); # we can do both ord() and chr() in one for loop, reducing the lines of code needed
	    a = a + 1;
	
	
        crypted = ''.join(crypted); # making sure there are no extra spaces in the final output
        newMsg.write(crypted); # we write the encrypted string to a text file
        passwd = raw_input("Please set a password for your key file:");
        passCheck = raw_input("enter password again:"); # simple password prompting (I kept running into a problem with getPass, so I just used raw_input)
        while passwd != passCheck: # asks for the password again if the two entries asking for the password do not match
                print ("two passwords entered do not match!"); 
                passwd = raw_input("Please set a password for your key file:");
                passCheck = raw_input("enter password again:");

	
        passwd = passwd;
        pickle.dump(key, open("key.p", "wb+")); # where we will store the key. This is a very insecure way to store keys and needs to change
        encPass = hashlib.sha256(passwd).hexdigest(); #  moved to SHA256 
        passFile = open("passFile.txt", "wb+");
        passFile.write(encPass);
        newMsg.close();
        passFile.close();
        return;

def decrypt():
	inputFile = raw_input("what is the name of the file you want to decrypt? Include filename extension:");
        message = open(inputFile, "rb");
        human = open("message.txt", "wb+");
        setPass = open("passFile.txt", "rb");
        passStat = os.stat('passFile.txt'); # we need to find out the size of the password file so that we can efficiently print the encoded password to a variable to decode
        passSize = passStat.st_size;
        passLine = setPass.readline(passSize);
        
        passCheck = raw_input("please enter your password to decrypt the file:");
	passHash = hashlib.sha256(passCheck).hexdigest();
        while passHash != passLine:
                print ("Password Incorrect!");
                passCheck = raw_input("please enter your password to decrypt the file");
        key = pickle.load( open("key.p", "rb"));

        messStat = os.stat(inputFile);
        messSize = messStat.st_size; # finds out size of message file
        fullMess = message.readline(messSize); # reads full message file (since the password lenght is up to user input, its better to have the program read up to the size of the file
        manipulateEnc = list(fullMess); # we can now iterate throught the encrypted string letter by letter

        i = 0;
        bigNums = [];
	readable = [];
        for letter in manipulateEnc:
                noombar = ord(manipulateEnc[i]);
		together = noombar - key[i]; # we shift the letter back to its unencrypted form and then we print it out
                if together < 0:
			together = together + 255;
		origText = chr(together);
		readable.append(origText);
                i = i + 1;


        unencrypted = ''.join(readable);
        human.write(unencrypted);
        message.close();
        human.close();
        setPass.close();
        return;

print ("Welcome to Pycrypt! The simple, light cipher!")

usage = raw_input("Would you like to encrypt, or decrypt?")
        
if usage == "encrypt":
        encrypt();
elif usage == "decrypt":
        decrypt();
                                        
