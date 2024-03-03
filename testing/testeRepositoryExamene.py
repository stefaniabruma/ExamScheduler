'''
Created on 25 ian. 2023

@author: stefa
'''
import unittest
from infrastructure.repositoryExamene import repoExm
from domain.examen import examen
from errors.repoError import RepositoryError
class TestCaseRepositoryExamene(unittest.TestCase):
    '''
    un nou tip de data pentru testele repository-ului de examene
    '''
    def setUp(self):
        '''
        setUp-ul realizat inaintea fiecarei proceduri de testare a repository-ului de examene
        '''
        self.__cale = 'testeExamene.txt'
        self.golesteFisier()
        self.__repo = repoExm(self.__cale)
        exm = examen('25.01', '11:00', 'FP', 'normal')
        self.__repo.adaugaExm(exm)
        
    def golesteFisier(self):
        '''
        goleste fisierul self.__cale
        '''
        with open(self.__cale,'w') as f:
            f.write('')
            
    def testeLungime(self):
        '''
        testele functionalitatii lungime a repo-ului de examene
        '''
        self.assertEqual(self.__repo.lungime(), 1)
        
    def testeGetALL(self):
        '''
        testeaza functionalitatea getAll a repoului de examene
        '''
        self.assertEqual(self.__repo.getAll(), [examen('25.01', '11:00', 'FP', 'normal')])
        
    def testeAdaugre(self):
        '''
        testeaza functionalitatea de adaugare a rpeo-ului de examene
        '''
        self.__repo.adaugaExm(examen('07.02', '09:00', 'ASC', 'normal'))
        self.assertEqual(self.__repo.lungime(), 2)
        self.assertRaises(RepositoryError, self.__repo.adaugaExm, examen('27.01', '11:00', 'FP', 'normal'))

if __name__ == '__main__':
    unittest.main()