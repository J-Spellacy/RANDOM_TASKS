
k = [2, 3, 4, 5, 6, 7, 8, 9]

'''
Takes a list of numbers and returns a list of the products of all the numbers in the 
list except the number at the index of the current iteration.

Without Division 1st and with division 2nd
'''

# without division
new_k = []
for i in range(0, len(k)):
    temp = k.copy()
    temp.pop(i)
    print(i, temp, k)
    l = 1
    for j in range(0, len(temp)):
        l = temp[j] * l
    new_k.append(l)

print(new_k)

# with division
new_k = []
l = 1
for i in range(0, len(k)):
    l = k[i] * l
for j in range(0, len(k)):
    new_k.append(l // k[j])
print(new_k)
        
