__author__ = 'Craig Chambers'


class BMI:
    '''
    Calculates BMI values for a given weight and height

    Defaults to:
     height=0
     weight=0
     measurement = 'imperial'
    '''

    def __init__(self, height=0, weight=0, measurement='imperial'):
        '''
        Initiates the class with height, weight and the measurement used
        :param height: height of the person in inches oe meters
        :param weight: weight of the person in pounds or kilograms
        :param measurement: imperial or metric
        :return: none
        '''
        self._measurement = measurement
        self._height = height
        self._weight = weight
        self._bmi = 0

        if self._measurement == 'imperial':
            self.calc_imperial_bmi(self._height,self._weight)
        elif self._measurement == 'metric':
            self.calc_metric_bmi(self._height, self._weight)
        else:
            raise ValueError('Measurement was not "imperial" or "metric"', self._measurement)

    @property
    def height(self):
        '''
        Height property (used to calculate bmi)

        :return: height
        '''
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def weight(self):
        '''
        Height property (used to calculate bmi)

        :return: weight
        '''
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value
        self.which_calculation()

    @property
    def bmi(self):
        '''
        Calculated bmi value as an integer
        :return: bmi
        '''
        return int(self._bmi)

    @bmi.setter
    def bmi(self, value):
        self._bmi = value
        self.which_calculation()

    @property
    def bmi_as_string(self):
        '''
        Property that shows the bmi property as a string

        :return: bmi as a string (underweight, healthy, overweight, obese, extremely obese)
        '''
        bmi_string=''
        if self._bmi < 19:
            bmi_string='Underweight'
        elif self._bmi >= 19 and self._bmi < 25:
            bmi_string='Healthy'
        elif self._bmi >= 25 and self._bmi < 30:
            bmi_string='Overweight'
        elif self._bmi >= 30 and self._bmi < 40:
            bmi_string='Obese'
        elif self._bmi >= 40:
            bmi_string='Extremely Obese'
        else:
            raise ValueError('Unable to calculate string version of bmi', bmi_string)
        return bmi_string


    def which_calculation(self):
        '''
        Calls relevant function to calculate bmi based on value in self._measurement (defaults to 'imperial')

        :return: none
        '''
        if self._measurement == 'imperial':
            self.calc_imperial_bmi(self._height, self._weight)
        elif self._measurement == 'metric':
            self.calc_metric_bmi(self._height, self._weight)
        else:
            raise ValueError('Measurement was not "imperial" or "metric"', self._measurement)

    def calc_imperial_bmi(self, the_height, the_weight):
        '''
        Calculates BMI in Imperial measurements

        English BMI Formula
            BMI = ( Weight in Pounds / ( Height in inches x Height in inches ) ) x 703
        :param the_height: height in inches
        :param the_weight: weight in pounds
        :return none
        '''
        self._bmi = the_weight/(the_height*the_height) * 703

    def calc_metric_bmi(self, the_height, the_weight):
        '''
        Calculates BMI in metric measurements

        Metric BMI Formula
            BMI = ( Weight in Kilograms / ( Height in Meters x Height in Meters ) )
        :param the_height: height in meters
        :param the_weight: weight in kilograms
        :return none
        '''
        self._bmi = the_weight/(the_height*the_height)
