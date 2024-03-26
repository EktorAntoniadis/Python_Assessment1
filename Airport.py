from Airplane import Airplane
from GeneralQueue import GeneralQueue

# Αυτή η κλάση είναι για το αεροδρόμιο 
class Airport:
    def __init__(self):
        self.busy = False
        self.landing_queue = GeneralQueue()
        self.takeoff_queue = GeneralQueue()
        self.airplane_counter = 1
        
    # Αυτή η μέθοδος προσθέτει ένα αεροπλάνο στην ουρά προσγείωσης 
    def Add_airplane_to_landing_queue(self, airplane: Airplane):
        self.landing_queue.enqueue(airplane)
        self.airplane_counter += 1

    # Αυτή η μέθοδος προσθέτει ένα αεροπλάνο στην ουρά απογείωσης
    def Add_airplane_to_takeoff_queue(self, airplane: Airplane):
        self.takeoff_queue.enqueue(airplane)
        self.airplane_counter += 1

    # Αυτή η μέθοδος αφαιρεί ένα αεροπλάνο από την ουρά προσγείωσης
    def Remove_airplane_from_landing_queue(self, airplane: Airplane):
        print(f"CONTROL {airplane.plane_number} landing")
        if(airplane.has_problem):
            self.landing_queue.priority_dequeue(airplane)
        else:
             self.landing_queue.dequeue()
        self.busy = True
        if(self.landing_queue.isEmpty() and self.takeoff_queue.isEmpty()):
            self.busy = False

    # Αυτή η μέθοδος αφαιρεί ένα αεροπλάνο από την ουρά απογείωσης
    def Remove_airplane_from_takeoff_queue(self, airplane: Airplane):
        if(self.landing_queue.isEmpty()):
            print(f"CONTROL {airplane.plane_number} takeoff")
            self.takeoff_queue.dequeue()
            self.busy = True
        if(self.landing_queue.isEmpty() and self.takeoff_queue.isEmpty()):
            self.busy = False

    # Αυτή η μέθοδος μας ελέγχει ότι ο διάδρομος είναι άδειος
    def is_runway_busy(self):
        if (not self.landing_queue.isEmpty()):
             self.busy = True
        else: 
            self.busy = False     
        return self.busy