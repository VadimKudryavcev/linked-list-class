from linkedlist import LinkedList

ll = LinkedList()

ll2 = LinkedList()
ll2.add('ddd')
ll2.add('c3d')

ll3 = LinkedList()

print(ll3[0])

ll.add('a')
ll.add('b')
ll.add('c')
ll.add(ll3)
ll.add(10)
ll.add(ll2)

print(ll)

print(ll[0])
print(ll[1])
print(ll[2])

print(ll.len())
