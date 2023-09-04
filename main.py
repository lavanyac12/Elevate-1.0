import sys, os
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QRect, QEventLoop
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QPushButton, QGridLayout, QVBoxLayout
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5 import uic
from ElevatorBackendLogic import Elevator
from PyQt5 import QtCore
#Imports images
import logo_rc
import tree
import carpet
import floor

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

class ElevateInterior(QMainWindow):
    """
    ElevateInterior is the main window for the elevate interior GUI 
    """

    def __init__(self):
        """
        The constructor for ElevateInterior class

        Parameters:
            self (ElevateExterior): An instance of ElevateExterior
        """
                
        super(ElevateInterior, self).__init__()
        uic.loadUi("ElevateInterior.ui", self)
        self.show()
        self.signal = 0

        #Sets the current directory to the directory of the file
        self.CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
        
        self.soundPlayer = QMediaPlayer()

        #Resets the style of the buttons
        self.resetFloorStyle = "background-color: rgb(180, 182, 203); border-style: outset; border-width: 2px; border-radius: 16px; border-color: black;"        
        self.clickedStyle = "background-color: orange; border-style: outset; border-width: 2px; border-radius: 16px; border-color: black;"
        self.clickedCall = "background-color: green; border-style: outset; border-width: 2px; border-radius: 16px; border-color: black; font: bold 14px;"
        self.clickedHelp = "background-color: red; border-style: outset; border-width: 2px; border-radius: 16px; border-color: black; font: bold 14px;"
        self.arrowStyle = "background-color: orange; font: 32pt;"
        self.resetArrowStyle = "background-color: rgb(0, 0, 0); font: 32pt;"

        self.pushExit.clicked.connect(self.exitElevator)

        #Creates an elevator object for elevator logic 
        #Sets the floor number
        self.elevator1 = Elevator(10, 2)
        self.elevator1.setFloorQueue()

        self.floorButtons = [self.pressButton1,
                             self.pressButton2,
                             self.pressButton3,
                             self.pressButton4,
                             self.pressButton5,
                             self.pressButton6,
                             self.pressButton7,
                             self.pressButton8,
                             self.pressButton9,
                             self.pressButton10]

        self.closeIntDoors()
        self.holdClose.toggle()

        #Connecting button clicks
        for flrBtn in self.floorButtons:
            flrBtn.clicked.connect(self.floorButtonClicked)

        exterior.exteriorElevatorBtn.clicked.connect(self.exteriorFloorButtonClicked)

        self.holdClose.clicked.connect(self.holdCloseBtn)
        self.holdOpen.clicked.connect(self.holdOpenBtn)

        self.pushBackButton.clicked.connect(exterior.backBtn)
        self.changeView.clicked.connect(self.changeViewBtn)

        self.pressCallButton.clicked.connect(self.callIsPressed)
        self.pressHelpButton.clicked.connect(self.helpIsPressed)

        #Displays the current floor on elevator display
        self.displayFloor.display(1)

    def floorButtonClicked(self):
        """
        Manages elevator when buttons are clicked
        Adds floor to the queue, sets arrows for direction, and increments the display count 
        
        Parameters:
            self (ElevateInterior): An instance of ElevateInterior 
        """

        #Receives button that was clicked
        btn = self.sender()

        #Changes the current floor to the floor that was selected
        if (self.elevator1.currentFloor + 1) != int(btn.text()):
            btn.setStyleSheet(self.clickedStyle)
            self.elevator1.toggleOn(int(btn.text()) - 1)
            self.displayFloor.setDigitCount(2)

            #Moves elevator to selected floor 
            while (self.signal != 1 and 1 in self.elevator1.floorQueue):
                self.move_elevator()

            if 1 not in self.elevator1.floorQueue:
                self.intUpArrow.setStyleSheet(self.resetArrowStyle)
                self.intDownArrow.setStyleSheet(self.resetArrowStyle)

    def exteriorFloorButtonClicked(self):
        """
        Manages the elevator when an elevator is called from the exterior 

        Parameters:
            self (ElevateInterior): An instance of ElevateInterior 
        """
        btn = exterior.sender()

        btn.setStyleSheet(self.clickedStyle)

        #Moves the elevator and controls the doors
        if (self.elevator1.currentFloor + 1) != int(exterior.floorNumber.text()):
            self.elevator1.toggleOn(int(exterior.floorNumber.text()) - 1)
            self.move_elevator()
        else:
            exterior.openExtDoors()
            loop = QEventLoop()
            QTimer.singleShot(self.elevator1.elevatorMoveTime * 1000, loop.quit)
            loop.exec_()
            exterior.closeExtDoors()
            exterior.exteriorElevatorBtn.setStyleSheet(self.resetFloorStyle)

    def playAudioInterior(self, sound):
        """
        Plays the audio for the elevator interior
        
        Parameters:
            self (ElevateInterior): An instance of ElevateInterior
            sound (str): The sound to play
        """

        #Gets audio from directory and plays it when called
        url = QUrl.fromLocalFile(os.path.join(self.CURRENT_DIR, sound))
        content = QMediaContent(url)
        self.soundPlayer.setMedia(content)
        self.soundPlayer.play()

    def callIsPressed(self):
        """
        Manages the call button when clicked
        
        Parameters:
            self (ElevateInterior): An instance of ElevateInterior
        """

        #Starts audio and resets style of button
        self.pressCallButton.setStyleSheet(self.clickedCall)
        self.playAudioInterior("callSound.mp3")
        self.pressCallButton.clicked.connect(self.callIsPressedAgain)

    def callIsPressedAgain(self):
        """
        Manages the call button when unclicked
        
        Parameters:
            self (ElevateInterior): An instance of ElevateInterior
        """

        #Stops audio and resets style of button
        self.soundPlayer.stop()
        self.pressCallButton.setStyleSheet(self.resetFloorStyle)
        self.pressCallButton.clicked.connect(self.callIsPressed)

    def helpIsPressed(self):
        """
        Manages the help button when clicked
        
        Parameters:
            self (ElevateInterior): An instance of ElevateInterior
        """

        #Starts audio and resets style of button
        self.pressHelpButton.setStyleSheet(self.clickedHelp)
        self.playAudioInterior("alarmSound.mp3")
        self.pressHelpButton.clicked.connect(self.helpIsPressedAgain)

    def helpIsPressedAgain(self):
        """
        Manages the help button when unclicked
        
        Parameters:
            self (ElevateInterior): An instance of ElevateInterior
        """
        #Stops audio and resets style of button
        self.pressHelpButton.setStyleSheet(self.resetFloorStyle)
        self.soundPlayer.stop()
        self.pressHelpButton.clicked.connect(self.helpIsPressed)

    def move_elevator(self):
        """
        Moves the elevator to the next floor and updates floor display

        Parameters:
            self (ElevateInterior): An instance of ElevateInterior
        """
        self.elevator1.setDirection()
        self.signal = 1

        #Manages elevator when direction is upwards
        if self.elevator1.direction == "Up" and self.elevator1.currentFloor != self.elevator1.nextFloor:
            self.intDownArrow.setStyleSheet(self.resetArrowStyle)
            self.intUpArrow.setStyleSheet(self.arrowStyle)

            exterior.extDownArrow.setStyleSheet(self.resetArrowStyle)
            exterior.extUpArrow.setStyleSheet(self.arrowStyle)

            self.holdClose.setEnabled(False)
            self.holdOpen.setEnabled(False)

            self.elevator1.getNextFloor()
            self.elevator1.currentFloor += 1

            loop = QEventLoop()
            QTimer.singleShot(self.elevator1.elevatorMoveTime * 1000, loop.quit)
            loop.exec_()

            self.displayFloor.display(self.elevator1.currentFloor + 1)
            exterior.lcdFloorDisplay.display(self.elevator1.currentFloor + 1)
            self.move_elevator()

        #Manages elevator when direction is downwards
        elif self.elevator1.direction == "Down" and self.elevator1.currentFloor != self.elevator1.nextFloor:
            self.intUpArrow.setStyleSheet(self.resetArrowStyle)
            self.intDownArrow.setStyleSheet(self.arrowStyle)

            exterior.extUpArrow.setStyleSheet(self.resetArrowStyle)
            exterior.extDownArrow.setStyleSheet(self.arrowStyle)

            self.holdClose.setEnabled(False)
            self.holdOpen.setEnabled(False)

            self.elevator1.getNextFloor()
            self.elevator1.currentFloor -= 1

            loop = QEventLoop()
            QTimer.singleShot(self.elevator1.elevatorMoveTime * 1000, loop.quit)
            loop.exec_()

            self.displayFloor.display(self.elevator1.currentFloor + 1)
            exterior.lcdFloorDisplay.display(self.elevator1.currentFloor + 1)
            self.move_elevator()
        
        #Manages elevator when destination is reached
        elif self.elevator1.currentFloor == self.elevator1.nextFloor:
            self.holdClose.setCheckable(False)
            self.signal = 0
            self.elevator1.reachedFloor()

            self.holdClose.setEnabled(True)
            self.holdOpen.setEnabled(True)

            self.floorButtons[self.elevator1.currentFloor].setStyleSheet(self.resetFloorStyle)

            exterior.exteriorElevatorBtn.setStyleSheet(self.resetFloorStyle)
            exterior.extUpArrow.setStyleSheet(self.resetArrowStyle)
            exterior.extDownArrow.setStyleSheet(self.resetArrowStyle)

            self.openIntDoors()
            if (self.elevator1.currentFloor + 1) == int(exterior.floorNumber.text()):
                exterior.openExtDoors()

            self.playAudioInterior("reachingFloors.mp3")

            loop = QEventLoop()
            QTimer.singleShot(5 * 1000, loop.quit)
            loop.exec_()

            if not(self.holdClose.isChecked()):
                self.closeIntDoors()
                if (self.elevator1.currentFloor + 1) == int(exterior.floorNumber.text()):
                    exterior.closeExtDoors()

    def openIntDoors(self):
        """
        Opens the interior doors of the elevator

        Parameters:
            self (ElevateInterior): An instance of ElevateInterior
        """

        #Manages left door
        self.intLefta = QPropertyAnimation(self.intLeft, b"geometry")
        self.intLefta.setDuration(1000)
        self.intLefta.setStartValue(QRect(90, 10, 211, 691))
        self.intLefta.setEndValue(QRect(90, 10, 41, 691))
        self.intLefta.setEasingCurve(QEasingCurve.InOutCubic)

        #Manages right door
        self.intRighta = QPropertyAnimation(self.intRight, b"geometry")
        self.intRighta.setDuration(1000)
        self.intRighta.setStartValue(QRect(300, 10, 201, 691))
        self.intRighta.setEndValue(QRect(460, 10, 41, 691))
        self.intRighta.setEasingCurve(QEasingCurve.InOutCubic)

        self.intLefta.start()
        self.intRighta.start()

    def closeIntDoors(self):
        """
        Closes the interior doors of the elevator

        Parameters:
            self (ElevateInterior): An instance of ElevateInterior
        """
        
        #Manages left door
        self.intLefta = QPropertyAnimation(self.intLeft, b"geometry")
        self.intLefta.setDuration(1000)
        self.intLefta.setStartValue(QRect(90, 10, 41, 691))
        self.intLefta.setEndValue(QRect(90, 10, 211, 691))
        self.intLefta.setEasingCurve(QEasingCurve.InOutCubic)

        #Manages right door
        self.intRighta = QPropertyAnimation(self.intRight, b"geometry")
        self.intRighta.setDuration(1000)
        self.intRighta.setStartValue(QRect(460, 10, 41, 691))
        self.intRighta.setEndValue(QRect(300, 10, 201, 691))
        self.intRighta.setEasingCurve(QEasingCurve.InOutCubic)

        self.intLefta.start()
        self.intRighta.start()

    def holdCloseBtn(self):
        """
        Holds the interior doors of the elevator closed
        
        Parameters:
            self (ElevateInterior): An instance of ElevateInterior
        """

        self.holdClose.setCheckable(True)
        self.holdClose.toggle()
        self.closeIntDoors()

    def holdOpenBtn(self):
        """
        Holds the interior doors of the elevator open
        
        Parameters:
            self (ElevateInterior): An instance of ElevateInterior
        """
                
        loop = QEventLoop()
        QTimer.singleShot(self.elevator1.elevatorMoveTime * 1000, loop.quit)
        loop.exec_()

    def exitElevator(self):
        """
        Exits the elevator interior GUI and returns to the elevator exterior GUI

        Parameters:
            self (ElevateInterior): An instance of ElevateInterior
        """

        exterior.floorNumber.setText(str(self.elevator1.currentFloor + 1))
        self.soundPlayer.setMuted(True)
        widget.setCurrentIndex(2)

    def changeViewBtn(self):
        """
        Changes the view of the elevator to the exterior view by selecting a floor

        Parameters:
            self (ElevateInterior): An instance of ElevateInterior
        """
        self.soundPlayer.setMuted(True)
        widget.setCurrentIndex(3)


