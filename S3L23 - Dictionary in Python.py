
# In comparison with Lists,  DICTIONARIES  are unordered mappings for storing Objs.
# CAN’T be sorted.

# Dictionaries use a Key-Value pairing. This helps to quickly grab
# Obj-s without need to know an index of a location.

# {"Key1":"Value1", "Key2":"Value2"}

# Keys should always be STRINGS.
# Values could be anything.

my_Dictionary = {"Key1":"Value1", "Key2":"Value2"}

my_Dictionary
# {'Key1': 'Value1', 'Key2': 'Value2'}

my_Dictionary["Key2"]
# 'Value2'

my_Dictionary2 = {"Apple":2.99, "Oranges":1.99, "Milk":5.80}

my_Dictionary2["Oranges"]
# 1.99

# Example of a Dictionary containing an int, a List & another Dictionary:
d = {"K1":123, "K2":[8,5,3], "K3":{"insideKey4":100}}

d["K3"]
# {'insideKey4': 100}

# Calling a Nested Obj-s:

d["K3"]["insideKey4"]
# 100

d["K2"][2]
# 3


# Modifying inner content:
d2 = {"Key1":["a","b","c"]}

d2
# {'Key1': ['a', 'b', 'c']}

d2["Key1"][2].upper()
# 'C'

# Adding new Key-Value pairs to a Dictionary:
d3 = {"K1":100,"K2":200}

d3["K3"] = 300

d3
# {'K1': 100, 'K2': 200, 'K3': 300}


# Overwrite existing Key-Value pair:
d3["K1"] = "NEW VALUE"

d3
# {'K1': 'NEW VALUE', 'K2': 200, 'K3': 300}


# Showing content:
d4 = {'K01': 10, 'K02': 20, 'K03': 30}

d4.keys()
# dict_keys(['K01', 'K02', 'K03'])

d4.values()
# dict_values([10, 20, 30])

d4.items()
# dict_items([('K01', 10), ('K02', 20), ('K03', 30)])


#Content in parentheses ( ) are actually a Tuple/Кортеж
