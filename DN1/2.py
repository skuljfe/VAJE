def naloga_2():
    list_1=[0,1,2,3,4,5,6,7,8,9]
    list_2=[9,8,7,6,5,4,3,2,1,0]
    list_3=[]
    j=0

    for i in list_1:
        list_3.append(i+list_2[j])
        j+=1
    
    print(list_3)

naloga_2()