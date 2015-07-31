__author__ = 'Craig Chambers'
import bmi, bmr
import person as p


def input_as_integer(value):
    string_input = input(value)
    try:
        return int(string_input)
    except ValueError:
        print('You must input a number')

def convert_pounds_to_kilograms():
    pass

def convert_inches_to_centimetres();
    pass

person = p.Person()
person.sex = input('Enter your sex: ')
person.height = input_as_integer('Enter your height in inches: ')
person.weight = input_as_integer('Enter your weight in pounds: ')
person.age = input_as_integer('Enter your age in years: ')

bmi_result = bmi.BMI(int(person.height), int(person.weight), 'imperial')
bmr_result = bmr.BMR(person.sex, person.weight, person.height, person.age)

#print(bmi.__doc__)

print('Your BMI is: {0}'.format(str(bmi_result.bmi)))
print("You are currently '{}'".format(bmi_result.bmi_as_string))
print('Your BMR is: {}'.format(str(bmr_result.bmr)))
