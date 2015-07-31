__author__ = 'Craig Chambers'
import bmi as b

height = input('Enter your height in inches: ')
weight = input('Enter your weight in pounds: ')

bmi = b.BMI(int(height), int(weight), 'imperial')

#print(bmi.__doc__)

print('Your BMI is: {0}'.format(str(bmi.bmi)))
print("You are currently '{}'".format(bmi.bmi_as_string))
