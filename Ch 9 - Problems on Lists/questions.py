"""
1.
Create a list of five fruits: apple, banana, orange, kiwi, grapes.

2.
Extend this list of fruits to add five vegetables to it: potato, tomato, onion, capsicum, beans.

3.
Append one more vegetable to it: brinjal

4. 
Remove 'capsicum' from this list.

5.
Create a new list without bringing in any vegetable or fruit whose first letter of name is 'b'.

6.
Remove first fruit and first vegetable from this list.

7.
Pop the third item.

8.
Reverse the list.

9. 
Sort the list.

10.
Clear all items from the list.

11.
Delete the list completely.

12. 
What is the difference between .remove() and .pop()?

13.
How do you check if a list contains an element? Show that list of fruits contain the apple.

14.
What is the difference between append and extend?


"""

# Solutions

l = ['apple', 'banana', 'orange', 'kiwi', 'grapes']

v = ['potato', 'tomato', 'onion', 'capsicum', 'beans']

l.extend(v)

print(l)

l.append('brinjal')

print(l)

l.remove('capsicum')

print(l)

m = [i for i in l if not i.startswith('b')]

print(m)

l.remove('apple')
l.remove('potato')

print(l)

l.pop(3)

print(l)

l.reverse()

print(l)

l.sort()

print(l)

l.clear()

print(l)

del l

l = ['apple', 'banana', 'orange', 'kiwi', 'grapes']
print('apple' in l)

# 12: remove() takes the item value. pop() takes the item index.

# 14: append() adds an element. extend() does the concatenation of two lists.