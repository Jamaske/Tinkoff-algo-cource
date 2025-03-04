class Node:
    def __init__(self, val):
        self.val:int = val
        self.sum:int = val
        self.left:Node|None = None
        self.right:Node|None = None


class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        if self.root == None: 
            self.root = Node(val)
            return
        
        cur_node = self.root

        while True:
            cur_node.sum += val
            if val <= cur_node.val:
                if cur_node.left == None:
                    cur_node.left = Node(val)
                    return
    
                cur_node = cur_node.left
            else:
                if cur_node.right == None:
                    cur_node.right = Node(val)
                    return
                cur_node = cur_node.right
        
    def Print(self, node = 0, depth = 0):
        if node == None: return
        if node == 0: 
            node = self.root
            print(f"[{node.val}] {node.sum}")
        else:
            print("|  "*(depth-1) + f"|--[{node.val}] {node.sum}")
        self.Print(node.left, depth + 1)
        self.Print(node.right, depth + 1)
        

    def range_sum_requr(self, l, r):
        #declare 2 nested reqursive functions
        def Right(cur:Node):
            nonlocal total, b
            if not cur: return
            if cur.val < b:# go further right (confirm positive mode assumption)
                Right(cur.right)
            elif cur.val == b:# exact border found (right subtree contredict positive assumption)
                if cur.right != None:
                    total -= cur.right.sum
            else:# change direction to Left (to negative estimate mode)
                total -= cur.sum
                Left(cur.left)

        def Left(cur:Node):
            nonlocal total, b
            if not cur: return
            if cur.val > b: # go futher left (confirm negative mode assumption)
                Left(cur.left)
            elif cur.val == b:# exact border found (val + left subtree contredicts negeative assumption)
                total += cur.val
                if cur.left != None:
                    total += cur.left.sum
            else: # cahnge direction to Right (to positive estimate mode)
                total += cur.sum
                Right(cur.right)
                
        if self.root == None: 
            return 0
        # lazy aproach for less code
        # sum[l,r] = sum[:r] - sum[:l) = sum[:r] - sum[:l - 1]
        total:int = 0
        b = l - 1
        Left(self.root)
        total = self.root.sum - total
        b = r
        Right(self.root)

        return total
    
    def range_sum(self, l:int, r:int):
        if not self.root: return 0

        def inf_B(cur: Node, b:int):
            total:int = cur.sum
            while True:

                while cur and cur.val < b: cur = cur.right

                if not cur: break
                if cur.val == b:
                    if cur.right: total -= cur.right.sum
                    break 
                
                total -= cur.sum
                cur = cur.left

                while cur and cur.val > b: cur = cur.left

                if not cur: break
                if cur.val == b:
                    total += cur.val
                    if cur.left: total += cur.left.sum
                    break

                total += cur.sum
                cur = cur.right
            return total

        return inf_B(self.root, r) - inf_B(self.root, l - 1)


            



    




tree = Tree()
for el in (8,4,2,1,3,6,5,7,12,10,9,11,14,13,15): tree.insert(el)

tree.Print()

l = 3
r = 8

print(tree.range_sum(l, r))
print((l+r)*(r-l+1) // 2)