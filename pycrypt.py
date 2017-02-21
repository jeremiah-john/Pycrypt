#!/usr/bin/env python
import random

def encrypt():
        key = [];

        messageIn = raw_input("what is it that you want to encrypt?:");
        sliced = list(messageIn);
        a = 0

        for letter in sliced:
            newKeyEntry = random.randint(1,110);
            key.append(newKeyEntry);
            print ord(sliced[a]);
            a = a + 1;
           
        return

encrypt();
