import random
class Train():
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(slf, fro, to): 
        print(f"Ticket is booked in train no: {slf.trainNo} from {fro} to {to} ")

    def getstatus(self):
        print(f"train no {self.trainNo} is on time")

    def getFare(Harry): #self ki jagah kuch or bhi likh de to fark nhi padta bss bahi same usi ke function me likhna padega 
        #exmple
        print(f"train no {Harry.trainNo} Ticket fare is {random.randint(222, 5555)}")
        
t = Train(23431)
t.book("Gwalior", "Bhopal")
t.getstatus()
t.getFare()