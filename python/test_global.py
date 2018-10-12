

Money = 2000

def AddMoney():
  global Money
  Money += 1

print Money
AddMoney()
print Money


'''
#comment global Money
Traceback (most recent call last):
  File "test_global.py", line 10, in <module>
    AddMoney()
  File "test_global.py", line 7, in AddMoney
    Money += 1
UnboundLocalError: local variable 'Money' referenced before assignment
'''
