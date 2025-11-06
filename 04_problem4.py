#What will be the length of following set s: 
# Answer: 1
s = set() 
s.add(20) 
s.add(20.0) 
#s.add('20') # length of s after these operations? 
print(len(s))

# Answer: 2
x = set() 
x.add(20)
x.add('20')
print(len(x))