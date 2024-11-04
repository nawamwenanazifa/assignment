#list are mutable or data stored in the list can always be updated or changed
#lists are array like structured
student_name = ["Sandra", "Patricia","Phiona", "Anita"] # it is storing strings
student_marks = [80,56,78,90] # it is storing integers
data = ["Nazifa", 69, "Jinja"] # mixed types
print(student_name)

#Accessing items in the list
#indexes(postive indexing)
print(student_name[0]) #first name
print(student_name[1]) #second name
print(student_name[2]) # third name

#Negative indexing
print(student_name[-3]) #first name
print(student_name[-2]) #second name
print(student_name[-1]) # third name

#appending means adding more items to the list
student_name.append("Michelle")
print(student_name)

#inserting
student_name.insert(2,"Phicratte")
print(student_name)


#HOME WORK
#Question 1
#print the list containg names of patricia, Faith, Phionah and Anitah.
student_list = ["Patricia", "Faith", "Phionah", "Anitah"]
print(f"\nThe student list: {student_list}\t")

#2. Add Marsha to the 4th position
student_list.insert(3, "Masha")
print(f"\nAdding Masha to the 4th postion in student list:{student_list}\t")

#3. Update the name Phiona to Aladinah
student_list[student_list.index('Phionah')] = "Aladinah"
print(f"\nUpdating Phionah to Aladinah in the student list:{student_list}\t")

#4.Display the length of the student list.
print(f"\nThe length of the the student list is:{len(student_list)}\t")

#5.print all the student names using a 4 loop
for student in student_list:
    student_list = ["Patricia", "Faith", "Phionah", "Anitah"]
    print(f"\n{student}\t")

#.6Calculate the total marks for the student marks variable.s
total_marks = sum(student_marks)
print(total_marks)