# using else with for loop

khana = ["Roti ", "Sabzi", "Chawal","Dal"]

# for item in khana:
#     print(item)
#     # break   # if there is break else will not work
#
# else:
#     print("This for loop ended properly")

for item in khana:
    if item == "paratha":
        break
else:
    print("Your item not found")