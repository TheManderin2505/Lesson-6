StudentDetails = ("Alex", 14, "model planes")
print(type(StudentDetails))

address = (220, "brikfeild appartment", "bangalore","karnataka", 546000)

for i in address:
    print(i)

houseno, appartmeent, city,state,pin = address
print()
print("House number :" + houseno)
print("Appartment name :" + appartmeent)
print("City:" + city)
print("state :" + state)
print("Pin :" + pin)
mypets = "dog","cat","parrot"
print(type)(mypets)

mytuple = ("mouse", (1,2,3),[10,45,60])

print(mytuple[0],[3])

#Tupel is imune to changes/ it can't be changed or alterd

mytuple[2],[2] = 450
print(mytuple)

mytuple1 = ("Apples","banana")
mytuple2 = ("orange", "cherry")
mytuple3 = mytuple1 + mytuple2
print(mytuple3)

my_tuple = ("apple","banna","cherry")
print(len(my_tuple))
print(my_tuple * 3)

tuple1 = ('c','o','d','i','n','g')
print(tuple1[0:3])
print(tuple1[2:6])
print(tuple1[:4])
print(tuple1[2:])
print(tuple1[:])
