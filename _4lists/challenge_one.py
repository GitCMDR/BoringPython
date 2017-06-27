"""this code is to respond to challenge one chapter 4"""

def listonator(list):
    "function will accept a list and return list concatenated with 'and'"
    list.insert(-1, 'and') # insert 'and' on the penultimate index of list
    for i in range(len(list) -2): # run loop and dont run on penultimate spot
        print(list[i] + ',', end=' ') # print all elements of id, instead of newline use ' '
    print(list[-2], end=' ') # add penultimate element to list
    print(list[-1]) # add last element to list

spam = ['apples', 'pizza', 'dogs', 'cats', 'electrode', 'pikachu']
listonator(spam) # output is 'apples, pizza, dogs and cats (or as many words in your list)
