# Task 1
print("\nTask1")
class Node():
	def __init__(self, key, desc):
		self.key = key
		self.left = None
		self.right = None
		self.desc = desc
	
def insert(root, node):

	if root is None:
		root = node 
	
	else:
		if root.key < node.key:
			if root.right is None:
				root.right = node 
			else:
				insert(root.right, node)
		else:
			if root.left is None:
				root.left = node
			else:
				insert(root.left, node)

		
def preorder(root):
  if root:
    print(root.key)
    preorder(root.left)
    preorder(root.right)

r = Node(35, "desc")
array = [75,25,62,101,13,9,33,8]

for i in array:
	insert(r, Node(i, "desc"+str(i)))

preorder(r)
	

# Task 2
print("\nTask2")

def checkHeight(root):
    if root is None: 
        return False
    return max(checkHeight(root.left)+1, checkHeight(root.right))

def checkBalance(root):
    if root is None: 
        return True
    return checkBalance(root.right) and checkBalance(root.left) and abs(checkHeight(root.left) - checkHeight(root.right)) < 2

if checkBalance(r)==True:
  print("The tree is balanced")
else:
  print("The tree is not balanced")
    

# Task 3
print("\nTask3")

arrayBalance = [20,30,34,61,110]
for i in arrayBalance:
  insert(r, Node(i, "desc"+str(i)))
  
preorder(r)

if checkBalance(r)==True:
  print("The tree is balanced")
else:
  print("The tree is not balanced")


# Task 4 
print("\nTask4")

def searchBST(root, key):
  while root is not None:
    if key > root.key:
      root=root.right
    elif key<root.key:
      root=root.left
    else:
      return True

key = input("Enter your key: ")
if searchBST(r,int(key))==True:
  print("Entered key:",key+", was located in the BST")
else:
  print("Entered key:",key+", was not located in the BST")
  
      



    