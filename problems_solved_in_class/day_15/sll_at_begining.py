class Node:
    def __init__(self,val):
        self.next=None
        self.val=val
class SLL:
    def __init__(self):
        self.head=None
    def add_begin(self,val):
        new_node=Node(val)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
    def display(self):
        if self.head is None:
            print("Empty List")
        else:
            cur=self.head
            while cur is not None:
                print(cur.val, end=" ")
                cur=cur.next
    

if __name__ == "__main__":
    sl=SLL()
    n=list(map(int,input().split()))
    for i in n:
        sl.add_begin(i)
    sl.display()