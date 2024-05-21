from json import load

from task5 import exgcd

with open('./resources/Crypto_task_6_file_9.json') as file:
    data = load(file)  # P Q G x k h(m)

y = pow(data['G'], data['x'], data['P'])
r = pow(data['G'], data['k'], data['P']) % data['Q']
s = exgcd(data['k'], data['Q'])[1] * (data['h(m)'] + data['x'] * r) % data['Q']
print(y, r, s)
