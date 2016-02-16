#!/usr/bin/python
'''
Data structures
1. list
2. Dictionaries 
'''

#1
groceries =['bananas','strawberries','apples','bread']
print 'Question 1\n',groceries

#1.a
groceries.append('champagne')
print '\nList after appending champagne:\n',groceries

#1.b
groceries.remove('bread')
print '\nList after removing bread:\n',groceries

#1.c
#Either sort the food items or
#print sorted(groceries)

#We define a dictionary of the items with their fist letters as keys
food_map = {}
for food_item in groceries:
	aisle = food_item[0] #first letter
	food_map[food_item] = aisle # map food item to aisle
print '\nFood map\n',food_map


#function to sort groceries
#not completed
def sort_gro(inp):       
	if  type(inp) is list and len(inp)!=0:
                
		print 545
	else:
		print 123


#2.b
catalog = {
	'apples':7.3,
	'bananas':5.5,
	'bread':1.0,
	'carrots':10.0,
	'champagne':20.9,
 	'strawberries':32.6
}
#print catalog
#2.c
catalog['strawberries']=63.43

#2.d
catalog['chicken']=6.5
#.3.b
in_stock=catalog.keys()
#print in_stock

#3.c
always_in_stock= tuple(in_stock)
#3.d
print '\ncome to shoprite, we always sell:'
for i in range(len(always_in_stock)):
	print i+1,':',always_in_stock[i],'\n'

#4.a
catalog_2 = {
	'apples':7.1,
	'bananas':5.0,
	'bread':2.0,
	'carrots':9.0,
	'champagne':20.0,
 	'strawberries':30.6
}

main_catalog = {
	'current_shop':catalog,
        'other_shop':catalog_2

}
print main_catalog

#4
def binary_insert():
	pass




