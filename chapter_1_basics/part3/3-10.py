counties = ['iceland', 'new zeland', 'norway', 'finland', 'canada']
print(counties[0].title())
print(counties[1].title())
print(counties[2].title())
print(counties[3].title())
print(counties[4].title())
print(counties)
counties.append('germany')
print(counties[-1].title())
counties.insert(2, 'france')
print(counties[1].title())
del counties[4]
popped_country = counties.pop(1)
print(popped_country)
print(counties)
counties.remove('germany')
print(counties)
counties.sort()
print(counties)
counties.sort(reverse=True)
print(counties)
sorted(counties)
print(counties)
counties.reverse()
print(counties)
print(len(counties))
