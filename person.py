__author__ = 'Craig Chambers'


class Person:
    '''
    Defines a person

    Collates all the information on a person including their sex, height, weight and age
    '''
    def __init__(self):
        '''
        :param self.__sex: sex of the person
        :param self.__height: height of the person
        :param self.__weight: weight of the person
        :param self.__age: age of the person
        :return: none
        '''
        self.__sex = ''
        self.__height = 0
        self.__weight = 0
        self.__age = 0

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, value):
        if value == 'm' or value == 'male':
            self.__sex = 'male'
        elif value == 'f' or value == 'female':
            self.__sex = 'female'
        else:
            raise ValueError(value + ' is not a valid sex')

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value > 0:
            self.__height = value
        else:
            raise ValueError('Height must be greater than 0')

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('Weight must be greater than 0')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):

        self.__age = value



