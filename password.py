import random 

kecil = "abcdefghijklmnopqrstuvwxyz"
besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
simbol = "!@#$%^&*():;'<>,/?`~[]\|}{"

string = kecil + besar + simbol
length = 16
password = "".join (random.sample(string, length))

print("password : " + password)