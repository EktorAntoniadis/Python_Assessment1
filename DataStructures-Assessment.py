import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []
    
airplane_statuses = ["landing", "takeoff", "emergency landing"] 
    
class Airplane:
    def __init__(self, number, time):
        self.plane_number = number
        self.arrival_time = time
        self.has_problem = False
        self.plane_status = "In order"

    def show_airplane_number(self):
        return self.plane_number
    
    def show_airplane_arrival_time(self):
        return self.arrival_time
    
    def request_landing(self): 
        print(f"Flight {self.show_airplane_number()} requests landing")

    def request_takeoff(self): 
        print(f"Flight {self.show_airplane_number()} requests takeoff")

    def request_emergency_landing(self): 
        print(f"Flight {self.show_airplane_number()} requests emergency landing")

    def get_airplane_status(self):
        airplane_statuses_length = len(airplane_statuses)
        random_number = random.randint(0, airplane_statuses_length - 1)
        self.plane_status = airplane_statuses[random_number]
        if (self.plane_status == "landing"):
            self.request_landing()
        if (self.plane_status == "takeoff"):
            self.request_takeoff()
        if (self.plane_status == "emergency landing"):
            self.request_emergency_landing()

class Airport:
    def __init__(self):
        self.busy = False
        self.landing_queue=Queue()
        self.takeoff_queue=Queue()
        self.airplane_counter = 1
        
    def Add_airplane_to_landing_queue(self, airplane):
        self.landing_queue.enqueue(airplane)
        self.airplane_counter += 1

    def Add_airplane_to_takeoff_queue(self, airplane):
        self.takeoff_queue.enqueue(airplane)
        self.airplane_counter += 1

    def Remove_airplane_from_landing_queue(self, airplane):
        print(f"CONTROL {airplane.plane_number} takeoff")
        self.landing_queue.dequeue()
        self.busy = True
        if(self.landing_queue.isEmpty() and self.takeoff_queue.isEmpty()):
            self.busy = False

    def Remove_airplane_from_takeoff_queue(self, airplane):
        if(self.landing_queue.isEmpty()):
            print(f"CONTROL {airplane.plane_number} takeoff")
            self.takeoff_queue.dequeue()
            self.busy = True
        if(self.landing_queue.isEmpty() and self.takeoff_queue.isEmpty()):
            self.busy = False

    def is_runway_busy(self):
        return self.busy
    
class Simulation:
    def __init__(self):
        None 