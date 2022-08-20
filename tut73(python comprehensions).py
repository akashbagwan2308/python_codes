#python comprehensions

# ls = []
# for i in range(100):
#     if i%3 ==0:
#         ls.append(i)
# ----------------list comprehension---------------------
ls = [i for i in range(100) if i%3==0]     # this is list comprehension
print(ls)

# --------------- dictionary comprehension--------------------------
# dict1 = { i:f"item{i}" for i in range(1,1000) if i%100==0}   # this is dictionary comprehension
dict1 = { i:f"item{i}" for i in range(5)}   # this is dictionary comprehension
dict2 = {value:key for key,value in dict1.items()}  # reverse of an dictionary
print(dict1)
print(dict2)
# --------------- Set comprehension--------------------------
dresses = {dress for dress in ['dress1','dress2','dress1'
    ,'dress2','dress1','dress2']}   # this is set comprehensions
print(dresses)
print(type(dresses))
# ----------- Generators Comprehensions --------------------

evens = (i for i in range(100) if i%2 == 0)
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())
# for item in evens:
#     print(item)

