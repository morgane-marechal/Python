def multiple_numb( *number ):
    my_list=[] 
    even_list=[]
    for num in number:
        if num % 2 == 0:
            even_list.append(num)    
            my_list.append(num)
        else:
            my_list.append(num)

    print("Voici tous les nombres de la liste: ",my_list)
    print("Voici uniquement les nombres pairs: ",even_list)


multiple_numb( 4,5,8,54,23 )