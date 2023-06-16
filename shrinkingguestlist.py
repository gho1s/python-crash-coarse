# shrinking guest list you just found out your new dinner table wont arrive in time for the dinner, 
# and you only have space for two guest
# start with program more guest 3-6 
#add a new line that prints a message say that you can only invite two people for dinner
#use a pop() to remove guest from each list one at a time until only
#two names remain in your list. Each time you pop() a name from the list, print a message to that 
#that person letting them know your sorry you cant invite them to dinner.
#Print a message to each of the to people still on your list, letting them know they're still invited
# Use del to remove the last two names frrom the list, so you have an empty list. Print your list to make sure you
#actually have an empty list at the end of your program

#starting right here and havt to edit a few things to make it work
print("I can only invite two people to dinner")

deceased_family = ['birdy', 'cat','clifton','donald','sarah','jerry']
d1 =  deceased_family.pop(0)
print("Hello im sorry but there is not enough space at our table for all of you thanks for understanding "  + d1)

d2 =  deceased_family.pop(0)
print("Hello im sorry but there is not enough space at our table for all of you thanks for understanding "  + d2)


d3 =  deceased_family.pop(0)
print("Hello im sorry but there is not enough space at our table for all of you thanks for understanding "  + d3)


d4 =  deceased_family.pop(0)
print("Hello im sorry but there is not enough space at our table for all of you thanks for understanding "  + d4)

print("Sarah you are still invited to dinner")

print("Jerry you are still invited to dinner")



del deceased_family[0]
del deceased_family[0]
print(deceased_family)




#print(deceased_family)







#print(deceased_family[0],'I would love to take you out to eat nanna.')

#print(deceased_family[1],'I would love to take you out to eat grandma. And we miss you.')

#print(deceased_family[2],'I would love to take you out to eat grandpa and thank you for everything .')

#print(deceased_family[3],'I would love to take you out to eat og miss you man.')

#deceased_family.insert(0, "orange")

#deceased_family.insert(3, "red")

#deceased_family.insert(6, "violet")

#print(deceased_family[0],"We found a bigger table to invite more people to dinner")

#print(deceased_family[1],"We found a bigger table to invite more people to dinner")

#print(deceased_family[2],"We found a bigger table to invite more people to dinner")

#print(deceased_family[3],"We found a bigger table to invite more people to dinner")

#print(deceased_family[4],"We found a bigger table to invite more people to dinner")

#print(deceased_family[5],"We found a bigger table to invite more people to dinner")

#print(deceased_family[6],"We found a bigger table to invite more people to dinner")


#print(deceased_family)

