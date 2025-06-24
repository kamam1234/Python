def calculate_sum(one, two, three, four):
  sum = (one*2) + (two*2) + (three*3) + (four+4)
  return sum
one = int(input('Enter the first number: '))
two = int(input('Enter the second number: '))
three = int(input('Enter the third number: '))
four = int(input('Enter the fourth number: '))
result = calculate_sum(one, two, three, four)
print(result)