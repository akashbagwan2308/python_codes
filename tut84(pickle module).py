# Pickle Module
import pickle
# # pickling a python object
# cars = ['Audi','BMW','Maruti']
# file = 'mycar.pkl'
# fileobj = open(file,"wb")
# pickle.dump(cars,fileobj)
# fileobj.close()
# Accessing mycar.pkl file using pickle module
file = 'mycar.pkl'
fileobj = open(file,"rb")
mycar  = pickle.load(fileobj)
print(mycar)