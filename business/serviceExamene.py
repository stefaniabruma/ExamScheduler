'''
Created on 25 ian. 2023

@author: stefa
'''
from validation.validatorExamene import validatorExm
from domain.examen import examen
from _datetime import date

class serviceExm:
    '''
    un nou tip de data pentru service-ul de examene
    '''
    def __init__(self, repoExamene):
        '''
        initializeaza o noua instanta de service de examene
        '''
        self.__repo = repoExamene
        self.__validator = validatorExm()
        self.__data = ''
        
    def adauga_examen(self, data, ora, materie, tip):
        '''
        adauga un nou examen
        '''
        exm = examen(data,ora,materie,tip)
        self.__validator.valideaza(exm)
        self.__repo.adaugaExm(exm)
    
    def examene_urmatoare(self):
        '''
        returneaza lista cu examenele din ziua urmatoare
        '''
        azi = date.today()
        parts = str(azi).split('-')
        
        zi = parts[2]
        luna = parts[1]
        data = zi + '.' + luna
        maine = self.calculeazaZiuaUrm(data)
        
        examene = []
        for exm in self.__repo.getAll():
            if exm.getData() == maine:
                examene.append(exm)
                
        examene.sort(key = lambda x: x.getOra())
        return examene
    
    def exameneUrmTreiZile(self):
        '''
        returneaza examenele programate in rumatoarele 3 zile
        '''
        if self.__data == '':
            return []
        
        data = self.__data
        examene = []
        
        for exm in self.__repo.getAll():
            if exm.getData() == data:
                examene.append([exm.getData(), exm.getOra(), exm.getMaterie(), exm.getTip()])
        
        data = self.calculeazaZiuaUrm(data)
        for exm in self.__repo.getAll():
            if exm.getData() == data:
                examene.append([exm.getData(), exm.getOra(), exm.getMaterie(), exm.getTip()])
                
        data = self.calculeazaZiuaUrm(data)
        for exm in self.__repo.getAll():
            if exm.getData() == data:
                examene.append([exm.getData(), exm.getOra(), exm.getMaterie(), exm.getTip()])
        
        return examene
    
    def schimbaData(self, dataN):
        '''
        schimba data dupa care se afiseaza exam din urm 3 zile
        '''
        self.__data = dataN
        
    def calculeazaZiuaUrm(self, data):
        '''
        calculeaza urmatoarea zi dupa o zi data data
        '''
        parts = data.split('.')
        ziua = int(parts[0])
        luna = int(parts[1])
        
        if luna in [1,3,5,7,8,10,12] and ziua == 31:
                ziua = 1
                luna += 1
        
        elif luna in [4,6,6,9,11] and ziua == 30:
            ziua = 1
            luna += 1
        
        elif luna == 2 and ziua == 29:
            ziua = 1
            luna += 1
        
        else:
            ziua += 1
            
        format = ''
        if ziua <= 9:
            format += '0'+str(ziua)
        else:
            format += str(ziua)
        
        format += '.'
        
        if luna <= 9:
            format += '0'+str(luna)
        else:
            format += str(luna)
            
        return format
    
    def getDataSetata(self):
        '''
        returneaza data setata de utilizator
        '''
        return self.__data
    
    def exameneAnumitSir(self, sir):
        '''
        returneaza examenele ale caror materie contine un anumit sir, ordonate dupa data si ora
        '''
        examene = []
        for exm in self.__repo.getAll():
            if sir in exm.getMaterie():
                examene.append(exm)
        examene.sort(key = lambda x: x.getData())
        
        sorted = False
        while not sorted:
            sorted = True
            for contor in range(len(examene)-1):
                if examene[contor].getData() == examene[contor].getData():
                    if examene[contor].getOra() > examene[contor+1].getOra():
                        examene[contor],examene[contor+1] = examene[contor+1],examene[contor]
                        sorted = False
                    
        return examene
                    