__author__ = 'Craig Chambers'


class BMR:
    """
    Calculates Basal Metabolic rate (BMR).

    For men: BMR = 10 x weight (kg) + 6.25 x height (cm) – 5 x age (years) + 5
    For women: BMR = 10 x weight (kg) + 6.25 x height (cm) – 5 x age (years) – 161

    """
    def __init__(self, sex, weight, height, age):
      """
      Initialises person with all variables.
        
      :param sex: Sex of person (male or female)
      :param weight:  Weight of person
      :param height: Height of person
      :param age:  Age of person
      :return: none
      """
      self.__sex = sex
      self.__weight = weight
      self.__height = height
      self.__age = age
      self.__bmr = 0
      self.__hbe = ''
      self.__calc_bmr(self.__sex, self.__weight, self.__height, self.__age)
      self.__calc_hbe(self.__bmr)

    @property
    def bmr(self):
      return self.__bmr

    @bmr.setter
    def bmr(self, value):
      self.__bmr = value
        
    @property
    def hbe(self):
      return self.__hbe
      
    @hbe.setter
    def hbe(self, value):
      self.__hbe = value

    def __calc_bmr(self, sex, weight, height, age):
      """
      Calculates BMR for given sex, weight, height and age.

      :param sex: sex of person (male or female)
      :param weight: weight of person in kilograms
      :param height: height of person in centimetres
      :param age: age of person in years (integer)
      :return: none
      """
      if sex == 'male':
        self.__bmr = 10 * weight + 6.25 * height - 5 * age + 5
      elif sex == 'female':
        self.__bmr = 10 * weight + 6.25 * height - 5 * age - 161
      else:
        raise ValueError('Incorrect parameters')

    def __calc_hbe(self, bmr):
      """
      Calculates the Harris Benedict Equation from your BMR
      
      :param bmr: Your BMR value
      :return: none
      """
      hbe = ''
      hbe += 'Harris Benedict score: \n'
      hbe += 'Sedentary: {}'.format(str(int(bmr*1.2))) + '\n'
      hbe += 'Lightly active: {}'.format(str(int(bmr*1.375))) + '\n'
      hbe += 'Moderately active: {}'.format(str(int(bmr*1.55))) + '\n'
      hbe += 'Very active: {}'.format(str(int(bmr*1.725))) + '\n'
      hbe += 'Extra active: {}'.format(str(int(bmr*1.9))) + '\n'
      self.__hbe = hbe
      
    

