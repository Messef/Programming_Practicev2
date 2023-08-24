a=["a", 'b', 'c']
counter=0
for i in enumerate(a):
    print(i)
    if i=='a':
        print('nice')
    counter+=1
print(counter)