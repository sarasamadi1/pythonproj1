def permutation(a,b):
    if len(a) != len(b):                                       #returning false if the lenght of the lists are not equal
        return False
    n = len(a)
    count = 0
    differ=0
    for i in range(n):
        for j in range(n):
            if b[j] == a[i]:                                   #if there are elements in both lists which are equal to eachother
                count += 1                                     #we add one number to count
            else:
                differ+=1                                      #if not add one number to differ
    if count==n:
        print( a ,"and",b ,"are permutations")
    else:
        print(differ)

def main():
    list1 = []                                                  #making empty lists: list1 and list2
    n1 = int(input("Enter number of elements : "))              #asking the user about the lenght of the lists
    for i in range(0, n1):
        ele1 = int(input("Enter the list element :"))           #inserting all elements user enters to each list
        list1.append(ele1)
    list2 = []
    n2 = int(input("Enter number of elements : "))
    for i in range(0, n2):
        ele2 = int(input("Enter the list element :"))
        list2.append(ele2)
    print(permutation(list1,list2))                             #passing both lists to the function
main()