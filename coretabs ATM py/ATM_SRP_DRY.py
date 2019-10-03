class ATM:
  def __init__(self, balance, bank_name):
    self.balance = balance
    self.bank_name = bank_name
    self.withdrawals_log = []
    self.currencies=[100, 50, 10, 5,4,3,2,1]

  def greeting(self):
    print('Wellcom to {0} Bank'.format(self.bank_name
    print('your balance >>', self.balance)

  def check_balance(self, request):
    if not(self.balance > request) :
      print('Sorry, you are try withdraw: {0}, but Your balance just : {1}'.format(request, self.balance))
    else:
      return self.balance > request
  
  def show_withdrawlog(self):
    for item in self.withdrawals_log:
      print(item)

  def withdraw(self, request):
    self.greeting()
    self.get_currentbalance()
    if (self.check_balance(request)):
      self.withdrawals_log.append(request)
      self.balance -= request
      while request > 0:
          for coin in self.currencies:
              while request >= coin:
                  print('give', coin)
                  request-=coin


balance1 = 400
balance2 = 500

atm1 = ATM(balance1,"Samba")
atm2 = ATM(balance2,"ALRajhi")

atm1.withdraw(777)
atm2.withdraw(179)
atm1.withdraw(34)
atm2.withdraw(17)
atm1.withdraw(42)
atm2.withdraw(268)
atm1.withdraw(167)


print('----- log withdraw from atm1 -----')
atm1.show_withdrawlog()
print('>>>>> log withdraw from atm2 <<<<<')
atm2.show_withdrawlog()
