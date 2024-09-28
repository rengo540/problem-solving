# nuber = 5 
# print(id(nuber))
# number = nuber 
# print(id(number))

# nuber = nuber + 1
# print(id(nuber))

# print(number)
# print(nuber)

# fruits = ["apple"]
# another_fruits = fruits
# fruits += ["banana"]
# print(fruits)
# print(another_fruits)

# print(id(fruits))
# print(id(another_fruits))

# class Fruits :
#     def __init__(self) -> None:
#         self.name = None

# fruits = Fruits()
# fruits.name = "apple"
# import copy
# another = fruits
# print(id(fruits))
# print(id(another))
# another.name = "orange"

# print(fruits.name)
# print(another.name)


# def append_to(item, target=[]):
#       target.append(item)
#       return target


# print(append_to(1))
# print(append_to(1,target=[5]))
# print(append_to(1))
# print(append_to(1))


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,None)))))
head1 = head.next
head1.next = None
print('suii')