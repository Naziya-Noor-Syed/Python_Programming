class Account:
    def __init__(self, accno, accpass):
        self.accno = accno
        self.__accpass = accpass

    def reset_pass(self):
        print(self.__accpass)

acc1= Account("12345", "abcde")
print("Account number:", acc1.accno)
print(acc1.reset_pass())