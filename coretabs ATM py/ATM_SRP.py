class ATM:
  def __init__(self, balance, bank_name):
    self.balance = balance
    self.bank_name = bank_name

  def greeting(self):
    print('Wellcom to {0} Bank'.format(self.bank_name))

  def get_currentbalance(self):
    print('your balance >>', self.balance)

  def check_balance(self, request):
    if not(self.balance > request) :
      print('Sorry, you are try withdraw: {0}, but Your balance just : {1}'.format(request, self.balance))
    else:
      return self.balance > request

  def withdraw(self, request):
    self.greeting()
    self.get_currentbalance()
    #check_result = self.check_balance(request)
    if (self.check_balance(request)):
      give = 0
      self.balance -= request
      while request > 0:
        if request >= 100:
          give = 100
        elif request >= 50:
          give = 50
        elif request >= 10:
          give = 10
        elif request >= 5:
          give = 5
        else :
          give = request
        print('give',give)
        request -= give

balance1 = 400
balance2 = 500

atm1 = ATM(balance1,"Samba")
atm2 = ATM(balance2,"ALRajhi")

atm1.withdraw(777)
atm2.withdraw(276)
atm1.withdraw(34)
atm2.withdraw(5)
atm1.withdraw(40)
atm1.withdraw(800)
atm1.withdraw(190)


print('----- log withdrawfrom atm1 -----')
atm1.show_withdrawlog()
print('>>>>> log withdrawfrom atm2 <<<<<')
atm2.show_withdrawlog()
