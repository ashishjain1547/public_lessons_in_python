# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/divisible-or-not-81b86ad7/

n=int(input('Enter the size of input:'))
a=input('Enter the numbers:').split()
if len(a)!=n:
    print('Insufficent input')
    raise Exception
last_digit=int(a[-1][-1])
last_digits = [i[-1] for i in a]
new_number = int(''.join(last_digits))
if new_number%10==0:
    print('Yes')
else:
    print('No')
