#ejm1
users = ['Alexandra', 'Nicolas', 'Thor', 'Gorda']

for user in users:
    print(user)

#ejm2
user1 = 'Alexandra'

for u in user1:
    print(u)

#En for tambien se utiliza break, continue

#ejm3:
for x in range(3, 30, 3):
    print(x)
else: #else se puede ocupar para dejar algun mensaje
    print('End')

#ejm4
users = ['Alexandra', 'Nicolas', 'Thor', 'Gorda']
ages = [21, 18, 1, 11]

for user in users:
    for age in ages:
        print(user, age)