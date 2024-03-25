from Airplane import Airplane
from Airport import Airport
import datetime
import random


class Simulation:
    def __init__(self, number_of_scheduled_planes, maxsize_of_landing_planes):
        self.scheduled_planes =  number_of_scheduled_planes
        self.landing_maxsize = maxsize_of_landing_planes
        self.airport = Airport()

    def start_simulation(self):
        plane_requests = 1
        while(plane_requests < self.scheduled_planes):
            request_time = datetime.datetime.now() + datetime.timedelta(minutes = 10)
            plane = Airplane(random.randint(1000,9999), request_time)
            plane.get_airplane_status()
            if(plane.plane_status == "landing" or plane.has_problem):
                self.airport.Add_airplane_to_landing_queue(plane)
            if(plane.plane_status == "takeoff"):
                self.airport.Add_airplane_to_takeoff_queue(plane)

            plane_requests += 1

            if(plane.has_problem):
                self.airport.Remove_airplane_from_landing_queue(plane)

            if(self.airport.landing_queue.size() == self.landing_maxsize):
                while (not self.airport.landing_queue.isEmpty()):
                    waiting_plane = self.airport.landing_queue.items[0]
                    self.airport.Remove_airplane_from_landing_queue(waiting_plane)

            if(not self.airport.is_runway_busy() and not self.airport.takeoff_queue.isEmpty()):
                while (not self.airport.takeoff_queue.isEmpty()):
                    plane_to_depart = self.airport.takeoff_queue.items[0]
                    self.airport.Remove_airplane_from_takeoff_queue(plane_to_depart)

        print(f"Schedule with {plane_requests} planes was completed.")


simulation = Simulation(50, 3)
simulation.start_simulation()