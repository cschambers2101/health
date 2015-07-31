__author__ = 'craigchambers'
import bmi as b

height = input('Enter your height in inches')
weight = input('Enter your weight in pounds')

bmi = b.BMI(int(height), int(weight), 'imperial')

print(bmi.__doc__)

print('Your BMI is: {0}'.format(str(bmi.bmi)))
bmi.height = 50
print('Changed height to {}'.format(bmi.height))
bmi.weight = 200
print('Changed weight to {}'.format(bmi.weight))
print('Your BMI is: {0}'.format(str(bmi.bmi)))

