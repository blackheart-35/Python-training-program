I have 39 keywords. in which 4 soft keywords and 35 are hard keywords

###  list:-

1: list



*  it works as dynamic array
* declaration: \[]
*  store data type



### sets:-

###  

* in sets indexing is not available
* its immutable
* declaration : {}



### Dictionary:



* it is combination of key value
* declaration := key:value
* it is semi-mutable
* key can not be updated but value can
* new key value can be added



### string:



* its declaration : ""

### 

### **tuple** :

* tuple are immutable



* stores every type

 

### slicing :





● It is the process of fetching multiple characters from the

collection at the same time using positive indexing.

● Syntax: var\[start index : end index+1 : step value/updation]

● Where,

● Start index is the index of the character we want to start

from.

● End index is the index of the character till where we want to

fetch the characters.

● Step value is the number of steps we are taking to reach

from one character to another.

● eg:

s=”python”

If we want to fetch ‘thon’ from this collection we can use positive slicing.







###  Negative slicing:







It is the process of fetching more than one character at a single time with

* the help of negative indexes.





### operations on multi valued data type:



#### Add operations:



1. \- .Append (add in the end of line)
2. \- .insert(insert new element at given index)
3. \- .Extend (add multiple value in the end of line of code)
4. \- .Concatenation(
5.  its working on in place(it modifies or change the list but does not create new list) insertion





#### Access operation:



* my list \[index\_value]
* my list \[start : stop]





#### update operation:



\#mylist\[index\_value] = change/replace to update







# pop:





\#my\_list.pop(index/value by default last time)





### Remove:



\#my\_list.remove(value/element that you want to remove)





### Delete:



\# del my\_list\[start : stop]





### Clear:



\#my\_list.clear(clear everything)



### reverse:

### 

it reverse the list



\#my\_list.reverse()





### sort:



it sorts the list in ascending or descending order



\#my\_list.sort()





### operation on dictionary:



#### Add operation:



#### syntax:



\#my\_dict\[key] = value



#### update operation:



##### syntax:



\#my\_dict.update({'key':value,'key':value,'key':value,'key':value,'key':value,......})





### Remove operation:



#### syntax:



1. \#my\_dict.pop(key) {remove specific given key}
2. \#my\_dict.popitem(){remove last key/item of list}





#### Example:





a={

    'ac':'hyy',

    'aod':'jg',

    'hc':'gh'

}

print(a.popitem())

print(a)

print(a.pop('ac'))

print(a)



##### output:



('hc', 'gh')

{'ac': 'hyy', 'aod': 'jg'}

hyy

{'aod': 'jg'}





### view operation:



can fetch key and value or both.



.keys()



.values()



.items() it gives output as a list of tuples.(\[])



### bitwise operator:



* these are the operator that directly work on binary
* they work on binar format 0 and 1





1.  Bitwise and operator(\&)
2.  Bitwise or operator(|)
3.  Bitwise xor operator(^)
4.  Bitwise left shift operator(<<)
5.  Bitwise right shift operator(>>)





* and \& or \& xor work on two value



* left shift and right shift work on single value



### and operator :



* output bit become one when if both output bits are one













### or operator







* the output is false when both condition are false





### bitwise "or" operator :







* each bits become one when only one bits become one



#### Truth table :





##### 0   0   0

##### 0   1	1

##### 1   0	1

##### 1   1	0









### left shift :





* Bits move to the left, and new 0s come in from the right.
* 
* Effect:
* 
* Number becomes bigger (multiplies by 2 for each shift).
* 
* Example:
* 4 << 1
* 
* 
* Binary of 4 → 0100
* 
* Left shift by 1 → 1000 → 8



### 

### 

### Right Shift (>>)



* Bits move to the right, and:
* 
* For positive numbers, new bits on the left are 0
* 
* For negative numbers, new bits are 1 (sign bit preserved)
* 
* Effect:
* 
* Number becomes smaller (divides by 2 for each shift).



#### Example:

4 >> 1





* Binary of 4 → 0100
* 
* Right shift by 1 → 0010 → 2











### Assignment operator:





###### We have only one assignment operator which is equal operator(=). It is

###### used to assign the value to variables.

###### Apart from this we have an augmented assignment operator, which is

###### used to update the already existing value of any variable and store the

###### resultant output in the same variable.

###### 







Eg: a=12

a=a+8 or a+=8

a=20









### Membership operators:







###### These operators are used to check if a given value is a part or member

###### of a given collection(multi valued data type)

###### We have only 2 membership operators:





###### 1\. IN

###### 2\. not in

















### &nbsp;Identity operators:



###### These operators are used to check if two variables are pointing towards

###### same memory location or not

###### We have only 2 identity operators:

###### 1 IS

###### 2 IS NOT









###### 

















