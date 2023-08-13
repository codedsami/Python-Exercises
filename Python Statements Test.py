

st = 'Print only the words that start with s in this sentence'
st = st.split()

for s in st:
    if s[0] == 's':
        print(s)
       
for n in range(0, 11):
    if n%2 == 0:
        print(n)
        
list1 = [num  for num in range(1,50) if num%3 == 0]     
print(list1)
   
#list2 = [num if num%3 == 0 else 0 for num in range(1,50) ]     
#print(list2)

st = 'Print every word in this sentence that has an even number of letters'
st = st.split()
for even in st:
    if len(even)%2 == 0:
        print(even)
        
for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print('FizzBuzz')
    elif i%3 == 0:
        print('Fizz')
    elif i%5 == 0:
        print('Buzz')
    else: 
        print(i) 
        
st = 'Create a list of the first letters of every word in this string'
l = [f[0] for f in st.split()]
print(l)