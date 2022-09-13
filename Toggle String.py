
'''
Problem:
You have been given a String S consisting of uppercase and lowercase English alphabets.
You need to change the case of each alphabet in this String. That is, all the uppercase letters
should be converted to lowercase and all the lowercase letters should be converted to uppercase.
You need to then print the resultant String to output.

'''
#### MY CODE

name = input() 
def toggle(name):
    join='' 
    for i in range(len(name)):
        if(name[i].islower() == True):
            l2u=name[i].upper()
            join+=l2u
        else:
            u2l=name[i].lower()
            join+=u2l
    return join


print(toggle(name))

