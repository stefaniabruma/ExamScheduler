'''
Created on 25 ian. 2023

@author: stefa
'''
from domain.examen import examen
from errors.repoError import RepositoryError
class repoExm:
    '''
    un nou tip de data pentru repository-ul de exmamene
    '''
    def __init__(self, cale):
        '''
        initializeaza o nou instanta de reposiotry de examene
        '''
        self.__examene = []
        self.__cale = cale
        
    def __readAll(self):
        '''
        citeste examenele din fisierul self.__cale
        '''
        with open(self.__cale, 'r') as f:
            lines = f.readlines()
            self.__examene.clear()
            for line in lines:
                line = line.strip()
                if line!='':
                    parts = line.split(',')
                    data = parts[0]
                    ora = parts[1]
                    materie = parts[2]
                    tip = parts[3]
                    exm = examen(data,ora,materie,tip)
                    self.__examene.append(exm)
                    
    def __writeAll(self):
        '''
        scrie toate examenel in fisier
        '''
        with open(self.__cale,'w') as f:
            for exm in self.__examene:
                f.write(str(exm)+'\n')
                
    def lungime(self):
        '''
        returneaza numarul de examene inregistrate
        '''
        self.__readAll()
        return len(self.__examene)
    
    def getAll(self):
        '''
        returneaza toate examenele
        '''
        self.__readAll()
        return self.__examene
    
    def adaugaExm(self, exm):
        '''
        adauga un examen in lista de examene
        '''
        self.__readAll()
        if exm in self.__examene:
            raise RepositoryError('Examen existent!\n')
        self.__examene.append(exm)
        self.__writeAll()