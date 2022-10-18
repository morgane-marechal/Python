def multiple_numb( *number ):
    my_list=[] 
    for num in number:
        my_list.append(num)
    my_list.sort()  
    print("Voici tous les nombres de la liste par ordre croissant: ",my_list)
    

multiple_numb( 100,17,0,-1,4,5,8,54,23 )