class ElevateExterior(QMainWindow):
    """
    ElevateExterior is the main window for the elevate exterior GUI 
    """

    def __init__(self):
        """
        The constructor for ElevateExterior class

        Parameters:
            self (ElevateExterior): An instance of ElevateExterior
        """
        super(ElevateExterior, self).__init__()
        uic.loadUi("ElevateExterior.ui", self)
        self.show()
        self.displaySignal = QtCore.pyqtSignal(str)
        self.closeExtDoors()

        #Manages button for entering an elevator
        self.pushEnter.clicked.connect(self.enterElevator)

        #Manages the button for going to the home page
        self.pushBackButton.clicked.connect(self.backBtn)

        #Manages displays
        self.lcdFloorDisplay.setDigitCount(2)
        self.lcdFloorDisplay.display(1)

        #Resets the style of the arrows
        self.arrowStyle = "background-color: orange; font: 32pt;"
        self.resetArrowStyle = "background-color: rgb(0, 0, 0); font: 32pt;"

    def openExtDoors(self):
        """
        Opens the exterior doors of the elevator

        Parameters:
            self (ElevateExterior): An instance of ElevateExterior 
        """

        #Manages left door
        self.extLefta = QPropertyAnimation(self.extLeft, b"geometry")
        self.extLefta.setDuration(1000)
        self.extLefta.setStartValue(QRect(0, 0, 221, 591))
        self.extLefta.setEndValue(QRect(0, 0, 41, 591))
        self.extLefta.setEasingCurve(QEasingCurve.InOutCubic)

        #Manages right door 
        self.extRighta = QPropertyAnimation(self.extRight, b"geometry")
        self.extRighta.setDuration(1000)
        self.extRighta.setStartValue(QRect(220, 0, 211, 591))
        self.extRighta.setEndValue(QRect(390, 0, 41, 591))
        self.extRighta.setEasingCurve(QEasingCurve.InOutCubic)

        self.extLefta.start()
        self.extRighta.start()

    def closeExtDoors(self):
        """
        Closes the exterior doors of the elevator

        Parameters:
            self (ElevateExterior): An instance of ElevateExterior 
        """

        #Manages left door
        self.extLefta = QPropertyAnimation(self.extLeft, b"geometry")
        self.extLefta.setDuration(1000)
        self.extLefta.setStartValue(QRect(0, 0, 41, 591))
        self.extLefta.setEndValue(QRect(0, 0, 221, 591))
        self.extLefta.setEasingCurve(QEasingCurve.InOutCubic)

        #Manages right door 
        self.extRighta = QPropertyAnimation(self.extRight, b"geometry")
        self.extRighta.setDuration(1000)
        self.extRighta.setStartValue(QRect(390, 0, 41, 591))
        self.extRighta.setEndValue(QRect(220, 0, 211, 591))
        self.extRighta.setEasingCurve(QEasingCurve.InOutCubic)

        self.extLefta.start()
        self.extRighta.start()

    def enterElevator(self):
        """
        Exits the elevator exterior GUI and returns to the elevator interior GUI

        Parameters:
            self (ElevateExterior): An instance of ElevateExterior
        """
        widget.setCurrentIndex(1)
        interior.soundPlayer.setMuted(False)

    def backBtn(self):
        """
        Returns to the main page

        Parameters:
            self (ElevateExterior): An instance of ElevateExterior
        """
        interior.soundPlayer.setMuted(True)
        widget.setCurrentIndex(0)


