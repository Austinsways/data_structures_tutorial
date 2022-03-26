"""for this problem, imagine we are trying to track all the unique users who have visited our website. each user has a username  
and may visit the website multiple times, but we only want to know the unique users.
"""
day1 = ["bob", "jim", "jill", "jacob", "jhonson", "ava", "ryann"]
day2 = ["bob", "jim", "jill", "bob", "jim", "jill", "jared", "aly", "austin"]

#create a set for each day
set1 = set()
set2 = set()


#add each member from each list into there independent days
for user in day1:
    set1.add(user)
for user in day2:
    set2.add(user)

#print out the unique users in each day.
for person in set1:
    print(person)

for person in set2:
    print(person)


#we would like to know if bob visited on day1, write code to find bob and print "found bob!" if he did show up
if "bob" in set1:
    print("found bob!")
else:
    print("no bob );")

#we want to know what users visited on both days. using the intersection, show the users that  visited both days. 
both_days = set1 & set2
print(both_days)

#we want to see what user have visited during either day. use a union to merge the sets to show us all the users that have visited this week.
either_day = set1 | set2
print(either_day)
