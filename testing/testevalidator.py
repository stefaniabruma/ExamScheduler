'''
Created on 25 ian. 2023

@author: stefa
'''
import unittest
from validation.validatorExamene import validatorExm
from errors.validationError import ValidationError
from domain.examen import examen
class TestCaseTesteValidator(unittest.TestCase):
    '''
    un nou tip data pentru testele validatorului de examene
    '''
    def setUp(self):
        '''
        setUp realizat inaintea fiecarei proceduri de testare a validatorlui de examene
        '''
        self.__valid = validatorExm()
        
    def testeValideaza(self):
        '''
        testeaza functionalitatea de validare a validatorlui de examene
        '''
        self.assertRaises(ValidationError, self.__valid.valideaza,examen('0702', '11:00', 'ASC', 'normal'))
        self.assertRaises(ValidationError, self.__valid.valideaza,examen('31:04', '11:00', 'ASC', 'normal'))
        self.assertRaises(ValidationError, self.__valid.valideaza,examen('32:01', '11:00', 'ASC', 'normal'))
        self.assertRaises(ValidationError, self.__valid.valideaza,examen('30:02', '11:00', 'ASC', 'normal'))
        self.assertRaises(ValidationError, self.__valid.valideaza,examen('67:02', '11:00', 'ASC', 'normal'))
        self.assertRaises(ValidationError, self.__valid.valideaza,examen('07:02', '1100', 'ASC', 'normal'))
        self.assertRaises(ValidationError, self.__valid.valideaza,examen('07:02', '30:00', 'ASC', 'normal'))
        self.assertRaises(ValidationError, self.__valid.valideaza,examen('07:02', '11:62', 'ASC', 'normal'))
        self.assertRaises(ValidationError, self.__valid.valideaza,examen('07:02', '11:00', 'ASC', 'invalid'))
        
        self.__valid.valideaza(examen('07.02', '11:00', 'ASC', 'normal'))
        
if __name__ == '__main__':
    unittest.main()