class MainPage(QMainWindow): 
    """
    MainPage is the class that contains the main page of the GUI
    """

    def __init__(self):
        """
        The constructor for MainPage class

        Parameters:
            self (MainPage): An instance of MainPage
        """
        super(MainPage, self).__init__()
        uic.loadUi("startPage.ui", self)
        self.show()

        #Connecting button clicks
        self.popUpButtons = [self.pushStatement, self.pushTeam, self.pushHelp, self.pushUpdate, self.pushVersion]
        for popButton in self.popUpButtons:
            popButton.clicked.connect(self.show_popup)  

        #Connecting start simulation to exterior window
        self.pushStart.clicked.connect(self.startSim)    

    def show_popup(self):
        """
        Shows the pop up window when the user clicks on the pop up buttons

        Parameters:
            self (MainPage): An instance of MainPage
        """

        #Receives what button was clicked
        btn = self.sender()

        msg = QMessageBox()

        #Different tabs on main page and their associated messages
        if btn.text() == "Company Statement":
            msg.setWindowTitle("Company Statement")
            statementText = "COMPANY STATEMENT: \n\nEstablished in 2023, High Rise Elevator Inc. creates a platform, Elevate, that provides consumers with a safe and secure “Elevator Management System”. \nThe feedback from community members form the foundation of our standards, whether it be for residential, business, or governmental purposes. "
            msg.setText(statementText)
            x = msg.exec_()
        elif btn.text() == "Meet The Team":
            msg.setWindowTitle("Meet The Team")
            teamText = "MEET THE TEAM: \n\nElevate is a hard working team\n\nLavanya Chhilwar\nJaden Rajan George\nKartikey Garg\nSayyada Aisha Mehvish\nNifemi Ogunmade\nMolly Toby\nLynn John-Koshy" 
            msg.setText(teamText)
            x = msg.exec_()
        elif btn.text() == "Get Help":
            msg.setWindowTitle("Get Help")
            helpText = "CONTACT: \n\nContact us by phone or email at: \n\n(416) 967 - 1111 \n gethelp@elevate.ca" 
            msg.setText(helpText)
            x = msg.exec_()
        elif btn.text() == "Update":
            msg.setWindowTitle("Install Update")
            updateText = "UPDATES: \n\nTo install the latest updates go to: \n\nwww.elevate.ca/updates" 
            msg.setText(updateText)
            x = msg.exec_()
        elif btn.text() == "Version":
            msg.setWindowTitle("Current Version")
            versionText = "CURRENT VERSION: \n\nElevate 1.1" 
            msg.setText(versionText)
            x = msg.exec_()

    def startSim(self):
        """
        Starts the simulation, beginning in the interior view

        Parameters:
            self (MainPage): An instance of MainPage
        """
        widget.setCurrentIndex(1)
        interior.soundPlayer.setMuted(False)

