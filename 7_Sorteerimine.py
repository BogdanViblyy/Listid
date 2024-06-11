# Teil on vaja luua programm, mis sorteerib numbrite nimekirja kahaneva/kasvava absoluutväärtuse järgi.

numbers=[4, -5, 6, -4, -8, 34, 22, -10, 1]

print('Loend:')
print(numbers)

print()
print('Kasvava sorteeritud:')
print(sorted(numbers, key=abs))

print()
print('Kahaneva sorteeritud:')
print(sorted(numbers, key=abs, reverse=True))