# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PROVATEST.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import subprocess
from datetime import date,datetime
import pandas as pd
import numpy as np
import webbrowser
from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox 
from PyQt5.QtCore import QRect, QPropertyAnimation  
import group_rc
import addonsfunctions as af
from ui_main import Ui_MainWindow
calcolo= 0

 ###############  CLASSE CUSTOM  ###############################################################

class MyWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dragPos = QtCore.QPoint()
        self.calcolo = 0
        self.risultato = 0
        # Create a key group and add keys
        self.decision = 0
        self.btn_grp = QButtonGroup()
        self.btn_grp.setExclusive(True)
        self.btn_grp.addButton(self.module0)
        self.btn_grp.addButton(self.registro)
        self.btn_grp.addButton(self.moduletest)
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.closebutton.clicked.connect(lambda:self.close())
        self.minimizebutton.clicked.connect(lambda:self.showMinimized())
        self.maximizebutton.clicked.connect(self.minmax)
        self.testbutton.clicked.connect(self.slidemenu)
        self.moduletest.clicked.connect(self.slidemenuvertical)
        self.module0.clicked.connect(lambda: self.gen.setCurrentWidget(self.home))
        self.module0.clicked.connect(self.halfvertical)
        self.module0.clicked.connect(self.check_account)
        self.module1.clicked.connect(lambda: self.gen.setCurrentWidget(self.start))
        self.module1.clicked.connect(lambda: self.label_4.setText("Test Cut Score: 80%"))
        self.module2.clicked.connect(lambda: self.gen.setCurrentWidget(self.start))
        self.module2.clicked.connect(lambda: self.label_4.setText("Test Cut Score: 80%"))
        self.module3.clicked.connect(lambda: self.gen.setCurrentWidget(self.start))
        self.module3.clicked.connect(lambda: self.label_4.setText("Test Cut Score: 80%"))
        self.module4.clicked.connect(lambda: self.gen.setCurrentWidget(self.start))
        self.module4.clicked.connect(lambda: self.label_4.setText("Test Cut Score: 80%"))
        self.module5.clicked.connect(lambda: self.gen.setCurrentWidget(self.start))
        self.module5.clicked.connect(lambda: self.label_4.setText("Test Cut Score: 80%"))
        self.module6.clicked.connect(lambda: self.gen.setCurrentWidget(self.start))
        self.module6.clicked.connect(lambda: self.label_4.setText("Test Cut Score: 80%"))
        self.module7.clicked.connect(lambda: self.gen.setCurrentWidget(self.start))
        self.module7.clicked.connect(lambda: self.label_4.setText("Test Cut Score: 80%"))
        self.modulemix.clicked.connect(lambda: self.gen.setCurrentWidget(self.start))
        self.modulemix.clicked.connect(lambda: self.label_4.setText("Test Cut Score: "+ self.lineEdit_6.text()))
        self.buttonstart.clicked.connect(lambda: self.gen.setCurrentWidget(self.page1))
        self.buttonstart.clicked.connect(lambda: self.sfondotasti.hide())
        self.buttonstart.clicked.connect(self.resetprova)
        self.tryagain.clicked.connect(lambda: self.gen.setCurrentWidget(self.page1))
        self.tryagain.clicked.connect(lambda: self.sfondotasti.hide())
        self.tryagain.clicked.connect(self.resetprova)
        self.avanti.clicked.connect(self.incrementi)
        self.indietro.clicked.connect(self.decrementi)
        self.conf.clicked.connect(self.popup)
        self.pushButton_2.clicked.connect(self.popup_save)
        self.registro.clicked.connect(lambda: self.gen.setCurrentWidget(self.regis))
        self.registro.clicked.connect(self.halfvertical)
        self.registro.clicked.connect(self.mostratabella)
        self.Moduli.hide()
        self.Questions.hide()
        self.CutScore.hide()
        self.LearningHub.hide()
        self.frame_17.hide()
        self.moduletest.hide()
        self.module1.hide()
        self.module2.hide()
        self.module3.hide()
        self.module4.hide()
        self.module5.hide()
        self.module6.hide()
        self.module7.hide()
        self.modulemix.hide()
        self.linkbutton.clicked.connect(self.web_browser)
        self.linkbutton.hide()
        self.empty.clicked.connect(self.emptyregis)
        self.Tabella.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.download.clicked.connect(self.getSaveFileName)
        self.pushButton.clicked.connect(self.guida)
        
        
        #### aggiungo righe nella tabella del registro
        self.offset = None
        self.frame_5.installEventFilter(self)
        self.statusBar.setFixedHeight(10)
        
        #### PROVA A LEGGERE IL FILE ACCOUNT.XLSX
        try: 
                self.account = account
                self.lineEdit.setText(str(self.account.iloc[0,0]))
                self.lineEdit_2.setText(str(self.account.iloc[0,1]))
                self.lineEdit_3.setText(str(self.account.iloc[0,2]))
                self.comboBox.setCurrentIndex(int(self.account.iloc[0,3]))
                self.hidemine()
        except:
                pass
        
        self.comboBox.currentIndexChanged['int'].connect(self.hidemine)
    
    def emptyregis(self):
        msg = QMessageBox()
        msg.setWindowTitle("Cancellazione Registro")
        msg.setText("Sei sicuro di voler svuotare il registro ? ")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Cancel)
        x= msg.exec()
        if x == QMessageBox.Ok:
                df3 = pd.DataFrame(columns=['Nome','Cognome','Data','Test', 'Risultato'])  
                df3.to_csv(os.path.join('./',r'registro.csv'), index = None ) 
                df4 = pd.read_csv('./registro.csv')
                self.Tabella.setRowCount(df4.shape[0])
                for i in range(df4.shape[0]):
                        self.Tabella.setItem(i,0,QTableWidgetItem(df4.iloc[i]['Nome']))
                        self.Tabella.setItem(i,1,QTableWidgetItem(df4.iloc[i]['Cognome']))
                        self.Tabella.setItem(i,2,QTableWidgetItem(df4.iloc[i]['Data'])) 
                        self.Tabella.setItem(i,3,QTableWidgetItem(df4.iloc[i]['Test']))
                        self.Tabella.setItem(i,4,QTableWidgetItem(df4.iloc[i]['Risultato']))  

    def guida(self):
        subprocess.Popen(['Guida.pdf'],shell=True)
    def check_account(self):
        try: 
                self.account = pd.read_csv('./account.csv')
                self.lineEdit.setText(str(self.account.iloc[0,0]))
                self.lineEdit_2.setText(str(self.account.iloc[0,1]))
                self.lineEdit_3.setText(str(self.account.iloc[0,2]))
                self.comboBox.setCurrentIndex(int(self.account.iloc[0,3]))
                self.hidemine()
        except:
                pass
    def mostratabella(self):
        try:
                df = pd.read_csv('./registro.csv')
                self.Tabella.setRowCount(df.shape[0])
                for i in range(df.shape[0]):
                        
                        self.Tabella.setItem(i,0,QTableWidgetItem(df.iloc[i]['Nome']))
                        self.Tabella.setItem(i,1,QTableWidgetItem(df.iloc[i]['Cognome']))
                        self.Tabella.setItem(i,2,QTableWidgetItem(df.iloc[i]['Data'])) 
                        self.Tabella.setItem(i,3,QTableWidgetItem(df.iloc[i]['Test']))
                        self.Tabella.setItem(i,4,QTableWidgetItem(df.iloc[i]['Risultato'])) 
        except:
                pass
                        

