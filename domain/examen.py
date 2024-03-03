'''
Created on 25 ian. 2023

@author: stefa
'''
class examen():
    '''
    un nou tip e data pentru examen
    '''
    def __init__(self, data, ora, materie, tip):
        '''
        initializeaza o noua instanta de examem
        '''
        self.__data = data
        self.__ora = ora
        self.__materie = materie
        self.__tip = tip
    
    def __eq__(self, __o):
        '''
        rescrie functia '==' pentru doua examene
        '''
        return self.__materie == __o.__materie and self.__tip == __o.__tip
    
    def __str__(self):
        '''
        rescrie functia "str" pentru un exmamen
        '''
        return f'{self.__data},{self.__ora},{self.__materie},{self.__tip}'
    
    def getData(self):
        '''
        returneaza data unui examen
        '''
        return self.__data
    
    def getOra(self):
        '''
        returnaza ora unui examen
        '''
        return self.__ora
    
    def getMaterie(self):
        '''
        returneaza materia unui examen
        '''
        return self.__materie
    
    def getTip(self):
        '''
        returneaza tipul unui examen
        '''
        return self.__tip