def find_fibonacci(list1):    #defining the function
 list=[]           #creating an empty list to put the new list in it
 for i in range(len(list1)):
     sub=[]         ##creating an empty sub list
     if (list1[i-2]+list1[i-1]==list1[i]):     #checking if there are any 3 numbers in the list that creat fibonacci
         sub.append(list1[i-2])       #adding those found numbers and adding the to a sublist
         sub.append(list1[i-1])
         sub.append(list1[i])
         list.append(sub)            #putting the sublists in to one list
 return list

fibonacci=find_fibonacci([2, 8, 4, 6, 1, 7, 8, 4, 7, 9, 4, 13])
print(fibonacci)