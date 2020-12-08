for T in range(int(input())):
    n,m = map(int,input().split())
    if n<=30:
        count=0
        a=list(map(int,input().split()))
        for i in a:
            if i%m==0:
                count+=1
        print(pow(2,count)-1)  
