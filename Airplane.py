import random
airplane_statuses = ["landing", "takeoff", "emergency landing"] 

# Αυτή η κλάση χρησιμοποιείται στην κλάση αεροδρόμιο 
class Airplane:
    def __init__(self, number, time):
        self.plane_number = number
        self.arrival_time = time
        self.has_problem = False
        self.plane_status = "In order"

    # Αυτή η μέθοδός δείχνει τον αριθμό πτήσης του αεροπλάνου 
    def show_airplane_number(self):
        return self.plane_number
    
    # Αυτή η μέθοδος δείχνει την ώρα άφιξης
    def show_airplane_arrival_time(self):
        return self.arrival_time
    
    # Αυτή η μέθοδος δείχνει αιτήμα προσγείωσης
    def request_landing(self): 
        print(f"Flight {self.show_airplane_number()} requests landing")

    # Αυτή η μέθοδος δείχνει αιτήμα απογείωσης
    def request_takeoff(self): 
        print(f"Flight {self.show_airplane_number()} requests takeoff")

    # Αυτή η μέθοδος δείχνει αιτήμα εκτακτής προσγείωσης 
    def request_emergency_landing(self): 
        print(f"Flight {self.show_airplane_number()} requests emergency landing")

    # Αυτή η μέθοδος δείχνει την κατάσταση του αεροπλάνου
    def get_airplane_status(self):
        airplane_statuses_length = len(airplane_statuses)
        random_number = random.randint(0, airplane_statuses_length - 1)
        self.plane_status = airplane_statuses[random_number]
        if (self.plane_status == "landing"):
            self.request_landing()
        if (self.plane_status == "takeoff"):
            self.request_takeoff()
        if (self.plane_status == "emergency landing"):
            self.has_problem = True
            self.request_emergency_landing()