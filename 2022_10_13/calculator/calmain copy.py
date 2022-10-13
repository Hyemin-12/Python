import imp
from calculator import *

n1 = int(input('첫 번째 수는? : '))
n2 = int(input('두 번째 수는? : '))

print(f'{n1} + {n2} = {add(n1, n2)}')
print(f'{n1} - {n2} = {sub(n1, n2)}')
print(f'{n1} * {n2} = {mul(n1, n2)}')
print(f'{n1} / {n2} = {div(n1, n2)}')