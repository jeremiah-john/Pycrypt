import cPickle as pickle
setPass = raw_input("enter your desired password")
checkPass = raw_input("re-enter password")
while setPass != checkPass:
    print "the password entries do not match!";
    setPass = raw_input("enter your desired password");
    checkPass = raw_input("re-enter password");
key = {9, 6, 5, 0}

pickle.dump(key, open( "key.p", "wb" ))
