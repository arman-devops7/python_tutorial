# strings is a datatype that stores a sequence of characters
str1="hello"
str2='hello'
str3='''hllo
world'''
str4="snns\nsps"
str5="snns\tsps"
print(str5)


# string operations
print(str1+str2)

print(len(str4))

# indexing
print(str1[3])

# slicing

str="hello_world"
print(str[1:4])
print(str[:4])
print(str[4:])
print(str[:])

# negative indexing (count from last)
print(str[-3:-1])


# returns true if string ends with substr
str="I am studying python"
print(str.endswith("on"))
print(str.endswith("nn"))

# capitalize first char(creates new string)
print(str.capitalize())
print(str)

# replace(creates new string)
print(str.replace("a","e"))
print(str)

# find the word in string (creates new string, returns the founded word/letter starting index,if nothing is found it will return -1)
print(str.find("am"))
print(str)

# count(creates new string,count the occurence of word/letter)
print(str.count("a"))
print(str)

# practice question

# 1) take user input and print its length

# name=input("Enter the sentence --> ")
# print(len(name))

# 2) find the occurence of $ in string
# dollarFind="$hvib $ftufa $"
# print(dollarFind.count("$"))