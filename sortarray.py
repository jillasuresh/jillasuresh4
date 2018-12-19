def sortit(arr,n): 
    for i in range(n): 
        arr[i] = i+1
    if __name__=='__main__': 
     arr=[10,7,9,2,8,3,5,4,6,1] 
     n=len(arr) 
    sortit(arr,n) 
   for i in range(n): 
      print(arr[i],end=" ") 
