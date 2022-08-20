# Json Module
# json == java script object notation
import json

data = '{"var1":"harry","var2":56}'
print(data)

parsed = json.loads(data)
print(parsed)
print(parsed['var1'])
# task = json.load   ????

data2 = { "channel_name": "codewithharry",
          "cars":['BMW','audi a8','ferrary'],
          "fridge":('roti',540),
          "is bad": False}
jscom = json.dumps(data2)  # to make compatible with java script
print(jscom)
# Task = what is sort_keys parameter in  dumps