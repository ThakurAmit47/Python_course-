import random
class Train():
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to} ")

    def getstatus(self):
        print(f"train no {self.trainNo} is on time")

    def getFare(self):
        print(f"train no {self.trainNo} Ticket fare is {random.randint(222, 5555)}")
        
t = Train(23431)
t.book("Gwalior", "Bhopal")
t.getstatus()
t.getFare()