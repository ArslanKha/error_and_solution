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
###write a program which can tell us about the uppercase and lowercase in string
y=raw_input('Enter a string:')
lowercase="abcdefghijklmnopqrstuvwxyz"
uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
counter=0
count=0
for i in y:
    if i.uppercase:
        counter+=1
    elif i.lowercase:
        count+=1
print "UPPER CASE:",counter
print "LOWER CASE:",count
###Enter a string:Hello world!
###---------------------------------------------------------------------------
###AttributeError                            Traceback (most recent call last)
####<ipython-input-2-39d18d4d5914> in <module>()
#      5 count=0
#      6 for i in y:
#----> 7     if i.uppercase:
#     8         counter+=1
#      9     elif i.lowercase:

###AttributeError: 'str' object has no attribute 'uppercase'###
y=raw_input('Enter a string:')
lowercase="abcdefghijklmnopqrstuvwxyz"
uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
counter=0
count=0
for i in y:
    if i in uppercase:
        counter+=1
    elif i in lowercase:
        count+=1
print "UPPER CASE:",counter
print "LOWER CASE:",count
#now it change
#output==Enter a string:Hello world!
#UPPER CASE: 1
#LOWER CASE: 9
###write a program to tell about the a STAR astrogan
day = int(input("Input birthday: "))
month = raw_input("Input month of birth (e.g. march, july etc): ")
if month == 'december':
    astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
elif month == 'january':
    astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
elif month == 'february':
    astro_sign = 'Aquarius' if (day < 19) else 'pisces'
elif month == 'march':
    astro_sign = 'Pisces' if (day < 21) else 'aries'
elif month == 'april':
    astro_sign = 'Aries' if (day < 20) else 'taurus'
elif month == 'may':
    astro_sign = 'Taurus' if (day < 21) else 'gemini'
elif month == 'june':
    astro_sign = 'Gemini' if (day < 21) else 'cancer'
elif month == 'july':
    astro_sign = 'Cancer' if (day < 23) else 'leo'
elif month == 'august':
    astro_sign = 'Leo' if (day < 23) else 'virgo'
elif month == 'september':
    astro_sign = 'Virgo' if (day < 23) else 'libra'
elif month == 'october':
    astro_sign = 'Libra' if (day < 23) else 'scorpio'
elif month == 'november':
    astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
print "Your Astrological sign is :",astro_sign
###Input birthday: 11
###Input month of birth (e.g. march, july etc): april
###Your Astrological sign is : Aries
###write a program fibnoci from 0to50
def fibnew(n):
    a,b=0,1
    while b<n:
        print b
        a , b = b , a+b
#I face a problem to not change this program by a for loop
#I ever face like error (syntax error) wich i solve it or more following:
#Attribute error:face when apply some kind str in str so same operation on it
#Name error: some kind of variable or thing that not seen by interprator
#IOError:when there is file which was not exist
#IndentationError: expected an indented block
#unbounded local error:which we face when the variable call first by assign later in code























 