my_name ='Tammy'
my_age= 28 # keep my secret
my_height = 162 # cm
my_weight = 53 # kg
my_eyes = 'black'
my_teeth = 'ivory white'
my_hair = 'black'
my_country= 'China'

print "Please tell me something about %s." %my_name
print "Tammy is %d cm tall," %my_height
print "and %d kg, a slim girl." %my_weight
print "She has %s eyes and %s color hair." %(my_eyes, my_hair)
print "She is a happy girl, and right now she lives in %s." %my_country

# this line is trick, try to get it exactly right 
print "if I add %d, %d, and %d I get %d." %(my_age, my_height, my_weight, my_age+my_height+my_weight)


x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary, do_not)

print x
print y 

print "I said: %r." % x
print "I also said:'%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" #%r is for debugging

print joke_evaluation % hilarious 

w = "This is the left side of ..."
e = "a string with a right side."

print w + e

 # exercise 3.1
print "Mary has a little lamb."
print "Its fleece was white as %s." % 'snow'
print "Any everywhere that Mary went."
print "." *10 #what'd that do ?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens 
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12


 # exercise 3.2
print "Mary has a little lamb."
print "Its fleece was white as %s." % 'snow'
print "Any everywhere that Mary went."  # no comma in the end

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"


print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

# exercise 4.1 
formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one", "two", "three","four")
print formatter % (True, False, True, False)
print formatter % ( "I had this thing.", "That you could type up right.", "But it didn't sing.", "So I said goodnight.")
print formatter % ("formatter", "formatter", "formatter", "formatter")
print formatter % (formatter, formatter, formatter, formatter)

