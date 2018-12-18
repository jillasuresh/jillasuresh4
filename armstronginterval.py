lower case=int(input(""))
upper case=int(input(""))
 for n in range(lower case,upper case+1):
  sum = 0
 temp = num
   while temp>0:
       digit=temp%10
       sum+= digit ** 3
       temp//=10
 if n==sum:
       print(n)
