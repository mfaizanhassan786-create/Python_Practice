#Some are the Prctice of the Topic Lists and the tuple:

#Write a program to ask the user to enter the name of 3 movies and then store them in a list.
#Program 1:
movies = []
m1 = input("Enter movie one:")
m2 = input("Enter movie Two:")
m3 = input("Enter movie Three:")
movies.append(m1)
movies.append(m2)
movies.append(m3)
print(movies)


#Palindrome:

# Program 2:
list = [1, 2, 1]
print(list)
list_copy= list.copy()
print(list_copy)
list_copy.reverse()
print(list)
if(list == list_copy):
    print("Palindrome")
else:
    print("Not a Palindrome")

#Program 3
list1 = [2,3,2]
list_copy = list1.copy()
print(list1)
list_copy.reverse()
print(list_copy)
if(list1 == list_copy):
    print("Palindrome")
else:
    print("Not a Palindrome")

grade = ("A","B","C","D","F")
print(grade)
print(grade.count("A"))
print(grade.index("A"))

#For the to Print the Grades in the Ascending Order:
#Program 4:
grade = ["A","C","B","F","D"]
print(grade)
print(grade.count("A"))
print(grade.index("A"))
grade.sort()
print(grade)

#For the to Print the Grades in the Descending Order:
#Program 5:
grade = ["A","C","B","F","D"]
print(grade)
print(grade.count("A"))
print(grade.index("A"))
grade.sort(reverse=True)
print(grade)