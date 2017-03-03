#!/usr/bin/env python
import base64
import cPickle as pickle
import random

def encrypt():
        key = []; #random integers that We created are kept here

        messageIn = raw_input("what is it that you want to encrypt?:");
        sliced = list(messageIn); #We now can manipulate the string by letter. we need this for encryption with random integers
        a = 0;  # variable is set so we can go through each letter and assign it a key in for loop
        manipulate = []; # We keep the numbers we get from ord() here

        prechr = [];
        crypted = [];
        newMsg = open("out.txt","wb+");
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
                while newNum > 255:
                        newNum = newNum - 255;
            prechr.append(newNum);
            a = a + 1;

        a = 0

        for number in prechr:  #now we convert each new number into an ASCII character
                newChar = chr(prechr[a]);
                crypted.append(newChar);
                a = a + 1;



        crypted = ''.join(crypted);
        newMsg.write(crypted);
        passwd = raw_input("Please set a password for your key file:");
        passCheck = raw_input("enter password again:");
        while passwd != passCheck:
                print ("two passwords entered do not match!");
                passwd = raw_input("Please set a password for your key file:");
                passCheck = raw_input("enter password again:");

        passwd = passwd;
        key = str(key);
        pickle.dump(key, open("key.p", "wb+"));
        encPass = base64.b64encode(passwd);
        passFile = open("passFile.txt", "wb+");
        passFile.write(encPass);
        newMsg.close();
        passFile.close();
        return

encrypt();
