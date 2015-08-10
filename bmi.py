__author__ = 'Craig Chambers'


class BMI:
    """
    Calculates BMI values for a given weight and height.

    Defaults to:
     height=0
     weight=0
     measurement = 'imperial'
    """

    def __init__(self, height=0, weight=0, measurement='imperial'):
        """
        Initiates the class with height, weight and the measurement used.
        
        :param height: height of the person in inches or meters
        :param weight: weight of the person in pounds or kilograms
        :param measurement: imperial or metric
        :return: none
        """
        self.__measrement = measurement
        self.__height = height
        self.__weight = weight
        self.__bmi = 0

        if self.__measrement == 'imperial':
            self.__calc_imperial_bmi(self.__height,self.__weight)
        elif self.__measrement == 'metric':
            self.__calc_metric_bmi(self.__height, self.__weight)
        else:
            raise ValueError('Measurement was not "imperial" or "metric"', self.__measrement)

    @property
    def height(self):
        """
        Height property (used to calculate bmi).

        :return: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def weight(self):
        """
        Height property (used to calculate bmi).

        :return: weight
        """
        return self.__weight

    @weight.setter
    def weight(self, value):
        self.__weight = value
        self.__which_calculation()

    @property
    def bmi(self):
        """
        Calculated bmi value as an integer.
        
        :return: bmi
        """
        return int(self.__bmi)

    @bmi.setter
    def bmi(self, value):
        self.__bmi = value
        self.__which_calculation()

    @property
    def bmi_as_string(self):
        """
        Property that shows the bmi property as a string.

        :return: bmi as a string (underweight, healthy, overweight, obese, extremely obese)
        """
        bmi_string=''
        if self.__bmi < 19:
            bmi_string='Underweight'
        elif self.__bmi >= 19 and self.__bmi <= 24:
            bmi_string='Healthy'
        elif self.__bmi >= 25 and self.__bmi <= 29:
            bmi_string='Overweight'
        elif self.__bmi >= 30 and self.__bmi <= 39:
            bmi_string='Obese'
        elif self.__bmi >= 40:
            bmi_string='Extremely Obese'
        else:
            raise ValueError('Unable to calculate string version of bmi', bmi_string)
        return bmi_string

    def __which_calculation(self):
        """
        Calls relevant function to calculate bmi based on value in self.__measrement (defaults to 'imperial').

        :return: none
        """
        if self.__measrement == 'imperial':
            self.__calc_imperial_bmi(self.__height, self.__weight)
        elif self.__measrement == 'metric':
            self.__calc_metric_bmi(self.__height, self.__weight)
        else:
            raise ValueError('Measurement was not "imperial" or "metric"', self.__measrement)

    def __calc_imperial_bmi(self, the__height, the__weight):
        """
        Calculates BMI in Imperial measurements.

        English BMI Formula
            BMI = ( Weight in Pounds / ( Height in inches x Height in inches ) ) x 703
        :param the__height: height in inches
        :param the__weight: weight in pounds
        :return none
        """
        self.__bmi = the__weight/(the__height*the__height) * 703

    def __calc_metric_bmi(self, the__height, the__weight):
        """
        Calculates BMI in metric measurements.

        Metric BMI Formula
            BMI = ( Weight in Kilograms / ( Height in Meters x Height in Meters ) )
        :param the__height: height in meters
        :param the__weight: weight in kilograms
        :return none
        """
        self.__bmi = the__weight/(the__height*the__height)