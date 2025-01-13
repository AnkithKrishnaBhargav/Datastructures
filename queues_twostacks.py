# Enter your code here. Read input from STDIN. Print output to STDOUT

class Queue:
    def __init__(self):
        self.stack1=[]
        self.Mainstack=[]
        
    def enqueue(self,data):
        self.Mainstack.append(data)
    
    def dequeue(self):
        if not self.stack1:
            while self.Mainstack:
                self.stack1.append(self.Mainstack.pop())
        if self.stack1:
            self.stack1.pop()
            
    
    def display(self):
        if not self.stack1:
            print(self.Mainstack[0])  
        else:
            print(self.stack1[-1])
        
            
Q=Queue()
no_op=int(input())
for i in range(no_op):
    n=input()
    l=n.split()
    if l[0]=='1':
        Q.enqueue(int(l[1]))
    elif l[0]=='2':
        Q.dequeue()
    else:
        Q.display()
        
                  