##### to put headers for the table widget you will need to call setHorizontalHeadersLabels
        
        
        
    def save(self):
        df = pd.DataFrame(columns=['Nome','Cognome','Manager','Certificazione'])
        new_row = { 'Nome':self.lineEdit.text(),'Cognome':self.lineEdit_2.text(),'Manager':self.lineEdit_3.text(),'Certificazione':self.comboBox.currentIndex()}
        df = df.append(new_row,ignore_index=True)
        df.to_csv(os.path.join('./',r'account.csv'), index = None )
              
    def slidemenu(self):
        width = self.sfondotasti.width()
        
        if width == 50:
                newwidth = 400
                
        else:
                newwidth = 50
                

        self.animation = QPropertyAnimation(self.sfondotasti,b"minimumWidth")
        self.animation.setDuration(400)
        self.animation.setEasingCurve(QtCore.QEasingCurve.OutBack)
        self.animation.setEndValue(newwidth)
        self.animation.start()
    def popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Consegna Test")
        msg.setText("Stai per consegnare il test, una volta fatto non potrai modificare le risposte !")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Cancel)
        
        x= msg.exec()
        if x == QMessageBox.Ok:
                self.sfondotasti.show()
                self.elaborarisultati()
                self.gen.setCurrentWidget(self.mostrarisultati)
                #### salvataggio nel file registro
                try:
                        df = pd.read_csv('./registro.csv')
                        
                        now = datetime.now()
                        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                        risultato_percentuale = str(round(self.risultato, 2)) + ' %'
                        new_row2 = { 'Nome':self.lineEdit.text(),'Cognome':self.lineEdit_2.text(),'Data':dt_string,'Test':self.titolomodulo.text(),'Risultato': risultato_percentuale}
                        df = df.append(new_row2,ignore_index=True)
                        print(df)
                        df.to_csv(os.path.join('./',r'registro.csv'), index = None )
                except:
                        now = datetime.now()
                        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                        df2 = pd.DataFrame(columns=['Nome','Cognome','Data','Test', 'Risultato'])
                        risultato_percentuale = str(round(self.risultato, 2)) + ' %'
                        new_row2 = { 'Nome':self.lineEdit.text(),'Cognome':self.lineEdit_2.text(),'Data':dt_string,'Test':self.titolomodulo.text(),'Risultato': risultato_percentuale}
                        df2 = df2.append(new_row2,ignore_index=True)
                        df2.to_csv(os.path.join('./',r'registro.csv'), index = None )
        
                
   
                
        
    def slidemenuvertical(self):
        height = self.moviment.height()
        
        if height == 0:
                newheight = 400
                # self.centralwidget.sfondotasti.setMaximumSize(QtCore.QSize(newwidth, 16777215))
                
        else:
                newheight = 0
                # self.centralwidget.sfondotasti.setMaximumSize(QtCore.QSize(newwidth, 16777215))

        self.animation = QPropertyAnimation(self.moviment,b"minimumHeight")
        self.animation.setDuration(400)
        self.animation.setEasingCurve(QtCore.QEasingCurve.OutBack)
        self.animation.setEndValue(newheight)
        self.animation.start()
    def halfvertical(self):
        height = self.moviment.height()
        if height == 400:
                newheight = 0
                self.animation = QPropertyAnimation(self.moviment,b"minimumHeight")
                self.animation.setDuration(400)
                self.animation.setEasingCurve(QtCore.QEasingCurve.OutBack)
                self.animation.setEndValue(newheight)
                self.animation.start()
         
                    
    def resetprova(self):
            self.halfvertical()
            self.prova = provamaster.copy()
            try:
                    self.prova.iloc[:]['CORR 1'] = ''
                    self.prova.iloc[:]['CORR 2'] = ''
                    self.prova.iloc[:]['CORR 3'] = ''
                    self.prova.iloc[:]['CORR 4'] = ''
                    self.prova.iloc[:]['CORR 5'] = ''
                    global calcolo
                    calcolo = 0
            except:
                    pass
          #### controllo quale modulo ?? stato scelto
            if self.module1.isChecked():
                    self.titolomodulo.setText('Modulo 1')
                    
                    self.prova = self.prova[self.prova['Gruppo'] == 'Modulo 1']
                    self.prova.index = np.arange(1, len(self.prova) + 1)
                    
                    
            elif self.module2.isChecked():
                    self.titolomodulo.setText('Modulo 2')
                    
                    self.prova = self.prova[self.prova['Gruppo'] == 'Modulo 2']
                    self.prova.index = np.arange(1, len(self.prova) + 1)
                    
            elif self.module3.isChecked():
                    self.titolomodulo.setText('Modulo 3')
                    
                    self.prova = self.prova[self.prova['Gruppo'] == 'Modulo 3']
                    self.prova.index = np.arange(1, len(self.prova) + 1)
                    
            elif self.module4.isChecked():
                    self.titolomodulo.setText('Modulo 4')
                    
                    self.prova = self.prova[self.prova['Gruppo'] == 'Modulo 4']
                    self.prova.index = np.arange(1, len(self.prova) + 1)
            elif self.module4.isChecked():
                    self.titolomodulo.setText('Modulo 4')
                    
                    self.prova = self.prova[self.prova['Gruppo'] == 'Modulo 4']
                    self.prova.index = np.arange(1, len(self.prova) + 1)
            
            elif self.module5.isChecked():
                    self.titolomodulo.setText('Modulo 5')
                    
                    self.prova = self.prova[self.prova['Gruppo'] == 'Modulo 5']
                    self.prova.index = np.arange(1, len(self.prova) + 1)
            
            elif self.module6.isChecked():
                    self.titolomodulo.setText('Modulo 6')
                    
                    self.prova = self.prova[self.prova['Gruppo'] == 'Modulo 6']
                    self.prova.index = np.arange(1, len(self.prova) + 1)
                    
            elif self.module7.isChecked():
                    self.titolomodulo.setText('Modulo 7')
                    
                    self.prova = self.prova[self.prova['Gruppo'] == 'Modulo 7']
                    self.prova.index = np.arange(1, len(self.prova) + 1)
            
            elif self.modulemix.isChecked():
                    self.titolomodulo.setText('Simulazione Esame')
                    
                    ### compongo la prova fatta di 60 domande normali + 20 random dalla simulazione
                    
                    database1 = self.prova[self.prova['Gruppo'] == 'Simulazione']
                    database2 = self.prova[self.prova['Gruppo'] != 'Simulazione']
                    
                    database1 = database1.sample(n=20)
                    database2 = database2.sample(n=60)
                    frames = [database1, database2]
                    self.prova = pd.concat(frames)
                    self.prova = self.prova.sample(n=80) # forse non serve questa condizione
                    # devo aggiungere scelta di 80 domande random 
                    # e indici dataframe crescenti corretti
                    self.prova.index = np.arange(1, len(self.prova) + 1)
                    
                    
            
            self.showquestions()       
            
                            
    def elaborarisultati(self):
            righe = self.prova.shape[0]
            try:
                    righe = self.prova.shape[0]
                    for i in range(self.verticalLayout_2.count()):
                            if self.verticalLayout_2.itemAt(i).widget().isChecked():
                                    self.prova.iloc[calcolo,i+12] = 'x'
            except:
                    pass
            risultato = 0
            for i in range(righe):
                    vettore = self.prova.iloc[[i]]
                    vettorecorretto = corrette[corrette['Domanda'] == vettore.iloc[0]['Domanda']]
                    
                    if (vettore.iloc[0]['CORR 1'] == vettorecorretto.iloc[0]['CORR 1'] and
                        vettore.iloc[0]['CORR 2'] == vettorecorretto.iloc[0]['CORR 2'] and
                        vettore.iloc[0]['CORR 3'] == vettorecorretto.iloc[0]['CORR 3'] and
                        vettore.iloc[0]['CORR 4'] == vettorecorretto.iloc[0]['CORR 4'] and
                        vettore.iloc[0]['CORR 5'] == vettorecorretto.iloc[0]['CORR 5']):
                            risultato += 1
            risultato = round((risultato/righe)*100,2)
            self.risultato = risultato
            if risultato >= 80:
                    self.label_5.setStyleSheet("color: rgb(0, 170, 0);")
                    self.label_5.setText("Congratulazioni! Hai superato il test con il punteggio di:")
                    self.label_6.setText(str(risultato)+" %")
                    self.tryagain.hide()
            else:
                    self.label_5.setStyleSheet("color: rgb(255, 0, 0);")
                    self.label_5.setText("Sfortunatamente non hai superato il test, il tuo punteggio ??:")
                    self.label_6.setText(str(risultato)+" %")
                    self.tryagain.show()
                    
            
                #     self.prova.to_csv(os.path.join('./',r'test.csv'), index = None )
            
        
    def getSaveFileName(self):
        response = QFileDialog.getSaveFileName(
        parent = self,
        caption = "Esporta registro test",
        directory = 'RegistroTest.csv',
        filter = 'Excel File (*.csv)')
        response = response[0]
        response = response.replace('/', '\\')
        print(response)
        try:
                df = pd.read_csv('./registro.csv')
                print(df)
                df.to_csv(response, index = None )
                
        except:
                pass
                
    def web_browser(self):
            if self.comboBox.currentIndex() == 1:
                    webbrowser.open('https://help.sap.com/doc/fd2b9c6949de43938078489525288f13/PRO_2.0/en-US/50047c917a2610149575e3c6cab404af.html?collapse=5')
            elif self.comboBox.currentIndex() == 2:
                    webbrowser.open('https://help.sap.com/doc/fd2b9c6949de43938078489525288f13/PRO_2.0/en-US/50089b367a26101490068d8292630a23.html?collapse=5')
    
    def minmax(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
    def hidemine(self):
        if self.comboBox.currentIndex() == 1:
                self.Moduli.show()
                self.Questions.show()
                self.CutScore.show()
                self.LearningHub.show()
                self.lineEdit_4.show()
                self.lineEdit_5.show()
                self.lineEdit_6.show()
                self.linkbutton.show()
                self.lineEdit_4.setText('7')
                self.lineEdit_5.setText('80')
                self.lineEdit_6.setText('65%')
                self.frame_17.show()
                self.moduletest.show()
                self.module1.show()
                self.module2.show()
                self.module3.show()
                self.module4.show()
                self.module5.show()
                self.module6.show()
                self.module7.show()
                self.modulemix.show()
                self.moviment.show()
                fixed = """\nInventory Management and Physical Inventory\t\t8% - 12%\n
Valuation and Account Assignment\t\t\t\t8% - 12%\n
Configuration of Purchasing\t\t\t\t8% - 12%\n
Configuration of Master Data and Enterprise Structure\t8% - 12%\n
Invoice Verification\t\t\t\t\t8% - 12%\n
Sources of Supply\t\t\t\t\t8% - 12%\n
Document Release Procedure\t\t\t\t< 8%\n
Purchasing Optimization\t\t\t\t\t< 8%\n
Source Determination\t\t\t\t\t< 8%\n
Procurement Analytics\t\t\t\t\t< 8%\n
Consumption-Based Planning\t\t\t\t< 8%\n
Enterprise Structure and Master Data\t\t\t< 8%\n
Specific Procurement Processes\t\t\t\t< 8%\n
Basic Procurement\t\t\t\t\t< 8%\n
SAP S/4HANA User Experience\t\t\t\t< 8%
        """
                self.label_7.setAlignment(QtCore.Qt.AlignLeft)
                self.label_7.setText(fixed)
        elif self.comboBox.currentIndex() == 2:
                self.Moduli.show()
                self.Questions.show()
                self.CutScore.show()
                self.LearningHub.show()
                self.lineEdit_4.show()
                self.lineEdit_5.show()
                self.lineEdit_6.show()
                self.linkbutton.show()
                self.lineEdit_4.setText('5')
                self.lineEdit_5.setText('80')
                self.lineEdit_6.setText('60%')
                self.frame_17.show()
                self.moduletest.show()
                self.module1.show()
                self.module2.show()
                self.module3.show()
                self.module4.show()
                self.module5.show()
                self.module6.hide()
                self.module7.hide()
                self.modulemix.show()
                self.moviment.show()
        elif self.comboBox.currentIndex() == 0:
                self.Moduli.hide()
                self.Questions.hide()
                self.CutScore.hide()
                self.LearningHub.hide()
                self.lineEdit_4.setText('')
                self.lineEdit_5.setText('')
                self.lineEdit_6.setText('')
                self.linkbutton.hide()
                self.frame_17.hide()
                self.moduletest.hide()
                self.module1.hide()
                self.module2.hide()
                self.module3.hide()
                self.module4.hide()
                self.module5.hide()
                self.module6.hide()
                self.module7.hide()
                self.modulemix.hide()
                self.moviment.hide()
                self.label_7.setText('')
    def regexclude(self):
        self.module0.setChecked(False)
        self.moduletest.setChecked(False)
        
    def eventFilter(self, source, event):
        if source == self.frame_5:
            if event.type() == QtCore.QEvent.MouseButtonPress:
                self.offset = event.pos()
            elif event.type() == QtCore.QEvent.MouseMove and self.offset is not None:
                # no need for complex computations: just use the offset to compute
                # "delta" position, and add that to the current one
                self.move(self.pos() - self.offset + event.pos())
                # return True to tell Qt that the event has been accepted and
                # should not be processed any further
                return True
            elif event.type() == QtCore.QEvent.MouseButtonRelease:
                self.offset = None
        # let Qt process any other event
        return super().eventFilter(source, event)
        

        #     def mousePressEvent(self, event):  

        #         self.dragPos = event.globalPos()
                
        #     def mouseMoveEvent(self, event):                                  # !!!
        #         if event.buttons() == QtCore.Qt.LeftButton:
        #             self.move(self.pos() + event.globalPos() - self.dragPos)
        #             self.dragPos = event.globalPos()
        #             event.accept()  
           

    def deletebutton(self):
        
        for i in range(self.verticalLayout_2.count()):
                self.verticalLayout_2.itemAt(i).widget().deleteLater()
    def assigndec(self):
            decision = 1
    def incrementi(self):
            global calcolo
            
            
            
        #     print(self.prova.iloc[:,12:])
 
            righe = self.prova.shape[0]
            for i in range(self.verticalLayout_2.count()):
                    if self.verticalLayout_2.itemAt(i).widget().isChecked():
                            
                            self.prova.iloc[calcolo,i+12] = 'x'
                            
             
        
            if calcolo == righe -1:
                    calcolo = 0
            else:
                    calcolo += 1
            
            self.showquestions()
    def decrementi(self):
            global calcolo
            
            righe = self.prova.shape[0]
            for i in range(self.verticalLayout_2.count()):
                    if self.verticalLayout_2.itemAt(i).widget().isChecked():
                            
                            self.prova.iloc[calcolo,i+12] = 'x'    
            
                    
                            
         
            if calcolo == 0:
                    calcolo = righe-1
            else:
                    calcolo -= 1
            
            self.showquestions()  
    def popup_save(self):
        if self.comboBox.currentIndex() != 0:
                msg = QMessageBox()
                msg.setWindowTitle("Salvataggio Profilo")
                msg.setText("Salvando il profilo perderai eventuali altri profili salvati in precedenza ")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Cancel)
        
                x= msg.exec()
                if x == QMessageBox.Ok:
                        self.save()
        else:
                msg = QMessageBox()
                msg.setWindowTitle("Attenzione")
                msg.setText("Almeno una certificazione deve essere selezionata per procedere al salvataggio")
                msg.setIcon(QMessageBox.Critical)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
        
                x= msg.exec()
                
                              
    def addbuttons1(self):
            
            global calcolo
            
            i=calcolo
            vettore = self.prova.iloc[[i]]
            
            
            self.deletebutton()
            
            self.domanda.setText(vettore.iloc[0]['Domanda'])
            ndomande = vettore.iloc[0]['COLONNA']
            
            if vettore.iloc[0]['Tipo'] == 'R':
                    for i in range(ndomande):
                            self.radioButton = QtWidgets.QRadioButton(self.risposte)
                            self.radioButton.setObjectName("radioButton")
                            testo = str(vettore.iloc[0, i+4])
                            testospaziato = af.shorten(testo)
                            self.radioButton.setText(testospaziato)
                            self.radioButton.setAccessibleName("radioButton"+str(i+1))
                            
                        #     self.descrizione = QtWidgets.QLineEdit(self.risposte)
                        #     font = QtGui.QFont()
                        #     font.setFamily("IBM Plex Arabic")
                        #     font.setPointSize(12)
                        #     self.descrizione.setFont(font)
                        #     self.descrizione.setText(str(vettore.iloc[0, i+4]))
                        #     self.descrizione.setReadOnly(True)
                        #     self.descrizione.setObjectName("descrizione")
                        #     self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.descrizione)
                        #     self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.radioButton)
                            self.verticalLayout_2.addWidget(self.radioButton)
                            if self.prova.iloc[calcolo,i+12] == 'x':
                                    self.radioButton.setChecked(True)
                                    self.prova.iloc[calcolo,i+12] = ''
            else:
                    for i in range(ndomande):
                            self.checkBox = QtWidgets.QCheckBox(self.risposte)
                            self.checkBox.setObjectName("radioButton")
                            testo = str(vettore.iloc[0, i+4])
                            testospaziato = af.shorten(testo)
                            self.checkBox.setText(testospaziato)
                            self.checkBox.setAccessibleName("checkBox"+str(i+1))
                        #     self.checkBox.setWordWrap(True)
                            self.verticalLayout_2.addWidget(self.checkBox)
                            if self.prova.iloc[calcolo,i+12] == 'x':
                                    self.checkBox.setChecked(True)
                                    self.prova.iloc[calcolo,i+12] = ''
    
                 
    def showquestions(self):
            
            global calcolo
            
            i=calcolo
            self.numerodomanda.setText("Domanda: "+str(i+1))
            
            self.addbuttons1()
            
            

        


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)

    
decision= 0
corrette, provamaster = af.trovadati()
try:
        account = pd.read_csv('./account.csv')
        
        # account.index = np.arange(1, len(account) + 1)
        
        
                
except:
        pass