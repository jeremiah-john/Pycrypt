#!/usr/bin/env python
import os
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
            newNum = newData + key[a];
	    newLetter = chr(newNum);
            crypted.append(newLetter); # we can do both ord() and chr() in one for loop, reducing the lines of code needed
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
        pickle.dump(key, open("key.p", "wb+"));
        encPass = base64.b64encode(passwd);
        passFile = open("passFile.txt", "wb+");
        passFile.write(encPass);
        newMsg.close();
        passFile.close();
        return;

def decrypt():
        message = open("out.txt", "rb");
        human = open("message.txt", "wb+");
        setPass = open("passFile.txt", "rb");
        passStat = os.stat('passFile.txt');
        passSize = passStat.st_size;
        passLine = setPass.readline(passSize);
        passWord = base64.b64decode(passLine);
        
        passCheck = raw_input("please enter your password to decrypt the file:");

        while passCheck != passWord:
                print ("Password Incorrect!");
                passCheck = raw_input("please enter your password to decrypt the file");
        key = pickle.load( open("key.p", "rb"));

        messStat = os.stat('out.txt');
        messSize = messStat.st_size;
        fullMess = message.readline(messSize);
        manipulateEnc = list(fullMess);

        i = 0;
        bigNums = [];
        for letter in manipulateEnc:
                noombar = ord(manipulateEnc[i]);
                bigNums.append(noombar);
                i = i + 1;

        i = 0;
        numsPreChr = [];
        for data in bigNums:
                together = bigNums[i] - key[i];
                if together < 0:
                        together = together + 225;
                numsPreChr.append(together);
                i = i + 1;
        i = 0;
        readable = [];
        for num in numsPreChr:
                origText = chr(numsPreChr[i]);
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
                                        
