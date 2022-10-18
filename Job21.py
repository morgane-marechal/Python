numbers=[27,-17,-2,-251,1,-22,80,17,0,-1,77,8,717,23]

def mySort( numbers ):
    my_list=[] 
    for num in numbers:
        my_list.append(num)
    new_list=[]
    while my_list:
        minimum = my_list[0]  
        for x in my_list: 
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        my_list.remove(minimum)
    my_list = new_list
    return my_list  # <= return sans afficher
    
print(mySort(numbers))

def myDisplay( numbers ):
    print(numbers)

myDisplay(numbers)


