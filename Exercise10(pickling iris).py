# Pickling iris
#uci ml repository --> datasets --> iris --> iris.data
# download(using link) --> text --> parsing --> list of list --> pickle --> reading code
import requests
import pickle

data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
# print(data)
list = data.split("\n")
# print(list)
list2 = [item.split(",") for item in list if len(item)!=0]
print(list2)
with open("myiris.pkl","wb") as f:
    pickle.dump(list2,f)

# ---------------------------Code to read pickle file -----------------------------------
with open("myiris.pkl","rb") as f:
    print(pickle.load(f))

