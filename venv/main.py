'''
Created on 25 ian. 2023

@author: stefa
'''
from infrastructure.repositoryExamene import repoExm
from presentation.ui import userInterface
from testing.testeDomainExamene import TestCaseDomainExamene
from testing.testeRepositoryExamene import TestCaseRepositoryExamene
from testing.testeServiceExamene import TestCaseServiceExamene
from testing.testevalidator import TestCaseTesteValidator

if __name__ == '__main__':
    repoExamene = repoExm('examene.txt')
    ui = userInterface(repoExamene)
    ui.printExamUrmatoare()
    while True:
        ui.printMenu()
        cmd = ui.getComanda()
        ui.executa(cmd)
