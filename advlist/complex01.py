#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - simple list"""

def main():
    # create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list1
    print(list1)
    
    #display "artista_eos" from the list
    print(list1[1])

    # create a new list 
    list2 = ["juniper"]

    #extend list1 by list2
    list1.extend(list2)

    #display list1, which contains juniper from list 2
    print(list1)

    # create list3
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]
    
    # append list1 by list3
    list1.append(list3)

    #display list1, which conatins list3  
    print(list1)
    
    # display the list of IP addresses
    print(list1[4])
    
    # display the firt item in the list - first IP address
    print(list1[4][0])
    
    # creat new list
    animal = ["Fox", "Fly", "Ant", "Bee", "Cod", "Cat", "Dog", "Yak", "Cow", "Hen", "Koi","Hog", "Jay", "Kit"]
    
    #print the animal list
    print(' '.join(animal))

main()

