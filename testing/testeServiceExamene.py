'''
Created on 25 ian. 2023

@author: stefa
'''
import unittest
from infrastructure.repositoryExamene import repoExm
from business.serviceExamene import serviceExm
from errors.validationError import ValidationError
from domain.examen import examen

class TestCaseServiceExamene(unittest.TestCase):
    '''
    un nou tip de data pentru testele service-ului de examene
    '''
    def setUp(self):
        '''
        setUp-ul realizat inaintea fiecarei proceduri de testare a service-ului de examene
        '''
        self.__cale = 'testeExamene.txt'
        self.golesteFisier()
        self.__repo = repoExm('testeExamene.txt')
        self.__service = serviceExm(self.__repo)
        self.__service.adauga_examen('25.01', '11:10', 'FP', 'normal')
    
    def golesteFisier(self):
        '''
        goleste fisierul self.__cale
        '''
        with open(self.__cale,'w') as f:
            f.write('')
            
    def __readALL(self):
        '''
        citeste toate examenele din fisierul self.__cale
        '''
        examene = []
        with open(self.__cale, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line!='':
                    parts = line.split(',')
                    data = parts[0]
                    ora = parts[1]
                    materie = parts[2]
                    tip = parts[3]
                    exm = examen(data,ora,materie,tip)
                    examene.append(exm)
        return examene
        
    def testeAdaugare(self):
        '''
        ruleaza testele pentru functionalitatea de adaugare a service-ului de examene
        '''
        self.assertRaises(ValidationError, self.__service.adauga_examen,'0702', '11:00', 'ASC', 'normal')
        self.assertRaises(ValidationError, self.__service.adauga_examen,'31:04', '11:00', 'ASC', 'normal')
        self.assertRaises(ValidationError, self.__service.adauga_examen,'32:01', '11:00', 'ASC', 'normal')
        self.assertRaises(ValidationError, self.__service.adauga_examen,'30:02', '11:00', 'ASC', 'normal')
        self.assertRaises(ValidationError, self.__service.adauga_examen,'67:02', '11:00', 'ASC', 'normal')
        self.assertRaises(ValidationError, self.__service.adauga_examen,'07:02', '1100', 'ASC', 'normal')
        self.assertRaises(ValidationError, self.__service.adauga_examen,'07:02', '30:00', 'ASC', 'normal')
        self.assertRaises(ValidationError, self.__service.adauga_examen,'07:02', '11:62', 'ASC', 'normal')
        self.assertRaises(ValidationError, self.__service.adauga_examen,'07:02', '11:00', 'ASC', 'invalid')
        
        
        self.__service.adauga_examen('07.02', '11:00', 'ASC', 'normal')
        self.assertEqual(self.__readALL()[1], examen('07.02', '11:00', 'ASC', 'normal'))
        
    def testeCalculeazaZiuaUrm(self):
        '''
        testeaza functionalitatea de a calcula ziua urmatoare pe baza unui sir ce respecta formatul din cerinta
        '''
        self.assertEqual(self.__service.calculeazaZiuaUrm('25.01'), '26.01')
        self.assertEqual(self.__service.calculeazaZiuaUrm('31.10'), '01.11')
        self.assertEqual(self.__service.calculeazaZiuaUrm('30.04'), '01.05')
        self.assertEqual(self.__service.calculeazaZiuaUrm('29.02'), '01.03')
        self.assertEqual(self.__service.calculeazaZiuaUrm('25.01'), '26.01')
    
    def testeExameneUrm(self):
        '''
        testeaza functionalitatea de determinare a examenelor ce vor avea loc maine a service-ului de examene
        '''
        self.assertEqual(self.__service.examene_urmatoare(), [])
        self.__service.adauga_examen('26.01', '11:00', 'ASC', 'normal')
        self.__service.adauga_examen('02.02', '12:00', 'FP', 'restanta')
        self.__service.adauga_examen('26.01', '09:00', 'Logica', 'restanta')
        self.assertEqual(self.__service.examene_urmatoare(), [examen('26.01', '09:00', 'Logica', 'restanta'),examen('26.01', '11:00', 'ASC', 'normal')])
        
    def testeExameneUrmTreiZile(self):
        '''
        testeaza functionalitatea de determinare a examenelor ce vor avea loc in urm 3 zile
        '''
        
        self.__service.schimbaData('25.01')
        self.assertEqual(self.__service.exameneUrmTreiZile(), [['25.01', '11:10', 'FP', 'normal']])
        
        self.__service.adauga_examen('26.01', '11:00', 'ASC', 'normal')
        self.__service.adauga_examen('02.02', '12:00', 'FP', 'restanta')
        self.__service.adauga_examen('26.01', '09:00', 'Logica', 'restanta')
        
        self.assertEqual(self.__service.exameneUrmTreiZile(),[['25.01', '11:10', 'FP', 'normal'], ['26.01', '11:00', 'ASC', 'normal'], ['26.01', '09:00', 'Logica', 'restanta']])  
    
    def testeDataStata(self):
        '''
        ruleaza testele pentru a seta data pentru tabel si pentru getterul sau
        '''
        self.assertEqual(self.__service.getDataSetata(), '')
        self.__service.schimbaData('25.01')
        self.assertEqual(self.__service.getDataSetata(), '25.01') 
    
    def testeExameneAnumitSir(self):
        '''
        testeaza functionalitatea de a da examenele care contin in numele materiei lor un anumit sir, ordonate crescator dupa data si ora
        '''
        self.__service.adauga_examen('26.01', '11:00', 'ASC', 'normal')
        self.__service.adauga_examen('02.02', '12:00', 'Fundamentele programarii', 'restanta')
        self.__service.adauga_examen('26.01', '09:00', 'Logica', 'restanta')
        
        self.assertEqual(self.__service.exameneAnumitSir('a'), [examen('26.01', '09:00', 'Logica', 'restanta'), examen('02.02', '12:00', 'Fundamentele programarii', 'restanta')])
        self.assertEqual(self.__service.exameneAnumitSir('z'), []) 
if __name__ == '__main__':
    unittest.main()