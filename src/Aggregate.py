from src.LinkedList import LinkedList

"""
Aggregate class is responsible for implementating various operations on the linked list
    1. Get Minimum Timed Task Details
    2. Get Maximum Timed Task Details
    3. Get Average of all the execution times of the tasks pushed in the linked list
"""
class Aggregate:
    #Initializing linked list object for various operations
    def __init__(self, linked_list:LinkedList):
        self.linked_list = linked_list
    
    #Function responsible for searching the task having maximum execution time among all the tasks
    def get_maximised_time_task(self):
        temp_node = self.linked_list.get_list_head()
        if temp_node is None:
            return -1
        max_task = temp_node
        max_task_time = temp_node.end_time - temp_node.start_time
        temp_node = temp_node.next
        while(temp_node):
            time = temp_node.end_time - temp_node.start_time
            if(time>=max_task_time):
                max_task_time = time
                max_task = temp_node

            temp_node = temp_node.next

        return max_task, max_task_time
    
    #Function responsible for searching the task having minimum execution time among all the tasks
    def get_minimised_timed_task(self):
        temp_node = self.linked_list.get_list_head()
        if temp_node is None:
            return -1
        min_task = temp_node
        min_task_time = temp_node.end_time - temp_node.start_time
        temp_node = temp_node.next
        while (temp_node):
            time = temp_node.end_time - temp_node.start_time
            if (time <= min_task_time):
                min_task_time = time
                min_task = temp_node

            temp_node = temp_node.next

            return min_task , min_task_time
    
    #Function responsible for calculating average of the all execution times of the tasks in the linked list
    def get_average_time_of_all_tasks(self):
        temp_node = self.linked_list.get_list_head()
        if temp_node is None:
            return 0

        sum_of_task_time = 0
        counter=0
        while(temp_node):
            time = temp_node.end_time - temp_node.start_time
            sum_of_task_time+=time
            counter+=1
            temp_node=temp_node.next

        return sum_of_task_time/counter ,sum_of_task_time,counter