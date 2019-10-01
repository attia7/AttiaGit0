balance = 700
papers=[100, 50, 10, 5,4,3,2,1]

def withdraw(balance, request):
    if balance < request :
        print('Sorry, you are try withdraw: {0}, but Your balance just : {1}'.format(request, balance))
    else:
        print ('your balance >>', balance)
        orgnal_request = request
        while request > 0:
            for i in papers:
                while request >= i:
                    print('give', i)
                    request-=i
        balance -= orgnal_request
    return balance


def withdraw1(balance, request):
    give = 0
    if balance < request :
        print('Sorry, you are try withdraw: {0}, but Your balance just : {1}'.format(request, balance))
    else: 
        print ('your balance >>', balance)
        balance -= request
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
    return balance

balance = withdraw(balance, 777)
balance = withdraw(balance, 276)
balance = withdraw1(balance, 276)
balance = withdraw(balance, 34)
balance = withdraw1(balance, 5)
balance = withdraw1(balance, 500)