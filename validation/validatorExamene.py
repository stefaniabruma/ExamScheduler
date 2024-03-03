'''
Created on 25 ian. 2023

@author: stefa
'''
from errors.validationError import ValidationError
class validatorExm:
    '''
    un nou tip de data pentru validatorul de examene
    '''
    def valideaza(self, exm):
        '''
        verifica daca exmaneul exm este valid
        data - format dd.MM
        ora - format hh:mm
        materie - orice
        tip - in multimea {normal,restanta}
        '''
        errors = ''
        
        if exm.getData()[2]== '.':
            parts = exm.getData().split('.')
            ziua = parts[0]
            luna = parts[1]
            if luna in ['01','03','05','07','08','10', '12'] and int(ziua) > 31:
                errors += 'Data invalida\n'
            elif luna in ['04', '06', '09', '11'] and int(ziua) > 30:
                errors += 'Data invalida\n'
            elif luna == '02' and int(ziua) > 29:
                errors += 'Data invalida\n'
            elif luna not in ['01','02','03','05','07','08','10', '12', '04', '06', '09', '11']:
                errors += 'Data invalida\n'
                
        else:
            errors += 'Data invalida\n'
            
        if exm.getOra()[2]==':':
            parts = exm.getOra().split(':')
            ora = parts[0]
            minut = parts[1]
            if int(ora) > 23 or int(minut) >59:
                errors += 'Ora invalida!\n'
                
        else:
            errors += 'Ora invalida!\n'
        
        if exm.getTip() not in ['normal', 'restanta']:
            errors += 'Tip invalid!\n'
            
        if len(errors) > 0:
            raise ValidationError(errors)