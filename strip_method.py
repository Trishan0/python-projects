#------Using strip method for various strings------


#NORMAL USAGE 01 - Removing whitespaces on the string
word = "    Hello World   "
print(word)
print("1. Removed all Whitespaces\n"+word.strip())

#Removing white spaces on the left
print("2. Removed all left side Whitespaces\n"+word.lstrip())

#Removing white spaces on the Right
print("3. Removed all Right side Whitespaces\n"+word.rstrip())



#NORMAL USAGE 02 - Removingthe knowing symbol from the string
word = "----Hello World----"
print("\n"+word)
print("1. Removed all symbols\n"+word.strip('-'))

#Removing symbols on the left
print("2. Removed all symbols on the left side\n"+word.lstrip('-'))

#Removing symbols on the Right
print("3. Removed all symbols on the Right side\n"+word.rstrip('-'))



#NORMAL USAGE 03 - If first whitespace and then one type symbols exist
word = " *****Hello World**** "
print("\n"+word)
print("1. Removed all Whitespace and symbols\n"+word.strip(' *'))

#Removing whitespace and symbols on the left
print("2. Removed all left side whitespace and symbols\n"+word.lstrip(' *'))

#Removing whitespace and symbols on the Right
print("3. Removed all Right side Whitespace and symbols\n"+word.rstrip(' *'))



#If you don't know what are symbols in your string , Note - Left and right should be the same symbols in same order


word = " ^@%!#&(Hello World^@%!#&( "
s = [] #create a tuple for the store the symbols
for i in word:
    if not i.isalpha(): #checking the char is a english letter or not
        s.append(i) #if not a letter add it to tuple named 's'
    elif i.isalpha():
        break 

letters = ''.join(s)   #convert the created tuple into a string
print("\n\n1. Removed all\n"+word.strip(letters)) 
print("2. Removed all Left side\n"+word.lstrip(letters))
print("3. Removed all Right side\n"+word.rstrip(letters)) #use strip method and remove them
