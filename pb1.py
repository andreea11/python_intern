__author__ = 'andreea'

'''Given the binary tree in the image below, use a built in
python data structure to represent the binary tree
and easy to find any nodes within a given interval
(say: find all nodes that have a value between 23 and 68). '''

'''am ales ca si reprezentare pentru arbore o lista de forma:
 	[key, left, right] '''
class BinarySearchTree:

    root = None
    def __init__(self):
        self.root = []

    def construct(self,value):
        if self.root == []:
            self.root=[value,[],[]]
            #print(self.root)
        else:
            node=self.root
            while node:
               if value < node[0]:
                node=node[1]
               else:
                   node=node[2]
            node[:] = [value,[],[]]

    def range(self,min,max):
      while(self.root != []):
          if (len(self.root) !=1 ):
              node=self.root.pop()
              while (node != []):
                  aux=node.pop()
                  if isinstance(aux,int):
                       if ((aux>min) and (aux<max)):
                          print (aux)
                  else:
                      for i in aux:
                          if ((i>min) and (i<max)):
                            print (i)
          else:
              #if ((self.root>min) and (self.root<=max)):
              print (self.root)
              break



    def toString(self):
        return "This {} ".format(self.root)


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.construct(20)
    tree.construct(15)
    tree.construct(10)
    tree.construct(17)
    tree.construct(5)
    tree.construct(2)
    tree.construct(8)
    tree.construct(30)
    tree.construct(25)
    tree.construct(40)
    print(tree.toString())
    tree.range(1,40)



