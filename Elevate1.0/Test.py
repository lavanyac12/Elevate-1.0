from ElevatorBackendLogic import Elevator
import unittest


testElevator = Elevator(10, 2)
print("\nElevate 1.0 Test Cases: \n")


class TestFunctions(unittest.TestCase):

    def testSetFloorQueue1(self):
        '''
        Test to see if setFloorQueue() works when the floorQueue is filled with 0's and a 1.
        Should append maxFloor number of 0's
        
        Parameters:
            self (TestFunctions): An instance of TestFunctions
            
        Returns:
                None
        '''

        testElevator.floorQueue = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
        testElevator.setFloorQueue()

        expectedValue = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        resultValue = testElevator.floorQueue

        print("\nTEST 21: SETFLOORQUEUE()")
        print("Expected Value: " + str(expectedValue))
        print("Result Value: " + str(resultValue))
        print("\n")

        self.assertEqual(expectedValue, resultValue)

    def testSetFloorQueue2(self):
        '''
        Test to see if setFloorQueue() works when the floorQueue is an empty list.
        Should append maxFloor number of 0's
        
        Parameters:
            self (TestFunctions): An instance of TestFunctions
            
        Returns:
                None
        '''

        testElevator.floorQueue = []
        testElevator.setFloorQueue()

        expectedValue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        resultValue = testElevator.floorQueue

        print("TEST 22: SETFLOORQUEUE()")
        print("Expected Value: " + str(expectedValue))
        print("Result Value: " + str(resultValue))
        print("\n")

        self.assertEqual(expectedValue, resultValue)

    def testToggleOn1(self):
        '''
        Test to see if toggleOn() works when the floorQueue is full of 0's and we want to stop at floor 4
        
        Parameters:
            self (TestFunctions): An instance of TestFunctions
            
        Returns:
                None
        '''
                
        testElevator.floorQueue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        testElevator.toggleOn(4)

        expectedValue = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        resultValue = testElevator.floorQueue

        print("TEST 23: TOGGLEON()")
        print("Expected Value: " + str(expectedValue))
        print("Result Value: " + str(resultValue))
        print("\n")

        self.assertEqual(expectedValue, resultValue)

    def testToggleOn2(self):
        '''
        Test to see if toggleOn() works when the floorQueue is already full of 1's and we want to stop at floor 6
        
        Parameters:
            self (TestFunctions): An instance of TestFunctions
            
        Returns:
                None
        '''

        testElevator.floorQueue = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        testElevator.toggleOn(6)

        expectedValue = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        resultValue = testElevator.floorQueue

        print("TEST 24: TOGGLEON()")
        print("Expected Value: " + str(expectedValue))
        print("Result Value: " + str(resultValue))
        print("\n")

        self.assertEqual(expectedValue, resultValue)

    def testToggleOff1(self):
        '''
        Test to see if toggleOff() works when the floorQueue is already full of 1's
        
        Parameters:
            self (TestFunctions): An instance of TestFunctions
        
        Returns:
            None
        '''
                
        testElevator.floorQueue = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        testElevator.toggleOff(0)
        testElevator.toggleOff(2)
        testElevator.toggleOff(9)

        expectedValue = [0, 1, 0, 1, 1, 1, 1, 1, 1, 0]
        resultValue = testElevator.floorQueue

        print("TEST 25: TOGGLEOFF()")
        print("Expected Value: " + str(expectedValue))
        print("Result Value: " + str(resultValue))
        print("\n")

        self.assertEqual(expectedValue, resultValue)

    def testToggleOff2(self):
        '''
        Test to see if toggleOff() works when the floorQueue is already full of 0's

        Parameters:
            self (TestFunctions): An instance of TestFunctions

        Returns:
            None
        ''' 
                
        testElevator.floorQueue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        testElevator.toggleOff(0)
        testElevator.toggleOff(2)
        testElevator.toggleOff(9)

        expectedValue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        resultValue = testElevator.floorQueue

        print("TEST 26: TOGGLEOFF()")
        print("Expected Value: " + str(expectedValue))
        print("Result Value: " + str(resultValue))
        print("\n")

        self.assertEqual(expectedValue, resultValue)

    def testSlicedQueueUp1(self):
        '''
        Test to see if slicedQueUp() works when floorQue has a 1 with trailing 0s and 1s, so a floor above currentFloor is toggled.
        Should update floorQue to cut off leading 0s.

        Parameters:
            self (TestFunctions)

        Returns:
          None
        '''
        testElevator.currentFloor = 2
        testElevator.floorQueue = [0, 0, 0, 1, 1, 0, 0, 0, 0, 0]

        expectedValue = [1, 1, 0, 0, 0, 0, 0]
        resultValue = testElevator.slicedQueueUp()

        print("TEST 27: SLICEQUEUEUP()")
        print("Expected Value: " + str(expectedValue))
        print("Result Value: " + str(resultValue))
        print("\n")

        self.assertEqual(expectedValue, resultValue)
    
    def testSlicedQueueUp2(self):
        '''
        Test to see if slicedQueUp() works when currentFloor is the top level
        Should update floorQue to an empty []

        Parameters:
            self (TestFunctions)

        Returns:
            None
        '''
        testElevator.currentFloor = 10
        testElevator.floorQueue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

        expectedValue = []
        resultValue = testElevator.slicedQueueUp()

        print("TEST 28: SLICEQUEUEUP()")
        print("Expected Value: " + str(expectedValue))
        print("Result Value: " + str(resultValue))
        print("\n")

        self.assertEqual(expectedValue, resultValue)

    def testSlicedQueueDown1(self):
        '''
        Test to see if slicedQueueDown() works when a floor in floorQue is selected below currentFloor
        Should cut off leading 0s in floorQue

        Parameters:
            self (TestFunctions)

        Returns:
            None
        '''
        testElevator.currentFloor = 7
        testElevator.floorQueue = [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]

        expectedValue = [1, 0, 0, 1, 0, 0, 0]
        resultValue = testElevator.slicedQueueDown()

        print("TEST 29: SLICEQUEUEDOWN()")
        print("Expected Value: " + str(expectedValue))
        print("Result Value: " + str(resultValue))
        print("\n")

        self.assertEqual(expectedValue, resultValue)

    def testSlicedQueueDown2(self):
        testElevator.currentFloor = 1
        testElevator.floorQueue = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        expectedValue = [1]
        resultValue = testElevator.slicedQueueDown()

        print("TEST 30: SLICEQUEUEDOWN()")
        print("Expected Value: " + str(expectedValue))
        print("Result Value: " + str(resultValue))
        print("\n")

        self.assertEqual(expectedValue, resultValue)

    def testSetDirection1(self):
        testElevator.currentFloor = 5
        testElevator.floorQueue = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        testElevator.setDirection()

        expectedValue = "Down"
        resultValue = testElevator.direction

        print("TEST 31: SETDIRECTION()")
        print("Expected Value: " + str(expectedValue))
        print("Result Value: " + str(resultValue))
        print("\n")

        self.assertEqual(expectedValue, resultValue)

    def testSetDirection2(self):
        testElevator.currentFloor = 5
        testElevator.floorQueue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        testElevator.setDirection()

        expectedValue = "Up"
        resultValue = testElevator.direction

        print("TEST 32: SETDIRECTION()")
        print("Expected Value: " + str(expectedValue))
        print("Result Value: " + str(resultValue))
        print("\n")

        self.assertEqual(expectedValue, resultValue)

    def testSetDirection3(self):
        '''
        Test to see what direction is set when the elevator is on floor 5 and both floor 1 and 10 are toggled on

        Parameters:
            self (TestFunctions): An instance of TestFunctions

        Returns:
            None
        ''' 
        testElevator.currentFloor = 5
        testElevator.floorQueue = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        testElevator.setDirection()

        expectedValue = "Up"
        resultValue = testElevator.direction

        #Will always go up first
        print("TEST 33: SETDIRECTION()")
        print("Expected Value: " + str(expectedValue))
        print("Result Value: " + str(resultValue))
        print("\n")

        self.assertEqual(expectedValue, resultValue)

    def testSetDirection4(self):
        '''
        Test to see what direction is set when the elevator is on floor 1 and floor 1 is toggled on

        Parameters:
            self (TestFunctions): An instance of TestFunctions

        Returns:
            None
        ''' 

        testElevator.currentFloor = 1
        testElevator.floorQueue = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        testElevator.setDirection()

        expectedValue = "Down"
        resultValue = testElevator.direction

        print("TEST 34: SETDIRECTION()")
        print("Expected Value: " + str(expectedValue))
        print("Result Value: " + str(resultValue))
        print("\n")

        self.assertEqual(expectedValue, resultValue)

    def testSetDirection5(self):
        '''
        Test to see what direction is set when the elevator is on floor 10 and floor 10 is toggled on

        Parameters:
            self (TestFunctions): An instance of TestFunctions

        Returns:
            None
        ''' 
        testElevator.currentFloor = 10
        testElevator.floorQueue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        testElevator.setDirection()

        expectedValue = "Down"
        resultValue = testElevator.direction

        print("TEST 35: SETDIRECTION()")
        print("Expected Value: " + str(expectedValue))
        print("Result Value: " + str(resultValue))
        print("\n")

        self.assertEqual(expectedValue, resultValue)

    def testGetNextFloor1(self):
        '''
        Test to see if the elevator is able to read the next floor of the elevator to be visited
        
        Parameters:
            self (TestFunctions): An instance of TestFunctions

        Returns:
            None
        ''' 
        testElevator.currentFloor = 5
        testElevator.floorQueue = [0, 0, 0, 0, 0, 0, 1, 1, 0, 0]
        testElevator.getNextFloor()

        expectedValue = 6
        resultValue = testElevator.nextFloor

        print("TEST 36: GETNEXTFLOOR()")
        print("Expected Value: " + str(expectedValue))
        print("Result Value: " + str(resultValue))
        print("\n")

        self.assertEqual(expectedValue, resultValue)

    def testGetNextFloor2(self):
        '''
        Test to see if the elevator is able to read the next floor of the elevator to be visited
        
        Parameters:
            self (TestFunctions): An instance of TestFunctions

        Returns:
            None
        ''' 
        testElevator.currentFloor = 5
        testElevator.floorQueue = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        testElevator.getNextFloor()

        expectedValue = 8
        resultValue = testElevator.nextFloor

        print("TEST 37: GETNEXTFLOOR()")
        print("Expected Value: " + str(expectedValue))
        print("Result Value: " + str(resultValue))
        print("\n")

        self.assertEqual(expectedValue, resultValue)

    def testGetNextFloor3(self):
        '''
        Test to see if the elevator is able to read the next floor of the elevator to be visited
        
        Parameters:
            self (TestFunctions): An instance of TestFunctions

        Returns:
            None
        ''' 
        testElevator.currentFloor = 5
        testElevator.direction = "Down"
        testElevator.floorQueue = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        testElevator.getNextFloor()

        expectedValue = 2
        resultValue = testElevator.nextFloor

        print("TEST 38: GETNEXTFLOOR()")
        print("Expected Value: " + str(expectedValue))
        print("Result Value: " + str(resultValue))
        print("\n")

        self.assertEqual(expectedValue, resultValue)

    def testReachedFloorA(self):
        '''
        Test to see if reachedFloor() works for given floorQueue, and current floor is updated.
        
        Parameters: 
            self (TestFunctions)

        Returns:
            None
        '''
        
        testElevator.currentFloor = 5
        testElevator.floorQueue = [0, 0, 0, 0, 1, 0, 1, 0, 0, 0]
        testElevator.getNextFloor()
        testElevator.toggleOff(testElevator.currentFloor - 1)
        testElevator.reachedFloor()

        expectedValue = 4
        resultValue = testElevator.currentFloor

        print("TEST 39: REACHEDFLOOR()")
        print("Expected Value: " + str(expectedValue))
        print("Result Value: " + str(resultValue))
        print("\n")

        self.assertEqual(expectedValue, resultValue)

    def testReachedFloorB(self):
        '''
        Test to see if reachedFloor() works for given floorQueue, and queue is updated.
        
        Parameters: 
            self (TestFunctions)

        Returns:
            None
        '''

        testElevator.currentFloor = 5
        testElevator.floorQueue = [0, 0, 0, 0, 1, 0, 1, 0, 0, 0]
        testElevator.getNextFloor()
        testElevator.toggleOff(testElevator.currentFloor - 1)
        testElevator.reachedFloor()

        expectedValue = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
        resultValue = testElevator.floorQueue

        print("TEST 40: REACHEDFLOOR()")
        print("Expected Value: " + str(expectedValue))
        print("Result Value: " + str(resultValue))
        print("\n")

        self.assertEqual(expectedValue, resultValue)

if __name__ == '__main__':
    unittest.main()