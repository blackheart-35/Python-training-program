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





1. &nbsp;Bitwise and operator(\&) 
2. &nbsp;Bitwise or operator(|) 
3. &nbsp;Bitwise xor operator(^) 
4. &nbsp;Bitwise left shift operator(<<) 
5. &nbsp;Bitwise right shift operator(>>)





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









left shift 

