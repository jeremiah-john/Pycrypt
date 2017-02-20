#!/usr/bin/env python
import random

def encrypt():
        key = [];

        messageIn = raw_input("what is it that you want to encrypt?:");
        sliced = list(messageIn);

        for letter in sliced:
            newKeyEntry = random.randint(1,110);
            key.append(newKeyEntry);
            print chr(sliced[letter]);
           
        return

encrypt();
