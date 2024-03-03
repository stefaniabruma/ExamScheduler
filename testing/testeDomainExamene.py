'''
Created on 25 ian. 2023

@author: stefa
'''
import unittest
from domain.examen import examen

class TestCaseDomainExamene(unittest.TestCase):
    '''
    un nou tip de data pentru testele domeniului de examene
    '''
    def setUp(self):
        '''
        setUp ul realizat inaintea fiecarei procedui de testare a dopmeniului de examene
        '''
        self.__exm = examen('25.01', '11:00', 'FP', 'normal')
    
    def testeGettere(self):
        '''
        testeaza getterele domaeniului de examene
        '''
        self.assertEqual(self.__exm.getData(), '25.01')
        self.assertEqual(self.__exm.getOra(), '11:00')
        self.assertEqual(self.__exm.getMaterie(), 'FP')
        self.assertEqual(self.__exm.getTip(), 'normal')
        

if __name__ == '__main__':
    unittest.main()