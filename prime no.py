odd_prime=[]

for i in range(1, 100,2):

  flag1=1

  flag2=1

  for j in range(2,i):

      if i%j==0:

        flag1=0

        break

      if((i+2)%j==0):

        flag2=0

  if flag1==1 and flag2==1:

    print(i,"and",i+2)