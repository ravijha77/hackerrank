n=int(input())
a=input()
l=a.strip().split()
myset=set(l)
y=list(map(int,list(myset)))
y.sort()
t=len(y)
print(y[t-2])