class ChangeView(QMainWindow):
    """
    ChangeView is the class that goes to the associated exterior GUI based on the floor selected
    """

    def __init__(self):
        super(ChangeView, self).__init__()
        uic.loadUi("pickExteriorFloor.ui", self)
        self.show()

        #All exterior floor buttons
        self.floorButtons = [self.exteriorButton1,
                             self.exteriorButton2,
                             self.exteriorButton3,
                             self.exteriorButton4,
                             self.exteriorButton5,
                             self.exteriorButton6,
                             self.exteriorButton7,
                             self.exteriorButton8,
                             self.exteriorButton9,
                             self.exteriorButton10]
        
        #Connecting button clicks
        for Btn in self.floorButtons:
            Btn.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        """
        Changes the floor in the exterior GUI

        Parameters:
            self (ChangeView): An instance of ChangeView
        """
        btn = self.sender()
        exterior.floorNumber.setText(btn.text())
        widget.setCurrentIndex(2)

if __name__ == '__main__':
    """
    The main function of the program
    
    Parameters:
        None
    """
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    #Creates instances of the class
    #Adds them to the widgets
    mainPage = MainPage()
    exterior = ElevateExterior()
    interior = ElevateInterior()
    viewChanger = ChangeView()
    widget.addWidget(mainPage)
    widget.addWidget(interior)
    widget.addWidget(exterior)
    widget.addWidget(viewChanger)

    #Sets the dimension of the window
    interiorWidth = interior.width()
    interiorHeight = interior.height()
    interior.setFixedSize(900, 800)

    widget.show()
    app.exec_()