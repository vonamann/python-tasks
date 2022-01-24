number = int(input())

if number > 1000000000:
  print('Number is too big')
else:
  result = 0
  rem    = 0 # Remainder
  for i in range(10):
    rem    = number % 10
    number = number // 10
    result += rem
  print('Sum of number’s digits is: ' + str(result))
