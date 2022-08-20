"""
List of food with calories
reverse it by three methods:
1.inbulit
2.list[::-1]
3.swaping first with last
input: list from user
output: reverse list
"""
# --------------------------------------------------------------------------------------
list = ['Pizza:554','Burger:5695','Shake:655','Pani-Puri:558', 'Milk:58555','Samose:655']
list2 = list.copy()
list3 = list.copy()
print("Original list : ",list)
# Method 1st :-----
list.reverse()
print("Revered list by method 1 : ",list)
# Method 2nd :-----
list2 = list2[::-1]
print("Revered list by method 2 : ",list2)
# Method 3rd :-----
list4=[]
for i in range(len(list3)-1,-1,-1):
    list4.append(list3[i])
print("Revered list by method 3 : ",list4)
