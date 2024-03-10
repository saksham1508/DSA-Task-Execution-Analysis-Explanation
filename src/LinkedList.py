"""
Node Class:
    This is responsible for storing task details in the class and can be added to linked list
"""
class Node:
    #Constructor Implementation to take task_id , start_time, end_time
    def __init__(self,task_id,start_time=0,end_time=0):
        self.task_id=task_id
        self.start_time=start_time
        self.end_time=end_time
        self.next=0

    #function to return taskid
    def get_task_id(self):
        return self.task_id

#function to return starttime
    def get_start_time(self):
        return self.start_time

# function to return endtime
        def get_end_time(self):
            return self.end_time

#function responsible to return string equivalent of task details having taskid,starttime,endtime
def _str_(self):
    return str({'task_id':self.task_id, 'start_time':self.start_time, 'end_time':self.end_time})

    
"""
LinkedList Class:
    This is responsible for implementing Linked List for the tasks and is used for implementing
    various aggregate operations.

"""
class LinkedList:
    #Constructor Implementation
    def __init__(self):
        self.head = None
        
    #This method will return the head of the linked list
    def get_list_head(self):
        return self.head
    
    #This method is responsible for printing the linked list nodes
    def print_linked_list(self):
        temp_node = self.head
        while(temp_node is not None):
            print(temp_node.get_task_id())
            temp_node = temp_node.next

            
    #This method is responsible for inserting node in the linked list 
    #in the beginning or at end based on the flag as insert_at_starting
    def insert_node(self, node:Node, insert_at_starting=0):
        if node is None:
            return
        elif self.head is None:
            self.head = node

        elif insert_at_starting == 1:
            node.next = self.head
            return
        else:
            last_node =self.head
            while(last_node.next):
                last_node = last_node.next

            last_node.next = node
            return



    
    #This method is responsible for printing the linked list nodes in reverse order
    def print_in_reverse(self, node):
        if node:
            self.print_in_reverse(node.next)
            print(node.task_id)
        else:
            return