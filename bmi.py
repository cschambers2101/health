__author__ = 'craigchambers'

class BMI:
    '''
    Calculates BMI values for a given weight and height
    '''

    def __init__(self, height, weight, measurement):
        '''
        Initiates the class with height, weight and the measurement used
        :param height: height of the person in inches oe meters
        :param weight: weight of the person in pounds or kilograms
        :param measurement: imperial or metric
        :return: none
        '''
        self.measurement = measurement
        self.height = height
        self.weight = weight
        self.bmi = 0

        if self.measurement == 'imperial':
            self.bmi = self.calcImperialBMI(self.height,self.weight)
        elif self.measurement == 'metric':
            self.bmi = self.calcMetricBMI(self.height, self.weight)
        else:
            raise ValueError('Measurement was not "imperial" or "metric"', self.measurement)


    def calcImperialBMI(self, height, weight):
        '''
        Calculates BMI in Imperial measurements
        English BMI Formula
            BMI = ( Weight in Pounds / ( Height in inches x Height in inches ) ) x 703
        :param height: height in inches
        :param weight: weight in pounds
        :return: BMI value
        '''
        return (weight/(height*height))* 703

    def calcMetricBMI(self, height, weight):
        '''
        Calculates BMI in metric measurements
        Metric BMI Formula
            BMI = ( Weight in Kilograms / ( Height in Meters x Height in Meters ) )
        :param height: height in meters
        :param weight: weight in kilograms
        :return: BMI value
        '''
        return (weight/(height*height))