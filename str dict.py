str1 = "marolix technology"
dict = {}
for key in str1 :
    dict[key] = dict.get (key, 0) + 1
print("count all characters" + str(dict))
                         
