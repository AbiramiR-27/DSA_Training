from decimal import HAVE_THREADS
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
    def add_end(self,val):
        new_node=Node(val)
        if self.head is None:
            self.head=new_node
        else:
            cur=self.head
            while cur.next is not None:
                cur=cur.next
            cur.next=new_node
    def delete_node_first_node(self):
        if self.head is None:
            print("Empty list")
        else:
            self.head=self.head.next
    def delete_last(self):
        if self.head is None:
            print("Empty list")
        elif self.head.next is None:
            self.head=None
        else:
            cur=self.head
            while cur.next.next is not None:
                cur=cur.next
            cur.next=None
    def delete_an_element(self,val):
        if self.head is None:
            print("Empty list")
        else:
            cur=self.head
            while cur.next is not None:
                if cur.val==val:
                    cur.next=cur.next.next
                cur=cur.next
            if cur.val==val:
                cur.next=None
            else:
                print("The element is not found")
    def insert_an_element_after_an_element(self,val,aff):
        if self.head is None:
            print("Empty List")
        else:
            cur=self.head
            new_node=Node(aff)
            while cur.next is not None:
                if cur.val==val:
                    new_node.next=cur.next
                    cur.next=new_node
                cur=cur.next
            if cur.val==val:
                new_node.next=None
                cur.next=new_node
            else:
                print("The element is not found")

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
    x=int(input("Enter to add at end: "))
    y=int(input("Enter to add at begin: "))
    for i in n:
        sl.add_begin(i)
    sl.add_begin(y)
    sl.add_end(x)
    sl.delete_node_first_node()
    sl.display()