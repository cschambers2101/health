__author__ = 'craigchambers'
import bmi as b

height = input('Enter your height in inches')
weight = input('Enter your weight in pounds')

bmi = b.BMI(int(height), int(weight), 'imperial')
print('Your BMI is: {0}'.format(str(bmi.bmi)))
