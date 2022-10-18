def multiple_numb( *number ):
    my_list=[] 
    for num in number:
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
        
   
    print("Voici la liste des nombre par ordre croissant: ",my_list)

multiple_numb( 22,-2,-25631,1,-22,100,17,0,-1,40,8,5,23 )