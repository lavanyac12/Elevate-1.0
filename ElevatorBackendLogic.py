import random
import time

"""
ELEVATE 1.0

TOPIC: 
Elevator Management System

GROUP:
Lavanya Chhilwar (lchhilwar@torontomu.ca)
Jaden Rajan George (jadenrajan.george@torontomu.ca)
Kartikey Garg (kgarg@torontomu.ca)
Sayyada Aisha Mehvish (amehvish@torontomu.ca)
Nifemi Ogunmade (oogunmade@torontomu.ca)
Molly Toby (molly.toby@torontomu.ca)
Lynn John-Koshy (lynn.johnkoshy@torontomu.ca)
"""

class Elevator:
    """
    Elevator is used to facilitate backend logic of the elevator movement and respond the user calls
    """

    def __init__(self ,maxFloors, elevatorMoveTime):
        """
        Constructor for the elevator class
        
        Parameters:
            self (Elevator): An instance of Elevator
            maxFloors (int): The maximum number of floors in the building
            elevatorMoveTime (int): The time it takes for the elevator to move from one floor to floor
        """

        self.currentFloor = 0
        self.nextFloor = None
        self.maxFloors = maxFloors
        self.floorQueue = []
        self.elevatorMoveTime = elevatorMoveTime
        self.direction = "Up"

    def setFloorQueue(self):
        """
        Resets the floorQueue to 0
        
        Parameters: 
            self (Elevator): An instance of Elevator
        """
        for i in range(self.maxFloors):
            self.floorQueue.append(0)

    def toggleOn(self,floorNumber):
        """
        Sets the floorQueue attribute to 1 meaning it should be visited
        
        Parameters:
            self (Elevator): An instance of Elevator
            floorNumber: The floor number the elevator is going to
        """
        self.floorQueue[floorNumber] = 1

    def toggleOff(self, floorNumber):
        """
        Sets the floorQueue attribute to 0 meaning it has been visited and/or it has not been called
        
        Parameters:
            self (Elevator): An instance of Elevator
            floorNumber: The floor that the elevator has gone too
        """

        self.floorQueue[floorNumber] = 0

    def slicedQueueUp(self):
        """
        Checks whether floors above the current are toggled on
        
        Parameters:
            self (Elevator): An instance of Elevator
        """

        return self.floorQueue[self.currentFloor + 1:]

    def slicedQueueDown(self):
        """
        Checks whether floors below the current are toggled on
        
        Parameters:
            self (Elevator): An instance of Elevator
        """
        slicedQueueDown = self.floorQueue[0: self.currentFloor ]
        slicedQueueDown.reverse()

        return slicedQueueDown

    def setDirection(self):
        """
        Sets the direction of the elevator
        
        Parameters:
            self (Elevator): An instance of Elevator
        """
                
        if 1 in self.slicedQueueUp() and 1 not in self.slicedQueueDown():
            self.direction = "Up"
        elif 1 in self.slicedQueueDown() and 1 not in self.slicedQueueUp():
            self.direction = "Down"

    def getNextFloor(self):
        """
        Gets the next floor of the elevator to be visited
        
        Parameters:
            self (Elevator): An instance of Elevator
        """
                
        if self.direction == "Up":
            self.nextFloor = self.slicedQueueUp().index(1) + self.currentFloor + 1

        elif self.direction == "Down":
            self.nextFloor = (len(self.slicedQueueDown()) - self.slicedQueueDown().index(1) - 1)

    def reachedFloor(self):
        """
        Sets the current floor to be toggled off as it has been reached and next floor to be none
        
        Parameters:
            self (Elevator): An instance of Elevator
        """

        self.toggleOff(self.currentFloor)
        self.currentFloor = self.nextFloor
        self.nextFloor = None

def main():
    pass

if __name__ == "__main__":
   main()