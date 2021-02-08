# Assignment of Python for LetsUpgrade Python Course

##### Question 1 
# Experiment with Five list's Built in Function

students = ["Rohit Shetty","Ram Mishra", "Pari Yadav","Shubam Mishra", "Kanta Bhai", "Urvi Kanade"]
print(students)

students.append("Raakhi Singh")   #1 Adds a value to the end of the List
print(students)

students.pop()
students.pop()
students.pop()                    #2 Removes a value from the last from a list
print(students)

students.remove("Pari Yadav")     #3 Removes a specific given value from a list
print(students)

students.sort()                   #4 Sorts the list in Alphabatic order
print(students)

students.clear()                 #5 Clears the list items without deleting the List
print(students)


##### Question 2 
# Experiment with Five Dictionary's Built in Function

st_aloysius_school = {
    "Student_1": "Raju Shashtri",
    "Age": 14,
    "Std": "7th",
    "Result": "Pass",
    "Attendance": "91%",
    "Loc": "Mumbai"
    }  # this is a Dict which has a Key value Pair

print(st_aloysius_school)

a = st_aloysius_school.get("Result")    #1 To get a specific Value we use get() Function
print(a)

b = st_aloysius_school.keys()           #2 key() helps us to get all the keys from a dictionary
print(b)

c = st_aloysius_school.pop("Loc")       #3 Like List, Dict also have a pop function but in Dict's Pop we have to give a value to get it removed
print(c)

d = st_aloysius_school.values()         #4 values() helps us to get all the Values from a dictionary
print(d)

del st_aloysius_school["Age"]           #5 del helps us delete a key:value from a dictionary it can also delete whole dict too






