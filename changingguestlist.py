#changing guest list:  You just heard that one of your guest cant make the dinner,
# so you need to send out a new set of invintations. You'll have to think of someone else to invite.

#Start with your program from exercis 3-4. Add a print statement at
# the end of your program stating the name of the guest who cant make it

#Modify your list, replacing the name of the guest can't make 
#it with the name of the new person you are inviting.

#print a second set of invintation messages, one for each person who is still in your list.

deceased_family = ['birdy', 'cat','clifton','donald']
#print(deceased_family[0],'I would love to take you out to eat nanna.')
del deceased_family[0]
print(deceased_family)


print(deceased_family[1],'I would love to take you out to eat grandma. And we miss you.')
deceased_family.append('auntsarah')
print(deceased_family)
print(deceased_family[2],'I would love to take you out to eat grandpa and thank you for everything .')
print(deceased_family[0],"wont be joining us for dinner tonight because, god has other plans for her today")
(deceased_family.insert(0, 'UncleJerry'))
print(deceased_family[0], "will replace tonight ",deceased_family[1])
#print(deceased_family[3],'I would love to take you out to eat og miss you man.')
print(deceased_family[0],",",deceased_family[2],",",deceased_family[3],"",", your still going to dinner with us tonight")
