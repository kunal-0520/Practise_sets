# write a program to crate a dict of hindi words with values as their english translation. provide user with an option to look it up .

mydict = {
    "pankha" : 'fan',
    "kurchi" : 'chair',
    "hero" : 'shaktiman',
    "lahsun" : 'ginger'
}

print('options are :',mydict.keys())

a = input("enter the choice of your hindi word : " )
print("the meaning of your word is: ",mydict.get(a)) 
#these line will not throw an error if the key is not present it shows non because of get function.

