class A:
	def __init__(self):
		self.data1 = None
a = A()
print(id(a))
print(id(a.data1))
b = A()
print(id(b))
print(id(b.data1))
c = A()
print(id(c))
print(id(c.data1))
a.data1 = c
b.data1 = c
print(id(a))
print(id(a.data1))
print(id(b))
print(id(b.data1))
print(id(c))
print(id(c.data1))

class Node(object):
    def __init__(self, value, nextnode=None):
        self.value = value
        self.znextnode = nextnode

    def append(self, n):
        if not isinstance(n, Node):
            n = Node(n)
        self.znextnode, n = n, self.znextnode
        self.znextnode.znextnode = n
        
print("lasskdfj;asdfk")
a1 = Node(1)
print(id(a1))
print(id(a1.znextnode))
b1 = Node(2)
print(id(b1))
print(id(b1.znextnode))
c1 = Node(3)
print(id(c1))
print(id(c1.znextnode))

a1.append(c1)
b1.append(c1)
print(id(a1))
print(id(a1.znextnode))
print(id(b1))
print(id(b1.znextnode))
print(id(c1))
print(id(c1.znextnode))