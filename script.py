name='Monthly Python'
description='sketch comedy group'
year=1969
setence=name+'is a'+description+'formed in'+year
##type error:can't convert 'int' object to str implicitly
##index error:index are out of range
greeting="HELLO WORLD!"
greeding[12] ##thats give error
word1 ='Good'##slicing
half1 = len(word1)//2
end1=word1[half1:]
word2 ='Evening'
half2 =len(word2)//2
end2=word2[half2:]
print(end1,end2)
#if or else conditional
num_knight=4

if num_knight<3:
	print ("Retreat!")
else:
	print("Truce?")