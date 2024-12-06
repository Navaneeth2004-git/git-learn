keys = ['a','b','c','d']
values=[1,2,3,4]
a=zip(keys,values)
print(list(a))



dict_values={k:v for(k,v) in zip(keys,values)}
print(dict_values)