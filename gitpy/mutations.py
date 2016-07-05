s=input()
a=input()
list=a.strip().split()
s=s[:int(list[0])]+list[1]+s[int(list[0])+1:]
print(s)