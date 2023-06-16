#Think of something you can store in a list. for example a list of cities
#write a program that creates a list containing these items and then uses each function
#introduced in this chapter at least once
citys = ['harrisburg', 'philly', 'chester']
print(citys[1])
print(citys[1].title())
print(citys[2].title())
print(citys[-1])
message = "my first city to visit is " + citys[0].title()+ "."
print(message)

citys[0] = 'hollywood'
print(citys)


citys.append('bronx')


print(citys)
citys.append('queens')
citys.append('brooklyn')
citys.append('yonkers')
print(citys)


citys.insert(5, 'pittsburgh')
print(citys)


del citys[0]
print(citys)


citys.remove('philly')
print(citys)


crime_city = 'bronx'
print("\nThis city is "+  crime_city.title()+ "is not a safe city for me.")

citys.sort()
print(citys)
#stopped on page 48


citys.sort(reverse=True)
print(citys)
#page 49 printing in reverse order

citys.reverse()
print(citys)
# not working::len(citys)
# not workingprint(len)


print(citys[-1])