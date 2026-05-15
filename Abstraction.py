from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card 💳")

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI 📱")

class NetBanking(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Net Banking 🏦")

if __name__ == "__main__":

    choice = input("Enter payment method (card/upi/net): ").lower()
    amount = float(input("Enter amount: "))

    if choice == "card":
        payment = CreditCard()
    elif choice == "upi":
        payment = UPI()
    elif choice == "net":
        payment = NetBanking()
    else:
        print("Invalid choice")
        exit()

    payment.pay(amount)
