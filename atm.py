class Atm(object):
   def __init__(self,cardNumber, pinNumber):
       self.cardNumber = cardNumber
       self.pinNumber = pinNumber
   def checkBalance(self, balance):
       print("Your balance is" + balance)
       

   def withdrawl(self,balance, amount):
       newAmount = balance - amount
       print("You have withdrawn", str(amount), " and your remaining balance is", str(newAmount))
   
   




balance = input("Please enter your current balance")
card_Number = input("Please enter your card number")
pin_Number = input("please enter pin number")
object1 = Atm(card_Number, pin_Number)

activity = input("Please dial number -> (1)Check Balance, (2) Withdraw, (3) Deposit")

if(activity == 1 ):
    object1.checkBalance(balance)


elif(activity ==2):
    cash = input("Enter the money to be withdrawn")
    object1.withdrawl(balance, cash)


