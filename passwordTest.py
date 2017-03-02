import base64
import cPickle as pickle
setPass = raw_input("enter your desired password")
checkPass = raw_input("re-enter password")
while setPass != checkPass:
    print "the password entries do not match!";
    setPass = raw_input("enter your desired password");
    checkPass = raw_input("re-enter password");
    if setPass == checkPass:
        break;
passwd = checkPass;
encPass = base64.b64encode(passwd)
key = {9, 6, 5, 0}

pickle.dump(key, open( "key.p", "wb" ))
passCheck = raw_input("Please enter your password:")
entPass = base64.b64encode(passCheck)
while entPass != encPass:
    print("Wrong Password!");
    passCheck = raw_input("Please enter your password:");
    entPass = base64.b64encode(passwd);
    if entPass == encPass:
        break;
print ("Login Successful")
