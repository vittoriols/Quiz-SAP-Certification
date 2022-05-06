import pandas as pd
import os
import sys 
import numpy as np
import math

def trovadati():
    try:
        corrette = pd.read_excel('.\ConfigQuiz.xlsx',sheet_name='DATA')
        corrette.index = np.arange(1, len(corrette) + 1)
        
        dati_input = corrette.copy()
        
        righe = dati_input.shape[0] #numero di righe (domande)
        
        nvuote = dati_input.iloc[:,4:12].isnull().sum(axis=1)
        ndomande = 8 - nvuote
        corrette.fillna('',inplace=True)
        dati_input.fillna('',inplace=True)
        dati_input['COLONNA'] = ndomande
        dati_input.iloc[:]['CORR 1'] = ''
        dati_input.iloc[:]['CORR 2'] = ''
        dati_input.iloc[:]['CORR 3'] = ''
        dati_input.iloc[:]['CORR 4'] = ''
        dati_input.iloc[:]['CORR 5'] = ''
    except:
        pass
    
    # print(corrette.iloc[:,:])
    # print(dati_input.iloc[:,:])
    return corrette, dati_input

def shorten(testolungo):
        l = len(testolungo)
        if l >70:
            if l >150:
                n = math.floor(len(testolungo)/3)
            else:
                n = math.floor(len(testolungo)/2)
        
            c=1    
            for i in range(l):
                if i == n*c:
                    a = i
                    if testolungo[a] == ' ':
                        testolungo = testolungo[:a] + "\n" + testolungo[a+1:]
                        c +=1
                    else:
                        while testolungo[a] != ' ':
                            a -=1
                            if testolungo[a] == ' ':
                                print("sono qui")
                                testolungo = testolungo[:a] + "\n" + testolungo[a+1:]
                                c +=1
                                break
                        
        
        return testolungo 

