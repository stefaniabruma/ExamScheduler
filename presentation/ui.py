'''
Created on 25 ian. 2023

@author: stefa
'''
from business.serviceExamene import serviceExm
from errors.validationError import ValidationError
from errors.repoError import RepositoryError
class userInterface:
    '''
    un nou tip de data pentru interfata utilizator 
    '''
    def __init__(self, repoExamene):
        '''
        initializeaza o nou interfata utilizator
        '''
        self.__service = serviceExm(repoExamene)
        
    def printMenu(self):    
        '''
        printeaza meniul utilizatorului
        '''
        print('Adaugare examen - 1')
        print('Setati data pentru care doriti sa vedeti examenele programate in urmatoarele 3 zile - 2')
        print('Exportati in fisierul dorit examenele care contin in materie un anumit sir de caractere - 3')
        
    def getComanda(self):
        '''
        preia comanda de la utilizator
        '''
        cmd = input('Introduceti comanda: ')
        return cmd
    
    def executa(self, cmd):
        '''
        executa comanda data de utilizator
        '''
        
        if cmd == '1':
            self.adaugareExm()
        
        if cmd == '2':
            self.seteazaData()
        
        if cmd == '3':
            self.exportaFisier()
            
    def printExamUrmatoare(self):
        '''
        printeaza examenele ce au loc maine
        '''
        examene = self.__service.examene_urmatoare()
        
        for exm in examene:
            print(exm)
    
    def adaugareExm(self):
        '''
        introduce un nou examen
        '''
        data = input('Introduceti data examenului: ')
        ora = input('Introduceti ora examenului: ')
        materie = input('Introduceti materia examenului: ')
        tip = input('Introduceti tipul exmanelui: ')
        
        errors = ''
        try:
            self.__service.adauga_examen(data, ora, materie, tip)
        except ValidationError as ve:
            errors += str(ve)
        except RepositoryError as re:
            errors += str(re)
        
        if len(errors) > 0:
            print(errors)
            return 
    
        print('Examen adaugat cu succes!\n')
        self.printTabel()
    
    def printTabel(self):
        '''
        printeaza tabelul cu examenele ce urmeaza sa aiba loc in urmatoarele 3 zile de la data setata
        '''
        examene = self.__service.exameneUrmTreiZile()
        
        print('Examenele ce urmeaza sa aiba loc in urmatoerele trei zile de la data ', self.__service.getDataSetata(), ' sunt: ')
        print('Data'.ljust(10), 'Ora'.ljust(10), 'Materia'.ljust(10), 'Tipul'.ljust(10))
        
        for exm in examene:
            print(exm[0].ljust(10), exm[1].ljust(10), exm[2].ljust(10), exm[3].ljust(10))
            
    def seteazaData(self):
        '''
        permite utilizatorlui sa seteze o data pentru a vedea examenele din urmatoarele 3 zile
        '''
        data = input('Introduceti data pentru care doriti sa vedeti examenele programate in urmatoarele 3 zile: ')
        
        self.__service.schimbaData(data)
        
        self.printTabel()
        
    def exportaFisier(self):
        '''
        exporta in fisierul dat de utilizator examenele care contin sirul dat de utilizator sortate dupa data si ora
        '''
        cale = input('Introduceti fisierul: ')
        sir = input('Introduceti sirul de caractere: ')
        examene = self.__service.exameneAnumitSir(sir)
        
        with open(cale,'w+') as f:
            for exm in examene:
                f.write(str(exm)+'\n')
        
        self.printTabel()