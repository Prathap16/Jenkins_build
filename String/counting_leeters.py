s="Enter Some ##Strin!g"
list1=[word.strip("#") for word in s.split()]
print(' '.join(reversed(list1)))
