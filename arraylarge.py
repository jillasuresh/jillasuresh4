def Nmaxelements(list1,N): 
    final_list = [] 
   for i in range(0,N):  
        max1=0
        for j in range(len(list1)):
       if list1[j]>max1: 
                max1=list1[j]; 
                   list1.remove(max1); 
        final_list.append(max1) 
           print(final_list) 
