import random
import time
import os

class Vehicle:
    def __init__(self, vehicle_type, position):
        self.vehicle_type = vehicle_type
        self.position = position  # Position as (row, col)

class TrafficLight:
    def __init__(self):
        self.green_vertical = True  # Vertical light state
        self.green_horizontal = False  # Horizontal light state

    def toggle(self):
        self.green_vertical = not self.green_vertical
        self.green_horizontal = not self.green_horizontal

class Intersection:
    def __init__(self, size):
        self.size = size
        self.traffic_light = TrafficLight()
        self.vertical_vehicles = []
        self.horizontal_vehicles = []
        self.light_vertical_position = (size // 2, size // 2)  # Center position for vertical light
        self.light_horizontal_position = (size // 2, size // 2 + 1)  # Adjacent right for horizontal light

    def add_vertical_vehicle(self, vehicle):
        self.vertical_vehicles.append(vehicle)

    def add_horizontal_vehicle(self, vehicle):
        self.horizontal_vehicles.append(vehicle)

    def process_traffic(self):
        # Process vertical vehicles
        for vehicle in self.vertical_vehicles:
            if vehicle.position[0] < self.size - 1:
                # Check if vehicle is at the traffic light
                if vehicle.position[0] == self.light_vertical_position[0] and vehicle.position[1] == self.light_vertical_position[1]:
                    if not self.traffic_light.green_vertical:
                        continue  # Stop if the light is red
                vehicle.position = (vehicle.position[0] + 1, vehicle.position[1])
        self.vertical_vehicles = [v for v in self.vertical_vehicles if v.position[0] < self.size]

        # Process horizontal vehicles
        for vehicle in self.horizontal_vehicles:
            if vehicle.position[1] < self.size - 1:
                # Check if vehicle is at the traffic light
                if vehicle.position[0] == self.light_horizontal_position[0] and vehicle.position[1] == self.light_horizontal_position[1]:
                    if not self.traffic_light.green_horizontal:
                        continue  # Stop if the light is red
                vehicle.position = (vehicle.position[0], vehicle.position[1] + 1)
        self.horizontal_vehicles = [v for v in self.horizontal_vehicles if v.position[1] < self.size]

    def display(self):
        # Create a matrix representation of the intersection
        matrix = [['.' for _ in range(self.size)] for _ in range(self.size)]
        
        # Place vertical vehicles
        for vehicle in self.vertical_vehicles:
            matrix[vehicle.position[0]][vehicle.position[1]] = vehicle.vehicle_type[0].upper()

        # Place horizontal vehicles
        for vehicle in self.horizontal_vehicles:
            matrix[vehicle.position[0]][vehicle.position[1]] = vehicle.vehicle_type[0].upper()

        # Traffic light positions
        vertical_light_symbol = 'G' if self.traffic_light.green_vertical else 'R'
        horizontal_light_symbol = 'G' if self.traffic_light.green_horizontal else 'R'
        matrix[self.light_vertical_position[0]][self.light_vertical_position[1]] = vertical_light_symbol
        matrix[self.light_horizontal_position[0]][self.light_horizontal_position[1]] = horizontal_light_symbol

        # Print the matrix
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal
        for row in matrix:
            print(" ".join(row))
        print("\nVertical traffic light is " + ("green" if self.traffic_light.green_vertical else "red"))
        print("Horizontal traffic light is " + ("green" if self.traffic_light.green_horizontal else "red"))

def random_vertical_vehicle(size):
    vehicle_type = random.choice(['car', 'truck'])
    position = (0, size // 2)  # Start in the middle of the first column
    return Vehicle(vehicle_type, position)

def random_horizontal_vehicle(size):
    vehicle_type = random.choice(['car', 'truck'])
    position = (size // 2, 0)  # Start in the middle of the first row
    return Vehicle(vehicle_type, position)

def main():
    size = 5  # Size of the intersection matrix
    intersection = Intersection(size)
    simulation_time = 30  # Simulate for 30 seconds
    start_time = time.time()

    while time.time() - start_time < simulation_time:
        # Randomly introduce vertical vehicles
        if random.random() < 0.3:  # 30% chance to add a vertical vehicle each loop
            new_vehicle = random_vertical_vehicle(size)
            intersection.add_vertical_vehicle(new_vehicle)
            print(f"Added a {new_vehicle.vehicle_type} to the vertical lane.")

        # Randomly introduce horizontal vehicles
        if random.random() < 0.3:  # 30% chance to add a horizontal vehicle each loop
            new_vehicle = random_horizontal_vehicle(size)
            intersection.add_horizontal_vehicle(new_vehicle)
            print(f"Added a {new_vehicle.vehicle_type} to the horizontal lane.")

        # Process the traffic at the intersection
        intersection.process_traffic()

        # Display the current state of the intersection
        intersection.display()

        # Toggle the traffic lights every 10 seconds
        if int(time.time() - start_time) % 10 == 0:
            intersection.traffic_light.toggle()

        time.sleep(1)  # Wait 1 second before the next iteration

if __name__ == "__main__":
    main()