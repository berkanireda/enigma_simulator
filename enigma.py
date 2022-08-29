from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import numpy as np

alphabet = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
Reflecteur = np.array([25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1, -1, -3, -5, -7, -9, -11, -13, -15, -17, -19, -21, -23, -25]) 

R10 = np.array([17, 4, 19, 21, 7, 11, 3, -5, 7, 9, -10, 9, 17, 6, -6, -2, -4, -7, -12, -5, +3, +4, -21, -16, -2, -21])
R11 = np.array([10, 21, 5, -17, 21, -4, 12, 16, 6, -3, 7, -7, 4, 2, 5, -7, -11, -17, -9, -6, -9, -19, +2, -3, -21, -4])

R20 = np.array([25, 7, 17, -3, 13, 19, 12, 3, -1, 11, 5, -5, -7, 10, -2, 1, -2, +4, -17, -8, -16, -18, -9, -1, -22, -16])
R21 = np.array([3, 17, 22, 18, 16, 7, 5, 1, -7, 16, -3, 8, 2, 9, 2, -5, -1, -13, -12, -17, -11, -4, 1, -10, -19, -25])

R30 = np.array([12, -1, 23, 10, 2, 14, 5, -5, 9, -2, -13, 10, -2, -8, 10, -6, +6, -16, 2, -1, -17, -5, -14, -9, -20, -10])
R31 = np.array([1, 16, 5, 17, 20, 8, -2, +2, 14, 6, 2, -5, -12, -10, 9, 10, 5, -9, 1, -14, -2, -10, -6, 13, -10, -23])
    
key = np.empty((3, 3), dtype = list)

increment = 0
texte_crypte = ''

k1 = 1
k2 = 1
k3 = 1
text_index = 0



class Ui_Form(object):
    
    def configurer_rotor(self):
        
        if (self.comboBox.currentText() != self.comboBox_3.currentText()) and (self.comboBox.currentText() != self.comboBox_5.currentText()) and (self.comboBox_5.currentText() != self.comboBox_3.currentText()):
            key = globals()['key']
       
            self.pushButton_4.setEnabled(True)
            self.pushButton_2.setEnabled(True)
            self.pushButton.setEnabled(True)
            
            key[0,0] = self.comboBox.currentText()
            key[0,1] = self.comboBox_2.currentText()
            key[0,2] = self.Slider.value()  
            
            key[1,0] = self.comboBox_3.currentText()
            key[1,1] = self.comboBox_4.currentText()
            key[1,2] = self.Slider_2.value()  
            
            key[2,0] = self.comboBox_5.currentText()
            key[2,1] = self.comboBox_6.currentText()
            key[2,2] = self.Slider_3.value()
            
            
            globals()['R'+ key[0, 0] + '0'] = np.roll(globals()['R' + key[0, 0] + '0'], int(key[0 ,2]))
            globals()['R'+ key[0, 0] + '1'] = np.roll(globals()['R' + key[0, 0] + '1'], int(key[0 ,2]))
                
            globals()['R'+ key[1, 0] + '0'] = np.roll(globals()['R' + key[1, 0] + '0'], int(key[1 ,2]))
            globals()['R'+ key[1, 0] + '1'] = np.roll(globals()['R' + key[1, 0] + '1'], int(key[1 ,2]))
                
            globals()['R'+key[2, 0] + '0'] = np.roll(globals()['R' + key[2, 0] + '0'], int(key[2 ,2]))
            globals()['R'+key[2, 0] + '1'] = np.roll(globals()['R' + key[2, 0] + '1'], int(key[2 ,2]))
            
            self.pushButton_R1.setText(str(Reflecteur[0]))
            self.pushButton_R2.setText(str(Reflecteur[1]))
            self.pushButton_R3.setText(str(Reflecteur[2]))
            self.pushButton_R4.setText(str(Reflecteur[3]))
            self.pushButton_R5.setText(str(Reflecteur[4]))
            self.pushButton_R6.setText(str(Reflecteur[5]))
            self.pushButton_R7.setText(str(Reflecteur[6]))
            self.pushButton_R8.setText(str(Reflecteur[7]))
            self.pushButton_R9.setText(str(Reflecteur[8]))
            self.pushButton_R10.setText(str(Reflecteur[9]))
            self.pushButton_R11.setText(str(Reflecteur[10]))
        
            self.pushButton_R12.setText(str(Reflecteur[11]))
            self.pushButton_R13.setText(str(Reflecteur[12]))
            self.pushButton_R14.setText(str(Reflecteur[13]))
            self.pushButton_R15.setText(str(Reflecteur[14]))
            self.pushButton_R16.setText(str(Reflecteur[15]))
            self.pushButton_R17.setText(str(Reflecteur[16]))
            self.pushButton_R18.setText(str(Reflecteur[17]))
            self.pushButton_R19.setText(str(Reflecteur[18]))
            self.pushButton_R20.setText(str(Reflecteur[19]))
            self.pushButton_R21.setText(str(Reflecteur[20]))
            self.pushButton_R22.setText(str(Reflecteur[21]))
            self.pushButton_R23.setText(str(Reflecteur[22]))
            self.pushButton_R24.setText(str(Reflecteur[23]))
            self.pushButton_R25.setText(str(Reflecteur[24]))
            self.pushButton_R26.setText(str(Reflecteur[25]))
            
            ########################################
            
            ######### ROTOR 1 EDIT ###################
            self.pushButton_111.setText(str(R10[0]))
            self.pushButton_112.setText(str(R10[1]))
            self.pushButton_113.setText(str(R10[2]))
            self.pushButton_114.setText(str(R10[3]))
            self.pushButton_115.setText(str(R10[4]))
            self.pushButton_116.setText(str(R10[5]))
            self.pushButton_117.setText(str(R10[6]))
            self.pushButton_118.setText(str(R10[7]))
            self.pushButton_119.setText(str(R10[8]))
            self.pushButton_1110.setText(str(R10[9]))
            self.pushButton_1111.setText(str(R10[10]))
            
            self.pushButton_1112.setText(str(R10[11]))
            self.pushButton_1113.setText(str(R10[12]))
            self.pushButton_1114.setText(str(R10[13]))
            self.pushButton_1115.setText(str(R10[14]))
            self.pushButton_1116.setText(str(R10[15]))
            self.pushButton_1117.setText(str(R10[16]))
            self.pushButton_1118.setText(str(R10[17]))
            self.pushButton_1119.setText(str(R10[18]))
            self.pushButton_1120.setText(str(R10[19]))
            self.pushButton_1121.setText(str(R10[20]))
            self.pushButton_1122.setText(str(R10[21]))
            self.pushButton_1123.setText(str(R10[22]))
            self.pushButton_1124.setText(str(R10[23]))
            self.pushButton_1125.setText(str(R10[24]))
            self.pushButton_1126.setText(str(R10[25]))
            
            
            
            
            self.pushButton_121.setText(str(R11[0]))
            self.pushButton_122.setText(str(R11[1]))
            self.pushButton_123.setText(str(R11[2]))
            self.pushButton_124.setText(str(R11[3]))
            self.pushButton_125.setText(str(R11[4]))
            self.pushButton_126.setText(str(R11[5]))
            self.pushButton_127.setText(str(R11[6]))
            self.pushButton_128.setText(str(R11[7]))
            self.pushButton_129.setText(str(R11[8]))
            self.pushButton_1210.setText(str(R11[9]))
            self.pushButton_1211.setText(str(R11[10]))
            self.pushButton_1212.setText(str(R11[11]))
            self.pushButton_1213.setText(str(R11[12]))
            self.pushButton_1214.setText(str(R11[13]))
            self.pushButton_1215.setText(str(R11[14]))
            self.pushButton_1216.setText(str(R11[15]))
            self.pushButton_1217.setText(str(R11[16]))
            self.pushButton_1218.setText(str(R11[17]))
            self.pushButton_1219.setText(str(R11[18]))
            self.pushButton_1220.setText(str(R11[19]))
            self.pushButton_1221.setText(str(R11[20]))
            self.pushButton_1222.setText(str(R11[21]))
            self.pushButton_1223.setText(str(R11[22]))
            self.pushButton_1224.setText(str(R11[23]))
            self.pushButton_1225.setText(str(R11[24]))
            self.pushButton_1226.setText(str(R11[25]))
            
            
            ################### ROTOR 2 ######################3
            
            self.pushButton_211.setText(str(R20[0]))
            self.pushButton_212.setText(str(R20[1]))
            self.pushButton_213.setText(str(R20[2]))
            self.pushButton_214.setText(str(R20[3]))
            self.pushButton_215.setText(str(R20[4]))
            self.pushButton_216.setText(str(R20[5]))
            self.pushButton_217.setText(str(R20[6]))
            self.pushButton_218.setText(str(R20[7]))
            self.pushButton_219.setText(str(R20[8]))
            self.pushButton_2110.setText(str(R20[9]))
            self.pushButton_2111.setText(str(R20[10]))
            self.pushButton_2112.setText(str(R20[11]))
            self.pushButton_2113.setText(str(R20[12]))
            self.pushButton_2114.setText(str(R20[13]))
            self.pushButton_2115.setText(str(R20[14]))
            self.pushButton_2116.setText(str(R20[15]))
            self.pushButton_2117.setText(str(R20[16]))
            self.pushButton_2118.setText(str(R20[17]))
            self.pushButton_2119.setText(str(R20[18]))
            self.pushButton_2120.setText(str(R20[19]))
            self.pushButton_2121.setText(str(R20[20]))
            self.pushButton_2122.setText(str(R20[21]))
            self.pushButton_2123.setText(str(R20[22]))
            self.pushButton_2124.setText(str(R20[23]))
            self.pushButton_2125.setText(str(R20[24]))
            self.pushButton_2126.setText(str(R20[25]))
            
            
            self.pushButton_221.setText(str(R21[0]))
            self.pushButton_222.setText(str(R21[1]))
            self.pushButton_223.setText(str(R21[2]))
            self.pushButton_224.setText(str(R21[3]))
            self.pushButton_225.setText(str(R21[4]))
            self.pushButton_226.setText(str(R21[5]))
            self.pushButton_227.setText(str(R21[6]))
            self.pushButton_228.setText(str(R21[7]))
            self.pushButton_229.setText(str(R21[8]))
            self.pushButton_2210.setText(str(R21[9]))
            self.pushButton_2211.setText(str(R21[10]))
            self.pushButton_2212.setText(str(R21[11]))
            self.pushButton_2213.setText(str(R21[12]))
            self.pushButton_2214.setText(str(R21[13]))
            self.pushButton_2215.setText(str(R21[14]))
            self.pushButton_2216.setText(str(R21[15]))
            self.pushButton_2217.setText(str(R21[16]))
            self.pushButton_2218.setText(str(R21[17]))
            self.pushButton_2219.setText(str(R21[18]))
            self.pushButton_2220.setText(str(R21[19]))
            self.pushButton_2221.setText(str(R21[20]))
            self.pushButton_2222.setText(str(R21[21]))
            self.pushButton_2223.setText(str(R21[22]))
            self.pushButton_2224.setText(str(R21[23]))
            self.pushButton_2225.setText(str(R21[24]))
            self.pushButton_2226.setText(str(R21[25]))
        
        #################  ROTOR 3 ##########################
        
            self.pushButton_311.setText(str(R30[0]))
            self.pushButton_312.setText(str(R30[1]))
            self.pushButton_313.setText(str(R30[2]))
            self.pushButton_314.setText(str(R30[3]))
            self.pushButton_315.setText(str(R30[4]))
            self.pushButton_316.setText(str(R30[5]))
            self.pushButton_317.setText(str(R30[6]))
            self.pushButton_318.setText(str(R30[7]))
            self.pushButton_319.setText(str(R30[8]))
            self.pushButton_3110.setText(str(R30[9]))
            self.pushButton_3111.setText(str(R30[10]))
            self.pushButton_3112.setText(str(R30[11]))
            self.pushButton_3113.setText(str(R30[12]))
            self.pushButton_3114.setText(str(R30[13]))
            self.pushButton_3115.setText(str(R30[14]))
            self.pushButton_3116.setText(str(R30[15]))
            self.pushButton_3117.setText(str(R30[16]))
            self.pushButton_3118.setText(str(R30[17]))
            self.pushButton_3119.setText(str(R30[18]))
            self.pushButton_3120.setText(str(R30[19]))
            self.pushButton_3121.setText(str(R30[20]))
            self.pushButton_3122.setText(str(R30[21]))
            self.pushButton_3123.setText(str(R30[22]))
            self.pushButton_3124.setText(str(R30[23]))
            self.pushButton_3125.setText(str(R30[24]))
            self.pushButton_3126.setText(str(R30[25]))
            
            self.pushButton_321.setText(str(R31[0]))
            self.pushButton_322.setText(str(R31[1]))
            self.pushButton_323.setText(str(R31[2]))
            self.pushButton_324.setText(str(R31[3]))
            self.pushButton_325.setText(str(R31[4]))
            self.pushButton_326.setText(str(R31[5]))
            self.pushButton_327.setText(str(R31[6]))
            self.pushButton_328.setText(str(R31[7]))
            self.pushButton_329.setText(str(R31[8]))
            self.pushButton_3210.setText(str(R31[9]))
            self.pushButton_3211.setText(str(R31[10]))
            self.pushButton_3212.setText(str(R31[11]))
            self.pushButton_3213.setText(str(R31[12]))
            self.pushButton_3214.setText(str(R31[13]))
            self.pushButton_3215.setText(str(R31[14]))
            self.pushButton_3216.setText(str(R31[15]))
            self.pushButton_3217.setText(str(R31[16]))
            self.pushButton_3218.setText(str(R31[17]))
            self.pushButton_3219.setText(str(R31[18]))
            self.pushButton_3220.setText(str(R31[19]))
            self.pushButton_3221.setText(str(R31[20]))
            self.pushButton_3222.setText(str(R31[21]))
            self.pushButton_3223.setText(str(R31[22]))
            self.pushButton_3224.setText(str(R31[23]))
            self.pushButton_3225.setText(str(R31[24]))
            self.pushButton_3226.setText(str(R31[25]))
            
            self.pushButton_3.setEnabled(False)
            
        else:
            error = QMessageBox()
            error.setWindowTitle("Erreur de configuration")
            error.setText("Cette configuration n'est pas permise")
            error.setIcon(QMessageBox.Critical)
            print("Error of configuration")
            x = error.exec_()
        
        
        
        ############## reflector #####################
        
        

        
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        
       
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_rt1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_rt2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        
        
        
        ###########################################################
        self.verticalLayout_reflecteur = QtWidgets.QVBoxLayout()
         
        self.horizontalLayout_reflecteur = QtWidgets.QHBoxLayout()
        self.horizontalLayout_reflecteur.setObjectName("horizontalLayout_reflecteur")
        self.pushButton_R1 = QtWidgets.QPushButton(Form)
        
        ############ dictionary ###################
        dict = {"R1" : self.pushButton_R1 }
        self.pushButton_R1.setObjectName("pushButton_R1")
        self.horizontalLayout_reflecteur.addWidget(self.pushButton_R1)
        self.pushButton_R2 = QtWidgets.QPushButton(Form)
        self.pushButton_R2.setObjectName("pushButton_R2")
        
        dict["R2"] = self.pushButton_R1
        
        self.horizontalLayout_reflecteur.addWidget(self.pushButton_R2)
        self.pushButton_R3 = QtWidgets.QPushButton(Form)
        self.pushButton_R3.setObjectName("pushButton_R3")
        self.horizontalLayout_reflecteur.addWidget(self.pushButton_R3)
        self.pushButton_R4 = QtWidgets.QPushButton(Form)
        self.pushButton_R4.setObjectName("pushButton_R4")
        self.horizontalLayout_reflecteur.addWidget(self.pushButton_R4)
        self.pushButton_R5 = QtWidgets.QPushButton(Form)
        self.pushButton_R5.setObjectName("pushButton_R5")
        self.horizontalLayout_reflecteur.addWidget(self.pushButton_R5)
        self.pushButton_R6 = QtWidgets.QPushButton(Form)
        self.pushButton_R6.setObjectName("pushButton_R6")
        self.horizontalLayout_reflecteur.addWidget(self.pushButton_R6)
        self.pushButton_R7 = QtWidgets.QPushButton(Form)
        self.pushButton_R7.setObjectName("pushButton_R7")
        self.horizontalLayout_reflecteur.addWidget(self.pushButton_R7)
        self.pushButton_R9 = QtWidgets.QPushButton(Form)
        self.pushButton_R9.setObjectName("pushButton_R9")
        self.horizontalLayout_reflecteur.addWidget(self.pushButton_R9)
        self.pushButton_R10 = QtWidgets.QPushButton(Form)
        self.pushButton_R10.setObjectName("pushButton_R10")
        self.horizontalLayout_reflecteur.addWidget(self.pushButton_R10)
        self.pushButton_R11 = QtWidgets.QPushButton(Form)
        self.pushButton_R11.setObjectName("pushButton_R11")
        self.horizontalLayout_reflecteur.addWidget(self.pushButton_R11)
        self.pushButton_R12 = QtWidgets.QPushButton(Form)
        self.pushButton_R12.setObjectName("pushButton_R12")
        self.horizontalLayout_reflecteur.addWidget(self.pushButton_R12)
        self.pushButton_R13 = QtWidgets.QPushButton(Form)
        self.pushButton_R13.setObjectName("pushButton_R13")
        self.horizontalLayout_reflecteur.addWidget(self.pushButton_R13)
        self.pushButton_R14 = QtWidgets.QPushButton(Form)
        self.pushButton_R14.setObjectName("pushButton_R14")
        self.horizontalLayout_reflecteur.addWidget(self.pushButton_R14)
        self.pushButton_R15 = QtWidgets.QPushButton(Form)
        self.pushButton_R15.setObjectName("pushButton_R15")
        self.horizontalLayout_reflecteur.addWidget(self.pushButton_R15)
        self.pushButton_R16 = QtWidgets.QPushButton(Form)
        self.pushButton_R16.setObjectName("pushButton_R16")
        self.horizontalLayout_reflecteur.addWidget(self.pushButton_R16)
        self.pushButton_R17 = QtWidgets.QPushButton(Form)
        self.pushButton_R17.setObjectName("pushButton_R17")
        self.horizontalLayout_reflecteur.addWidget(self.pushButton_R17)
        self.pushButton_R18 = QtWidgets.QPushButton(Form)
        self.pushButton_R18.setObjectName("pushButton_R18")
        self.horizontalLayout_reflecteur.addWidget(self.pushButton_R18)
        self.pushButton_R19 = QtWidgets.QPushButton(Form)
        self.pushButton_R19.setObjectName("pushButton_R19")
        self.horizontalLayout_reflecteur.addWidget(self.pushButton_R19)
        self.pushButton_R20 = QtWidgets.QPushButton(Form)
        self.pushButton_R20.setObjectName("pushButton_R20")
        self.horizontalLayout_reflecteur.addWidget(self.pushButton_R20)
        self.pushButton_R21 = QtWidgets.QPushButton(Form)
        self.pushButton_R21.setObjectName("pushButton_R21")
        self.horizontalLayout_reflecteur.addWidget(self.pushButton_R21)
        self.pushButton_R22 = QtWidgets.QPushButton(Form)
        self.pushButton_R22.setObjectName("pushButton_R22")
        self.horizontalLayout_reflecteur.addWidget(self.pushButton_R22)
        self.pushButton_R23 = QtWidgets.QPushButton(Form)
        self.pushButton_R23.setObjectName("pushButton_R23")
        self.horizontalLayout_reflecteur.addWidget(self.pushButton_R23)
        self.pushButton_R24 = QtWidgets.QPushButton(Form)
        self.pushButton_R24.setObjectName("pushButton_R24")
        self.horizontalLayout_reflecteur.addWidget(self.pushButton_R24)
        self.pushButton_R25 = QtWidgets.QPushButton(Form)
        self.pushButton_R25.setObjectName("pushButton_R25")
        self.horizontalLayout_reflecteur.addWidget(self.pushButton_R25)
        self.pushButton_R26 = QtWidgets.QPushButton(Form)
        self.pushButton_R26.setObjectName("pushButton_R26")
        self.horizontalLayout_reflecteur.addWidget(self.pushButton_R26)
        self.pushButton_R8 = QtWidgets.QPushButton(Form)
        self.pushButton_R8.setObjectName("pushButton_R8")
        self.horizontalLayout_reflecteur.addWidget(self.pushButton_R8)
        
        self.verticalLayout_reflecteur.addLayout(self.horizontalLayout_reflecteur)
        
        self.verticalLayout.addLayout(self.verticalLayout_reflecteur)
        
        dict["R3"] = self.pushButton_R3
        dict["R4"] = self.pushButton_R4
        dict["R5"] = self.pushButton_R5
        dict["R6"] = self.pushButton_R6
        dict["R7"] = self.pushButton_R7
        dict["R8"] = self.pushButton_R8
        dict["R9"] = self.pushButton_R9
        dict["R10"] = self.pushButton_R10
        dict["R11"] = self.pushButton_R11
        dict["R12"] = self.pushButton_R12
        dict["R13"] = self.pushButton_R13
        dict["R14"] = self.pushButton_R14
        dict["R15"] = self.pushButton_R15
        dict["R16"] = self.pushButton_R16
        dict["R17"] = self.pushButton_R17
        dict["R18"] = self.pushButton_R18
        dict["R19"] = self.pushButton_R19
        dict["R20"] = self.pushButton_R20
        dict["R21"] = self.pushButton_R21
        dict["R22"] = self.pushButton_R22
        dict["R23"] = self.pushButton_R23
        dict["R24"] = self.pushButton_R24
        dict["R25"] = self.pushButton_R25
        dict["R26"] = self.pushButton_R26      
        
        ############################################################
        ##### rotor 3 ##########""
        self.verticalLayout_rt1.setObjectName("verticalLayout_rt1")
        
        self.titre = QtWidgets.QLabel()
        self.titre.setText("Rotor 3")
        self.verticalLayout_rt1.addWidget(self.titre)
        
        
        self.horizontalLayout_rt11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_rt11.setObjectName("horizontalLayout_rt11")
        self.pushButton_311 = QtWidgets.QPushButton(Form)
        self.pushButton_311.setObjectName("pushButton_311")
        self.horizontalLayout_rt11.addWidget(self.pushButton_311)
        self.pushButton_312 = QtWidgets.QPushButton(Form)
        self.pushButton_312.setObjectName("pushButton_312")
        self.horizontalLayout_rt11.addWidget(self.pushButton_312)
        self.pushButton_313 = QtWidgets.QPushButton(Form)
        self.pushButton_313.setObjectName("pushButton_313")
        self.horizontalLayout_rt11.addWidget(self.pushButton_313)
        self.pushButton_314 = QtWidgets.QPushButton(Form)
        self.pushButton_314.setObjectName("pushButton_314")
        self.horizontalLayout_rt11.addWidget(self.pushButton_314)
        self.pushButton_315 = QtWidgets.QPushButton(Form)
        self.pushButton_315.setObjectName("pushButton_315")
        self.horizontalLayout_rt11.addWidget(self.pushButton_315)
        self.pushButton_316 = QtWidgets.QPushButton(Form)
        self.pushButton_316.setObjectName("pushButton_316")
        self.horizontalLayout_rt11.addWidget(self.pushButton_316)
        self.pushButton_317 = QtWidgets.QPushButton(Form)
        self.pushButton_317.setObjectName("pushButton_317")
        self.horizontalLayout_rt11.addWidget(self.pushButton_317)
        self.pushButton_318 = QtWidgets.QPushButton(Form)
        self.pushButton_318.setObjectName("pushButton_318")
        self.horizontalLayout_rt11.addWidget(self.pushButton_318)
        self.pushButton_319 = QtWidgets.QPushButton(Form)
        self.pushButton_319.setObjectName("pushButton_319")
        self.horizontalLayout_rt11.addWidget(self.pushButton_319)
        self.pushButton_3110 = QtWidgets.QPushButton(Form)
        self.pushButton_3110.setObjectName("pushButton_3110")
        self.horizontalLayout_rt11.addWidget(self.pushButton_3110)
        self.pushButton_3111 = QtWidgets.QPushButton(Form)
        self.pushButton_3111.setObjectName("pushButton_3111")
        self.horizontalLayout_rt11.addWidget(self.pushButton_3111)
        self.pushButton_3112 = QtWidgets.QPushButton(Form)
        self.pushButton_3112.setObjectName("pushButton_3112")
        self.horizontalLayout_rt11.addWidget(self.pushButton_3112)
        self.pushButton_3113 = QtWidgets.QPushButton(Form)
        self.pushButton_3113.setObjectName("pushButton_3113")
        self.horizontalLayout_rt11.addWidget(self.pushButton_3113)
        self.pushButton_3114 = QtWidgets.QPushButton(Form)
        self.pushButton_3114.setObjectName("pushButton_3114")
        self.horizontalLayout_rt11.addWidget(self.pushButton_3114)
        self.pushButton_3115 = QtWidgets.QPushButton(Form)
        self.pushButton_3115.setObjectName("pushButton_3115")
        self.horizontalLayout_rt11.addWidget(self.pushButton_3115)
        self.pushButton_3116 = QtWidgets.QPushButton(Form)
        self.pushButton_3116.setObjectName("pushButton_3116")
        self.horizontalLayout_rt11.addWidget(self.pushButton_3116)
        self.pushButton_3117 = QtWidgets.QPushButton(Form)
        self.pushButton_3117.setObjectName("pushButton_3117")
        self.horizontalLayout_rt11.addWidget(self.pushButton_3117)
        self.pushButton_3118 = QtWidgets.QPushButton(Form)
        self.pushButton_3118.setObjectName("pushButton_3118")
        self.horizontalLayout_rt11.addWidget(self.pushButton_3118)
        self.pushButton_3119 = QtWidgets.QPushButton(Form)
        self.pushButton_3119.setObjectName("pushButton_3119")
        self.horizontalLayout_rt11.addWidget(self.pushButton_3119)
        self.pushButton_3120 = QtWidgets.QPushButton(Form)
        self.pushButton_3120.setObjectName("pushButton_3120")
        self.horizontalLayout_rt11.addWidget(self.pushButton_3120)
        self.pushButton_3121 = QtWidgets.QPushButton(Form)
        self.pushButton_3121.setObjectName("pushButton_3121")
        self.horizontalLayout_rt11.addWidget(self.pushButton_3121)
        self.pushButton_3122 = QtWidgets.QPushButton(Form)
        self.pushButton_3122.setObjectName("pushButton_3122")
        self.horizontalLayout_rt11.addWidget(self.pushButton_3122)
        self.pushButton_3123 = QtWidgets.QPushButton(Form)
        self.pushButton_3123.setObjectName("pushButton_3123")
        self.horizontalLayout_rt11.addWidget(self.pushButton_3123)
        self.pushButton_3124 = QtWidgets.QPushButton(Form)
        self.pushButton_3124.setObjectName("pushButton_3124")
        self.horizontalLayout_rt11.addWidget(self.pushButton_3124)
        self.pushButton_3125 = QtWidgets.QPushButton(Form)
        self.pushButton_3125.setObjectName("pushButton_3125")
        self.horizontalLayout_rt11.addWidget(self.pushButton_3125)
        self.pushButton_3126 = QtWidgets.QPushButton(Form)
        self.pushButton_3126.setObjectName("pushButton_3126")
        self.horizontalLayout_rt11.addWidget(self.pushButton_3126)
        
        self.verticalLayout_rt1.addLayout(self.horizontalLayout_rt11)
        self.horizontalLayout_rt12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_rt12.setObjectName("horizontalLayout_rt12")
        
        self.horizontalLayout_rt12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_rt12.setObjectName("horizontalLayout_rt12")
        self.pushButton_321 = QtWidgets.QPushButton(Form)
        self.pushButton_321.setObjectName("pushButton_321")
        self.horizontalLayout_rt12.addWidget(self.pushButton_321)
        self.pushButton_322 = QtWidgets.QPushButton(Form)
        self.pushButton_322.setObjectName("pushButton_322")
        self.horizontalLayout_rt12.addWidget(self.pushButton_322)
        self.pushButton_323 = QtWidgets.QPushButton(Form)
        self.pushButton_323.setObjectName("pushButton_323")
        self.horizontalLayout_rt12.addWidget(self.pushButton_323)
        self.pushButton_324 = QtWidgets.QPushButton(Form)
        self.pushButton_324.setObjectName("pushButton_324")
        self.horizontalLayout_rt12.addWidget(self.pushButton_324)
        self.pushButton_325 = QtWidgets.QPushButton(Form)
        self.pushButton_325.setObjectName("pushButton_325")
        self.horizontalLayout_rt12.addWidget(self.pushButton_325)
        self.pushButton_326 = QtWidgets.QPushButton(Form)
        self.pushButton_326.setObjectName("pushButton_326")
        self.horizontalLayout_rt12.addWidget(self.pushButton_326)
        self.pushButton_327 = QtWidgets.QPushButton(Form)
        self.pushButton_327.setObjectName("pushButton_327")
        self.horizontalLayout_rt12.addWidget(self.pushButton_327)
        self.pushButton_328 = QtWidgets.QPushButton(Form)
        self.pushButton_328.setObjectName("pushButton_328")
        self.horizontalLayout_rt12.addWidget(self.pushButton_328)
        self.pushButton_329 = QtWidgets.QPushButton(Form)
        self.pushButton_329.setObjectName("pushButton_329")
        self.horizontalLayout_rt12.addWidget(self.pushButton_329)
        self.pushButton_3210 = QtWidgets.QPushButton(Form)
        self.pushButton_3210.setObjectName("pushButton_3210")
        self.horizontalLayout_rt12.addWidget(self.pushButton_3210)
        self.pushButton_3211 = QtWidgets.QPushButton(Form)
        self.pushButton_3211.setObjectName("pushButton_3211")
        self.horizontalLayout_rt12.addWidget(self.pushButton_3211)
        self.pushButton_3212 = QtWidgets.QPushButton(Form)
        self.pushButton_3212.setObjectName("pushButton_3212")
        self.horizontalLayout_rt12.addWidget(self.pushButton_3212)
        self.pushButton_3213 = QtWidgets.QPushButton(Form)
        self.pushButton_3213.setObjectName("pushButton_3213")
        self.horizontalLayout_rt12.addWidget(self.pushButton_3213)
        self.pushButton_3214 = QtWidgets.QPushButton(Form)
        self.pushButton_3214.setObjectName("pushButton_3214")
        self.horizontalLayout_rt12.addWidget(self.pushButton_3214)
        self.pushButton_3215 = QtWidgets.QPushButton(Form)
        self.pushButton_3215.setObjectName("pushButton_3215")
        self.horizontalLayout_rt12.addWidget(self.pushButton_3215)
        self.pushButton_3216 = QtWidgets.QPushButton(Form)
        self.pushButton_3216.setObjectName("pushButton_3216")
        self.horizontalLayout_rt12.addWidget(self.pushButton_3216)
        self.pushButton_3217 = QtWidgets.QPushButton(Form)
        self.pushButton_3217.setObjectName("pushButton_3217")
        self.horizontalLayout_rt12.addWidget(self.pushButton_3217)
        self.pushButton_3218 = QtWidgets.QPushButton(Form)
        self.pushButton_3218.setObjectName("pushButton_3218")
        self.horizontalLayout_rt12.addWidget(self.pushButton_3218)
        self.pushButton_3219 = QtWidgets.QPushButton(Form)
        self.pushButton_3219.setObjectName("pushButton_3219")
        self.horizontalLayout_rt12.addWidget(self.pushButton_3219)
        self.pushButton_3220 = QtWidgets.QPushButton(Form)
        self.pushButton_3220.setObjectName("pushButton_3220")
        self.horizontalLayout_rt12.addWidget(self.pushButton_3220)
        self.pushButton_3221 = QtWidgets.QPushButton(Form)
        self.pushButton_3221.setObjectName("pushButton_3221")
        self.horizontalLayout_rt12.addWidget(self.pushButton_3221)
        self.pushButton_3222 = QtWidgets.QPushButton(Form)
        self.pushButton_3222.setObjectName("pushButton_3222")
        self.horizontalLayout_rt12.addWidget(self.pushButton_3222)
        self.pushButton_3223 = QtWidgets.QPushButton(Form)
        self.pushButton_3223.setObjectName("pushButton_3223")
        self.horizontalLayout_rt12.addWidget(self.pushButton_3223)
        self.pushButton_3224 = QtWidgets.QPushButton(Form)
        self.pushButton_3224.setObjectName("pushButton_3224")
        self.horizontalLayout_rt12.addWidget(self.pushButton_3224)
        self.pushButton_3225 = QtWidgets.QPushButton(Form)
        self.pushButton_3225.setObjectName("pushButton_3225")
        self.horizontalLayout_rt12.addWidget(self.pushButton_3225)
        self.pushButton_3226 = QtWidgets.QPushButton(Form)
        self.pushButton_3226.setObjectName("pushButton_3226")
        self.horizontalLayout_rt12.addWidget(self.pushButton_3226)
        
        
        
        self.verticalLayout_rt1.addLayout(self.horizontalLayout_rt12)
        self.verticalLayout.addLayout(self.verticalLayout_rt1)
        
        dict["311"] = self.pushButton_311
        dict["312"] = self.pushButton_312
        dict["313"] = self.pushButton_313
        dict["314"] = self.pushButton_314
        dict["315"] = self.pushButton_315
        dict["316"] = self.pushButton_316
        dict["317"] = self.pushButton_317
        dict["318"] = self.pushButton_318
        dict["319"] = self.pushButton_319
        dict["3110"] = self.pushButton_3110
        dict["3111"] = self.pushButton_3111
        dict["3112"] = self.pushButton_3112
        dict["3113"] = self.pushButton_3113
        dict["3114"] = self.pushButton_3114
        dict["3115"] = self.pushButton_3115
        dict["3116"] = self.pushButton_3116
        dict["3117"] = self.pushButton_3117
        dict["3118"] = self.pushButton_3118
        dict["3119"] = self.pushButton_3119
        dict["3120"] = self.pushButton_3120
        dict["3121"] = self.pushButton_3121
        dict["3122"] = self.pushButton_3122
        dict["3123"] = self.pushButton_3123
        dict["3124"] = self.pushButton_3124
        dict["3125"] = self.pushButton_3125 
        dict["3126"] = self.pushButton_3126  
        
        
        dict["321"] = self.pushButton_321
        dict["322"] = self.pushButton_322
        dict["323"] = self.pushButton_323
        dict["324"] = self.pushButton_324
        dict["325"] = self.pushButton_325
        dict["326"] = self.pushButton_326
        dict["327"] = self.pushButton_327
        dict["328"] = self.pushButton_328
        dict["329"] = self.pushButton_329
        dict["3210"] = self.pushButton_3210
        dict["3211"] = self.pushButton_3211
        dict["3212"] = self.pushButton_3212
        dict["3213"] = self.pushButton_3213
        dict["3214"] = self.pushButton_3214
        dict["3215"] = self.pushButton_3215
        dict["3216"] = self.pushButton_3216
        dict["3217"] = self.pushButton_3217
        dict["3218"] = self.pushButton_3218
        dict["3219"] = self.pushButton_3219
        dict["3220"] = self.pushButton_3220
        dict["3221"] = self.pushButton_3221
        dict["3222"] = self.pushButton_3222
        dict["3223"] = self.pushButton_3223
        dict["3224"] = self.pushButton_3224
        dict["3225"] = self.pushButton_3225
        dict["3226"] = self.pushButton_3226  
        
        ##########################################################
        self.verticalLayout_rt2.setObjectName("verticalLayout_rt2")
        
        self.titre = QtWidgets.QLabel()
        self.titre.setText("Rotor 2")
        self.verticalLayout_rt2.addWidget(self.titre)
        
        self.horizontalLayout_rt21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_rt21.setObjectName("horizontalLayout_rt21")
        self.pushButton_211 = QtWidgets.QPushButton(Form)
        self.pushButton_211.setObjectName("pushButton_211")
        self.horizontalLayout_rt21.addWidget(self.pushButton_211)
        
        self.pushButton_212 = QtWidgets.QPushButton(Form)
        self.pushButton_212.setObjectName("pushButton_212")
        self.horizontalLayout_rt21.addWidget(self.pushButton_212)
        self.pushButton_213 = QtWidgets.QPushButton(Form)
        self.pushButton_213.setObjectName("pushButton_213")
        self.horizontalLayout_rt21.addWidget(self.pushButton_213)
        self.pushButton_214 = QtWidgets.QPushButton(Form)
        self.pushButton_214.setObjectName("pushButton_214")
        self.horizontalLayout_rt21.addWidget(self.pushButton_214)
        self.pushButton_215 = QtWidgets.QPushButton(Form)
        self.pushButton_215.setObjectName("pushButton_215")
        self.horizontalLayout_rt21.addWidget(self.pushButton_215)
        self.pushButton_216 = QtWidgets.QPushButton(Form)
        self.pushButton_216.setObjectName("pushButton_216")
        self.horizontalLayout_rt21.addWidget(self.pushButton_216)
        self.pushButton_217 = QtWidgets.QPushButton(Form)
        self.pushButton_217.setObjectName("pushButton_217")
        self.horizontalLayout_rt21.addWidget(self.pushButton_217)
        self.pushButton_218 = QtWidgets.QPushButton(Form)
        self.pushButton_218.setObjectName("pushButton_218")
        self.horizontalLayout_rt21.addWidget(self.pushButton_218)
        self.pushButton_219 = QtWidgets.QPushButton(Form)
        self.pushButton_219.setObjectName("pushButton_219")
        self.horizontalLayout_rt21.addWidget(self.pushButton_219)
        self.pushButton_2110 = QtWidgets.QPushButton(Form)
        self.pushButton_2110.setObjectName("pushButton_2110")
        self.horizontalLayout_rt21.addWidget(self.pushButton_2110)
        self.pushButton_2111 = QtWidgets.QPushButton(Form)
        self.pushButton_2111.setObjectName("pushButton_2111")
        self.horizontalLayout_rt21.addWidget(self.pushButton_2111)
        self.pushButton_2112 = QtWidgets.QPushButton(Form)
        self.pushButton_2112.setObjectName("pushButton_2112")
        self.horizontalLayout_rt21.addWidget(self.pushButton_2112)
        self.pushButton_2113 = QtWidgets.QPushButton(Form)
        self.pushButton_2113.setObjectName("pushButton_2113")
        self.horizontalLayout_rt21.addWidget(self.pushButton_2113)
        self.pushButton_2114 = QtWidgets.QPushButton(Form)
        self.pushButton_2114.setObjectName("pushButton_2114")
        self.horizontalLayout_rt21.addWidget(self.pushButton_2114)
        self.pushButton_2115 = QtWidgets.QPushButton(Form)
        self.pushButton_2115.setObjectName("pushButton_2115")
        self.horizontalLayout_rt21.addWidget(self.pushButton_2115)
        self.pushButton_2116 = QtWidgets.QPushButton(Form)
        self.pushButton_2116.setObjectName("pushButton_2116")
        self.horizontalLayout_rt21.addWidget(self.pushButton_2116)
        self.pushButton_2117 = QtWidgets.QPushButton(Form)
        self.pushButton_2117.setObjectName("pushButton_2117")
        self.horizontalLayout_rt21.addWidget(self.pushButton_2117)
        self.pushButton_2118 = QtWidgets.QPushButton(Form)
        self.pushButton_2118.setObjectName("pushButton_2118")
        self.horizontalLayout_rt21.addWidget(self.pushButton_2118)
        self.pushButton_2119 = QtWidgets.QPushButton(Form)
        self.pushButton_2119.setObjectName("pushButton_2119")
        self.horizontalLayout_rt21.addWidget(self.pushButton_2119)
        self.pushButton_2120 = QtWidgets.QPushButton(Form)
        self.pushButton_2120.setObjectName("pushButton_2120")
        self.horizontalLayout_rt21.addWidget(self.pushButton_2120)
        self.pushButton_2121 = QtWidgets.QPushButton(Form)
        self.pushButton_2121.setObjectName("pushButton_2121")
        self.horizontalLayout_rt21.addWidget(self.pushButton_2121)
        self.pushButton_2122 = QtWidgets.QPushButton(Form)
        self.pushButton_2122.setObjectName("pushButton_2122")
        self.horizontalLayout_rt21.addWidget(self.pushButton_2122)
        self.pushButton_2123 = QtWidgets.QPushButton(Form)
        self.pushButton_2123.setObjectName("pushButton_2123")
        self.horizontalLayout_rt21.addWidget(self.pushButton_2123)
        self.pushButton_2124 = QtWidgets.QPushButton(Form)
        self.pushButton_2124.setObjectName("pushButton_2124")
        self.horizontalLayout_rt21.addWidget(self.pushButton_2124)
        self.pushButton_2125 = QtWidgets.QPushButton(Form)
        self.pushButton_2125.setObjectName("pushButton_2125")
        self.horizontalLayout_rt21.addWidget(self.pushButton_2125)
        self.pushButton_2126 = QtWidgets.QPushButton(Form)
        self.pushButton_2126.setObjectName("pushButton_2126")
        self.horizontalLayout_rt21.addWidget(self.pushButton_2126)
        self.verticalLayout_rt2.addLayout(self.horizontalLayout_rt21)
        
        
        
        self.horizontalLayout_rt22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_rt22.setObjectName("horizontalLayout_rt22")
        self.pushButton_221 = QtWidgets.QPushButton(Form)
        self.pushButton_221.setObjectName("pushButton_221")
        self.horizontalLayout_rt22.addWidget(self.pushButton_221)
        self.pushButton_222 = QtWidgets.QPushButton(Form)
        self.pushButton_222.setObjectName("pushButton_222")
        self.horizontalLayout_rt22.addWidget(self.pushButton_222)
        self.pushButton_223 = QtWidgets.QPushButton(Form)
        self.pushButton_223.setObjectName("pushButton_223")
        self.horizontalLayout_rt22.addWidget(self.pushButton_223)
        self.pushButton_224 = QtWidgets.QPushButton(Form)
        self.pushButton_224.setObjectName("pushButton_224")
        self.horizontalLayout_rt22.addWidget(self.pushButton_224)
        self.pushButton_225 = QtWidgets.QPushButton(Form)
        self.pushButton_225.setObjectName("pushButton_225")
        self.horizontalLayout_rt22.addWidget(self.pushButton_225)
        self.pushButton_226 = QtWidgets.QPushButton(Form)
        self.pushButton_226.setObjectName("pushButton_226")
        self.horizontalLayout_rt22.addWidget(self.pushButton_226)
        self.pushButton_227 = QtWidgets.QPushButton(Form)
        self.pushButton_227.setObjectName("pushButton_227")
        self.horizontalLayout_rt22.addWidget(self.pushButton_227)
        self.pushButton_228 = QtWidgets.QPushButton(Form)
        self.pushButton_228.setObjectName("pushButton_228")
        self.horizontalLayout_rt22.addWidget(self.pushButton_228)
        self.pushButton_229 = QtWidgets.QPushButton(Form)
        self.pushButton_229.setObjectName("pushButton_229")
        self.horizontalLayout_rt22.addWidget(self.pushButton_229)
        self.pushButton_2210 = QtWidgets.QPushButton(Form)
        self.pushButton_2210.setObjectName("pushButton_2210")
        self.horizontalLayout_rt22.addWidget(self.pushButton_2210)
        self.pushButton_2211 = QtWidgets.QPushButton(Form)
        self.pushButton_2211.setObjectName("pushButton_2211")
        self.horizontalLayout_rt22.addWidget(self.pushButton_2211)
        self.pushButton_2212 = QtWidgets.QPushButton(Form)
        self.pushButton_2212.setObjectName("pushButton_2212")
        self.horizontalLayout_rt22.addWidget(self.pushButton_2212)
        self.pushButton_2213 = QtWidgets.QPushButton(Form)
        self.pushButton_2213.setObjectName("pushButton_2213")
        self.horizontalLayout_rt22.addWidget(self.pushButton_2213)
        self.pushButton_2214 = QtWidgets.QPushButton(Form)
        self.pushButton_2214.setObjectName("pushButton_2214")
        self.horizontalLayout_rt22.addWidget(self.pushButton_2214)
        self.pushButton_2215 = QtWidgets.QPushButton(Form)
        self.pushButton_2215.setObjectName("pushButton_2215")
        self.horizontalLayout_rt22.addWidget(self.pushButton_2215)
        self.pushButton_2216 = QtWidgets.QPushButton(Form)
        self.pushButton_2216.setObjectName("pushButton_2216")
        self.horizontalLayout_rt22.addWidget(self.pushButton_2216)
        self.pushButton_2217 = QtWidgets.QPushButton(Form)
        self.pushButton_2217.setObjectName("pushButton_2217")
        self.horizontalLayout_rt22.addWidget(self.pushButton_2217)
        self.pushButton_2218 = QtWidgets.QPushButton(Form)
        self.pushButton_2218.setObjectName("pushButton_2218")
        self.horizontalLayout_rt22.addWidget(self.pushButton_2218)
        self.pushButton_2219 = QtWidgets.QPushButton(Form)
        self.pushButton_2219.setObjectName("pushButton_2219")
        self.horizontalLayout_rt22.addWidget(self.pushButton_2219)
        self.pushButton_2220 = QtWidgets.QPushButton(Form)
        self.pushButton_2220.setObjectName("pushButton_2220")
        self.horizontalLayout_rt22.addWidget(self.pushButton_2220)
        self.pushButton_2221 = QtWidgets.QPushButton(Form)
        self.pushButton_2221.setObjectName("pushButton_2221")
        self.horizontalLayout_rt22.addWidget(self.pushButton_2221)
        self.pushButton_2222 = QtWidgets.QPushButton(Form)
        self.pushButton_2222.setObjectName("pushButton_2222")
        self.horizontalLayout_rt22.addWidget(self.pushButton_2222)
        self.pushButton_2223 = QtWidgets.QPushButton(Form)
        self.pushButton_2223.setObjectName("pushButton_2223")
        self.horizontalLayout_rt22.addWidget(self.pushButton_2223)
        self.pushButton_2224 = QtWidgets.QPushButton(Form)
        self.pushButton_2224.setObjectName("pushButton_2224")
        self.horizontalLayout_rt22.addWidget(self.pushButton_2224)
        self.pushButton_2225 = QtWidgets.QPushButton(Form)
        self.pushButton_2225.setObjectName("pushButton_2225")
        self.horizontalLayout_rt22.addWidget(self.pushButton_2225)
        self.pushButton_2226 = QtWidgets.QPushButton(Form)
        self.pushButton_2226.setObjectName("pushButton_2226")
        self.horizontalLayout_rt22.addWidget(self.pushButton_2226)
        self.verticalLayout_rt2.addLayout(self.horizontalLayout_rt22)
        self.verticalLayout.addLayout(self.verticalLayout_rt2)
        
        

        dict["211"] = self.pushButton_211
        dict["212"] = self.pushButton_212
        dict["213"] = self.pushButton_213
        dict["214"] = self.pushButton_214
        dict["215"] = self.pushButton_215
        dict["216"] = self.pushButton_216
        dict["217"] = self.pushButton_217
        dict["218"] = self.pushButton_218
        dict["219"] = self.pushButton_219
        dict["2110"] = self.pushButton_2110
        dict["2111"] = self.pushButton_2111
        dict["2112"] = self.pushButton_2112
        dict["2113"] = self.pushButton_2113
        dict["2114"] = self.pushButton_2114
        dict["2115"] = self.pushButton_2115
        dict["2116"] = self.pushButton_2116
        dict["2117"] = self.pushButton_2117
        dict["2118"] = self.pushButton_2118
        dict["2119"] = self.pushButton_2119
        dict["2120"] = self.pushButton_2120
        dict["2121"] = self.pushButton_2121
        dict["2122"] = self.pushButton_2122
        dict["2123"] = self.pushButton_2123
        dict["2124"] = self.pushButton_2124
        dict["2125"] = self.pushButton_2125
        dict["2126"] = self.pushButton_2126
        
        dict["221"] = self.pushButton_221
        dict["222"] = self.pushButton_222
        dict["223"] = self.pushButton_223
        dict["224"] = self.pushButton_224
        dict["225"] = self.pushButton_225
        dict["226"] = self.pushButton_226
        dict["227"] = self.pushButton_227
        dict["228"] = self.pushButton_228
        dict["229"] = self.pushButton_229
        dict["2210"] = self.pushButton_2210
        dict["2211"] = self.pushButton_2211
        dict["2212"] = self.pushButton_2212
        dict["2213"] = self.pushButton_2213
        dict["2214"] = self.pushButton_2214
        dict["2215"] = self.pushButton_2215
        dict["2216"] = self.pushButton_2216
        dict["2217"] = self.pushButton_2217
        dict["2218"] = self.pushButton_2218
        dict["2219"] = self.pushButton_2219
        dict["2220"] = self.pushButton_2220
        dict["2221"] = self.pushButton_2221
        dict["2222"] = self.pushButton_2222
        dict["2223"] = self.pushButton_2223
        dict["2224"] = self.pushButton_2224
        dict["2225"] = self.pushButton_2225
        dict["2226"] = self.pushButton_2226
        
        ############################################################
        #############" rotor 1 EDIT 2  3 OBJET #################
        
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        
        self.titre = QtWidgets.QLabel()
        self.titre.setText("Rotor 1")
        self.verticalLayout_6.addWidget(self.titre)
        
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_111 = QtWidgets.QPushButton(Form)
        self.pushButton_111.setObjectName("pushButton_111")
        self.horizontalLayout_8.addWidget(self.pushButton_111)
        self.pushButton_112 = QtWidgets.QPushButton(Form)
        self.pushButton_112.setObjectName("pushButton_112")
        self.horizontalLayout_8.addWidget(self.pushButton_112)
        self.pushButton_113 = QtWidgets.QPushButton(Form)
        self.pushButton_113.setObjectName("pushButton_113")
        self.horizontalLayout_8.addWidget(self.pushButton_113)
        self.pushButton_114 = QtWidgets.QPushButton(Form)
        self.pushButton_114.setObjectName("pushButton_114")
        self.horizontalLayout_8.addWidget(self.pushButton_114)
        self.pushButton_115 = QtWidgets.QPushButton(Form)
        self.pushButton_115.setObjectName("pushButton_115")
        self.horizontalLayout_8.addWidget(self.pushButton_115)
        self.pushButton_116 = QtWidgets.QPushButton(Form)
        self.pushButton_116.setObjectName("pushButton_116")
        self.horizontalLayout_8.addWidget(self.pushButton_116)
        self.pushButton_117 = QtWidgets.QPushButton(Form)
        self.pushButton_117.setObjectName("pushButton_117")
        self.horizontalLayout_8.addWidget(self.pushButton_117)
        self.pushButton_118 = QtWidgets.QPushButton(Form)
        self.pushButton_118.setObjectName("pushButton_118")
        self.horizontalLayout_8.addWidget(self.pushButton_118)
        self.pushButton_119 = QtWidgets.QPushButton(Form)
        self.pushButton_119.setObjectName("pushButton_119")
        self.horizontalLayout_8.addWidget(self.pushButton_119)
        self.pushButton_1110 = QtWidgets.QPushButton(Form)
        self.pushButton_1110.setObjectName("pushButton_1110")
        self.horizontalLayout_8.addWidget(self.pushButton_1110)
        self.pushButton_1111 = QtWidgets.QPushButton(Form)
        self.pushButton_1111.setObjectName("pushButton_1111")
        self.horizontalLayout_8.addWidget(self.pushButton_1111)
        self.pushButton_1112 = QtWidgets.QPushButton(Form)
        self.pushButton_1112.setObjectName("pushButton_1112")
        self.horizontalLayout_8.addWidget(self.pushButton_1112)
        self.pushButton_1113 = QtWidgets.QPushButton(Form)
        self.pushButton_1113.setObjectName("pushButton_1113")
        self.horizontalLayout_8.addWidget(self.pushButton_1113)
        self.pushButton_1114 = QtWidgets.QPushButton(Form)
        self.pushButton_1114.setObjectName("pushButton_1114")
        self.horizontalLayout_8.addWidget(self.pushButton_1114)
        self.pushButton_1115 = QtWidgets.QPushButton(Form)
        self.pushButton_1115.setObjectName("pushButton_1115")
        self.horizontalLayout_8.addWidget(self.pushButton_1115)
        self.pushButton_1116 = QtWidgets.QPushButton(Form)
        self.pushButton_1116.setObjectName("pushButton_1116")
        self.horizontalLayout_8.addWidget(self.pushButton_1116)
        self.pushButton_1117 = QtWidgets.QPushButton(Form)
        self.pushButton_1117.setObjectName("pushButton_1117")
        self.horizontalLayout_8.addWidget(self.pushButton_1117)
        self.pushButton_1118 = QtWidgets.QPushButton(Form)
        self.pushButton_1118.setObjectName("pushButton_1118")
        self.horizontalLayout_8.addWidget(self.pushButton_1118)
        self.pushButton_1119 = QtWidgets.QPushButton(Form)
        self.pushButton_1119.setObjectName("pushButton_1119")
        self.horizontalLayout_8.addWidget(self.pushButton_1119)
        self.pushButton_1120 = QtWidgets.QPushButton(Form)
        self.pushButton_1120.setObjectName("pushButton_1120")
        self.horizontalLayout_8.addWidget(self.pushButton_1120)
        self.pushButton_1121 = QtWidgets.QPushButton(Form)
        self.pushButton_1121.setObjectName("pushButton_1121")
        self.horizontalLayout_8.addWidget(self.pushButton_1121)
        self.pushButton_1122 = QtWidgets.QPushButton(Form)
        self.pushButton_1122.setObjectName("pushButton_1122")
        self.horizontalLayout_8.addWidget(self.pushButton_1122)
        self.pushButton_1123 = QtWidgets.QPushButton(Form)
        self.pushButton_1123.setObjectName("pushButton_1123")
        self.horizontalLayout_8.addWidget(self.pushButton_1123)
        self.pushButton_1124 = QtWidgets.QPushButton(Form)
        self.pushButton_1124.setObjectName("pushButton_1124")
        self.horizontalLayout_8.addWidget(self.pushButton_1124)
        self.pushButton_1125 = QtWidgets.QPushButton(Form)
        self.pushButton_1125.setObjectName("pushButton_1125")
        self.horizontalLayout_8.addWidget(self.pushButton_1125)
        self.pushButton_1126 = QtWidgets.QPushButton(Form)
        self.pushButton_1126.setObjectName("pushButton_1126")
        self.horizontalLayout_8.addWidget(self.pushButton_1126)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_121 = QtWidgets.QPushButton(Form)
        
        
        
        self.pushButton_121.setObjectName("pushButton_121")
        self.horizontalLayout_9.addWidget(self.pushButton_121)
        self.pushButton_122 = QtWidgets.QPushButton(Form)
        self.pushButton_122.setObjectName("pushButton_122")
        self.horizontalLayout_9.addWidget(self.pushButton_122)
        self.pushButton_123 = QtWidgets.QPushButton(Form)
        self.pushButton_123.setObjectName("pushButton_123")
        self.horizontalLayout_9.addWidget(self.pushButton_123)
        self.pushButton_124 = QtWidgets.QPushButton(Form)
        self.pushButton_124.setObjectName("pushButton_124")
        self.horizontalLayout_9.addWidget(self.pushButton_124)
        self.pushButton_125 = QtWidgets.QPushButton(Form)
        self.pushButton_125.setObjectName("pushButton_125")
        self.horizontalLayout_9.addWidget(self.pushButton_125)
        self.pushButton_126 = QtWidgets.QPushButton(Form)
        self.pushButton_126.setObjectName("pushButton_126")
        self.horizontalLayout_9.addWidget(self.pushButton_126)
        self.pushButton_127 = QtWidgets.QPushButton(Form)
        self.pushButton_127.setObjectName("pushButton_127")
        self.horizontalLayout_9.addWidget(self.pushButton_127)
        self.pushButton_128 = QtWidgets.QPushButton(Form)
        self.pushButton_128.setObjectName("pushButton_128")
        self.horizontalLayout_9.addWidget(self.pushButton_128)
        self.pushButton_129 = QtWidgets.QPushButton(Form)
        self.pushButton_129.setObjectName("pushButton_129")
        self.horizontalLayout_9.addWidget(self.pushButton_129)
        self.pushButton_1210 = QtWidgets.QPushButton(Form)
        self.pushButton_1210.setObjectName("pushButton_1210")
        self.horizontalLayout_9.addWidget(self.pushButton_1210)
        self.pushButton_1211 = QtWidgets.QPushButton(Form)
        self.pushButton_1211.setObjectName("pushButton_1211")
        self.horizontalLayout_9.addWidget(self.pushButton_1211)
        self.pushButton_1212 = QtWidgets.QPushButton(Form)
        self.pushButton_1212.setObjectName("pushButton_1212")
        self.horizontalLayout_9.addWidget(self.pushButton_1212)
        self.pushButton_1213 = QtWidgets.QPushButton(Form)
        self.pushButton_1213.setObjectName("pushButton_1213")
        self.horizontalLayout_9.addWidget(self.pushButton_1213)
        self.pushButton_1214 = QtWidgets.QPushButton(Form)
        self.pushButton_1214.setObjectName("pushButton_1214")
        self.horizontalLayout_9.addWidget(self.pushButton_1214)
        self.pushButton_1215 = QtWidgets.QPushButton(Form)
        self.pushButton_1215.setObjectName("pushButton_1215")
        self.horizontalLayout_9.addWidget(self.pushButton_1215)
        self.pushButton_1216 = QtWidgets.QPushButton(Form)
        self.pushButton_1216.setObjectName("pushButton_1216")
        self.horizontalLayout_9.addWidget(self.pushButton_1216)
        self.pushButton_1217 = QtWidgets.QPushButton(Form)
        self.pushButton_1217.setObjectName("pushButton_1217")
        self.horizontalLayout_9.addWidget(self.pushButton_1217)
        self.pushButton_1218 = QtWidgets.QPushButton(Form)
        self.pushButton_1218.setObjectName("pushButton_1218")
        self.horizontalLayout_9.addWidget(self.pushButton_1218)
        self.pushButton_1219 = QtWidgets.QPushButton(Form)
        self.pushButton_1219.setObjectName("pushButton_1219")
        self.horizontalLayout_9.addWidget(self.pushButton_1219)
        self.pushButton_1220 = QtWidgets.QPushButton(Form)
        self.pushButton_1220.setObjectName("pushButton_1220")
        self.horizontalLayout_9.addWidget(self.pushButton_1220)
        self.pushButton_1221 = QtWidgets.QPushButton(Form)
        self.pushButton_1221.setObjectName("pushButton_1221")
        self.horizontalLayout_9.addWidget(self.pushButton_1221)
        self.pushButton_1222 = QtWidgets.QPushButton(Form)
        self.pushButton_1222.setObjectName("pushButton_1222")
        self.horizontalLayout_9.addWidget(self.pushButton_1222)
        self.pushButton_1223 = QtWidgets.QPushButton(Form)
        self.pushButton_1223.setObjectName("pushButton_1223")
        self.horizontalLayout_9.addWidget(self.pushButton_1223)
        self.pushButton_1224 = QtWidgets.QPushButton(Form)
        self.pushButton_1224.setObjectName("pushButton_1224")
        self.horizontalLayout_9.addWidget(self.pushButton_1224)
        self.pushButton_1225 = QtWidgets.QPushButton(Form)
        self.pushButton_1225.setObjectName("pushButton_1225")
        self.horizontalLayout_9.addWidget(self.pushButton_1225)
        self.pushButton_1226 = QtWidgets.QPushButton(Form)
        self.pushButton_1226.setObjectName("pushButton_1226")
        self.horizontalLayout_9.addWidget(self.pushButton_1226)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.verticalLayout.addLayout(self.verticalLayout_6)
        
        dict["111"] = self.pushButton_111
        dict["112"] = self.pushButton_112
        dict["113"] = self.pushButton_113
        dict["114"] = self.pushButton_114
        dict["115"] = self.pushButton_115
        dict["116"] = self.pushButton_116
        dict["117"] = self.pushButton_117
        dict["118"] = self.pushButton_118
        dict["119"] = self.pushButton_119
        dict["1110"] = self.pushButton_1110
        dict["1111"] = self.pushButton_1111
        dict["1112"] = self.pushButton_1112
        dict["1113"] = self.pushButton_1113
        dict["1114"] = self.pushButton_1114
        dict["1115"] = self.pushButton_1115
        dict["1116"] = self.pushButton_1116
        dict["1117"] = self.pushButton_1117
        dict["1118"] = self.pushButton_1118
        dict["1119"] = self.pushButton_1119
        dict["1120"] = self.pushButton_1120
        dict["1121"] = self.pushButton_1121
        dict["1122"] = self.pushButton_1122
        dict["1123"] = self.pushButton_1123
        dict["1124"] = self.pushButton_1124
        dict["1125"] = self.pushButton_1125
        dict["1126"] = self.pushButton_1126
        #####################################
        dict["121"] = self.pushButton_121
        dict["122"] = self.pushButton_122
        dict["123"] = self.pushButton_123
        dict["124"] = self.pushButton_124
        dict["125"] = self.pushButton_125
        dict["126"] = self.pushButton_126
        dict["127"] = self.pushButton_127
        dict["128"] = self.pushButton_128
        dict["129"] = self.pushButton_129
        dict["1210"] = self.pushButton_1210
        dict["1211"] = self.pushButton_1211
        dict["1212"] = self.pushButton_1212
        dict["1213"] = self.pushButton_1213
        dict["1214"] = self.pushButton_1214
        dict["1215"] = self.pushButton_1215
        dict["1216"] = self.pushButton_1216
        dict["1217"] = self.pushButton_1217
        dict["1218"] = self.pushButton_1218
        dict["1219"] = self.pushButton_1219
        dict["1220"] = self.pushButton_1220
        dict["1221"] = self.pushButton_1221
        dict["1222"] = self.pushButton_1222
        dict["1223"] = self.pushButton_1223
        dict["1224"] = self.pushButton_1224
        dict["1225"] = self.pushButton_1225
        dict["1226"] = self.pushButton_1226
        
        
        #####ALphabet lettre a encrypter 
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_A = QtWidgets.QPushButton(Form)
        self.pushButton_A.setObjectName("pushButton_A")
        self.horizontalLayout_5.addWidget(self.pushButton_A)
        self.pushButton_B = QtWidgets.QPushButton(Form)
        self.pushButton_B.setObjectName("pushButton_B")
        self.horizontalLayout_5.addWidget(self.pushButton_B)
        self.pushButton_C = QtWidgets.QPushButton(Form)
        self.pushButton_C.setObjectName("pushButton_C")
        self.horizontalLayout_5.addWidget(self.pushButton_C)
        self.pushButton_D = QtWidgets.QPushButton(Form)
        self.pushButton_D.setObjectName("pushButton_D")
        self.horizontalLayout_5.addWidget(self.pushButton_D)
        self.pushButton_E = QtWidgets.QPushButton(Form)
        self.pushButton_E.setObjectName("pushButton_E")
        self.horizontalLayout_5.addWidget(self.pushButton_E)
        self.pushButton_F = QtWidgets.QPushButton(Form)
        self.pushButton_F.setObjectName("pushButton_F")
        self.horizontalLayout_5.addWidget(self.pushButton_F)
        self.pushButton_G = QtWidgets.QPushButton(Form)
        self.pushButton_G.setObjectName("pushButton_G")
        self.horizontalLayout_5.addWidget(self.pushButton_G)
        self.pushButton_H = QtWidgets.QPushButton(Form)
        self.pushButton_H.setObjectName("pushButton_H")
        self.horizontalLayout_5.addWidget(self.pushButton_H)
        self.pushButton_I = QtWidgets.QPushButton(Form)
        self.pushButton_I.setObjectName("pushButton_I")
        self.horizontalLayout_5.addWidget(self.pushButton_I)
        self.pushButton_J = QtWidgets.QPushButton(Form)
        self.pushButton_J.setObjectName("pushButton_J")
        self.horizontalLayout_5.addWidget(self.pushButton_J)
        self.pushButton_K = QtWidgets.QPushButton(Form)
        self.pushButton_K.setObjectName("pushButton_K")
        self.horizontalLayout_5.addWidget(self.pushButton_K)
        self.pushButton_L = QtWidgets.QPushButton(Form)
        self.pushButton_L.setObjectName("pushButton_L")
        self.horizontalLayout_5.addWidget(self.pushButton_L)
        self.pushButton_M = QtWidgets.QPushButton(Form)
        self.pushButton_M.setObjectName("pushButton_M")
        self.horizontalLayout_5.addWidget(self.pushButton_M)
        self.pushButton_N = QtWidgets.QPushButton(Form)
        self.pushButton_N.setObjectName("pushButton_N")
        self.horizontalLayout_5.addWidget(self.pushButton_N)
        self.pushButton_O = QtWidgets.QPushButton(Form)
        self.pushButton_O.setObjectName("pushButton_O")
        self.horizontalLayout_5.addWidget(self.pushButton_O)
        self.pushButton_P = QtWidgets.QPushButton(Form)
        self.pushButton_P.setObjectName("pushButton_P")
        self.horizontalLayout_5.addWidget(self.pushButton_P)
        self.pushButton_Q = QtWidgets.QPushButton(Form)
        self.pushButton_Q.setObjectName("pushButton_Q")
        self.horizontalLayout_5.addWidget(self.pushButton_Q)
        self.pushButton_R = QtWidgets.QPushButton(Form)
        self.pushButton_R.setObjectName("pushButton_R")
        self.horizontalLayout_5.addWidget(self.pushButton_R)
        self.pushButton_S = QtWidgets.QPushButton(Form)
        self.pushButton_S.setObjectName("pushButton_S")
        self.horizontalLayout_5.addWidget(self.pushButton_S)
        
        self.pushButton_T = QtWidgets.QPushButton(Form)
        self.pushButton_T.setObjectName("pushButton_T")
        self.horizontalLayout_5.addWidget(self.pushButton_T)
        
        self.pushButton_U = QtWidgets.QPushButton(Form)
        self.pushButton_U.setObjectName("pushButton_U")
        self.horizontalLayout_5.addWidget(self.pushButton_U)
        
        self.pushButton_V = QtWidgets.QPushButton(Form)
        self.pushButton_V.setObjectName("pushButton_V")
        self.horizontalLayout_5.addWidget(self.pushButton_V)
        
        self.pushButton_W = QtWidgets.QPushButton(Form)
        self.pushButton_W.setObjectName("pushButton_W")
        self.horizontalLayout_5.addWidget(self.pushButton_W)
        
        self.pushButton_X = QtWidgets.QPushButton(Form)
        self.pushButton_X.setObjectName("pushButton_X")
        self.horizontalLayout_5.addWidget(self.pushButton_X)
        
        self.pushButton_Y = QtWidgets.QPushButton(Form)
        self.pushButton_Y.setObjectName("pushButton_Y")
        self.horizontalLayout_5.addWidget(self.pushButton_Y)
        
        self.pushButton_Z = QtWidgets.QPushButton(Form)
        self.pushButton_Z.setObjectName("pushButton_Z")
        self.horizontalLayout_5.addWidget(self.pushButton_Z)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        
        
        dict["0"] = self.pushButton_A
        dict["1"] = self.pushButton_B
        dict["2"] = self.pushButton_C
        dict["3"] = self.pushButton_D
        dict["4"] = self.pushButton_E
        dict["5"] = self.pushButton_F
        dict["6"] = self.pushButton_G
        dict["7"] = self.pushButton_H
        dict["8"] = self.pushButton_I
        dict["9"] = self.pushButton_J
        dict["10"] = self.pushButton_K
        dict["11"] = self.pushButton_L
        dict["12"] = self.pushButton_M
        dict["13"] = self.pushButton_N
        dict["14"] = self.pushButton_O
        dict["15"] = self.pushButton_P
        dict["16"] = self.pushButton_Q
        dict["17"] = self.pushButton_R
        dict["18"] = self.pushButton_S
        dict["19"] = self.pushButton_T
        dict["20"] = self.pushButton_U
        dict["21"] = self.pushButton_V
        dict["22"] = self.pushButton_W
        dict["23"] = self.pushButton_X
        dict["24"] = self.pushButton_Y
        dict["25"] = self.pushButton_Z
       ####################
        
        
        
        
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        
        
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 19, 160, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        
        
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_2)
        
        
        
        self.horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider.setMaximum(26)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_3.addWidget(self.horizontalSlider)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        
        app.setStyleSheet('''QSlider::groove:horizontal {
border: 1px solid #bbb;
background: white;
height: 10px;
border-radius: 4px;
}

QSlider::sub-page:horizontal {
background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,
    stop: 0 #66e, stop: 1 #bbf);
background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,
    stop: 0 #bbf, stop: 1 #55f);
border: 1px solid #777;
height: 10px;
border-radius: 4px;
}

QSlider::add-page:horizontal {
background: #fff;
border: 1px solid #777;
height: 10px;
border-radius: 4px;
}

QSlider::handle:horizontal {
background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
    stop:0 #eee, stop:1 #ccc);
border: 1px solid #777;
width: 13px;
margin-top: -2px;
margin-bottom: -2px;
border-radius: 4px;
}

QSlider::handle:horizontal:hover {
background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
    stop:0 #fff, stop:1 #ddd);
border: 1px solid #444;
border-radius: 4px;
}

QSlider::sub-page:horizontal:disabled {
background: #bbb;
border-color: #999;
}

QSlider::add-page:horizontal:disabled {
background: #eee;
border-color: #999;
}

QSlider::handle:horizontal:disabled {
background: #eee;
border: 1px solid #aaa;
border-radius: 4px;
}

QComboBox{
border:                 0.5px solid black;
background-color:   #D7ECD9;
color:                     black;
font-weight:            bold;
padding:                    5px 

}

QComboBox::drop-down{
    border:                 none;
    background-color:   #D7ECD9;
    color:                      rgb(255, 255, 255);
    font-weight:            bold;
    padding:                    0px;
}

QComboBox::down-arrow{
    image:                      url(:/icons/combobox_down_arrow.png);
    padding-right:          5px;
}

QListView{
    border:                 none;
    color:                      rgb(87, 96, 134);
    background-color:   rgb(255, 255, 255);
    font-weight:            bold;
    selection-background-color: rgb(47, 175, 178);
    show-decoration-selected: 1;
    margin-left:                -10px;
    padding-left    :           15px;
}

QListView::item:hover{

    background-color:   rgb(47, 175, 178);
    border:                 none;
}

''')
        
        
        
        
        
       
        
        
        
        self.Slider = self.verticalLayoutWidget.findChild(QtWidgets.QSlider, "horizontalSlider")
        self.horizontalSlider.valueChanged.connect(self.slider_control)
        self.label_slider_1 = self.verticalLayoutWidget.findChild(QtWidgets.QLabel, "label_4")
        
        
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(350, 20, 160, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
    
        
        self.comboBox_3 = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_3.setObjectName("comboBox_3")
        
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.verticalLayout_4.addWidget(self.comboBox_3)
        self.comboBox_4 = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.verticalLayout_4.addWidget(self.comboBox_4)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider_2.setMaximum(26)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.verticalLayout_4.addWidget(self.horizontalSlider_2)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        
        self.Slider_2 = self.verticalLayoutWidget_2.findChild(QtWidgets.QSlider, "horizontalSlider_2")
        self.horizontalSlider_2.valueChanged.connect(self.slider_control_2)
        self.label_slider_2 = self.verticalLayoutWidget_2.findChild(QtWidgets.QLabel, "label_6")
        
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(620, 20, 160, 131))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.comboBox_5 = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.verticalLayout_5.addWidget(self.comboBox_5)
        self.comboBox_6 = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.verticalLayout_5.addWidget(self.comboBox_6)
        self.horizontalSlider_3 = QtWidgets.QSlider(self.verticalLayoutWidget_3)
        self.horizontalSlider_3.setMaximum(26)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.verticalLayout_5.addWidget(self.horizontalSlider_3)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        
        self.Slider_3 = self.verticalLayoutWidget_3.findChild(QtWidgets.QSlider, "horizontalSlider_3")
        self.horizontalSlider_3.valueChanged.connect(self.slider_control_3)
        self.label_slider_3 = self.verticalLayoutWidget_3.findChild(QtWidgets.QLabel, "label_8")
        
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Message = QtWidgets.QGroupBox(Form)
        self.Message.setObjectName("Message")
        self.label_2 = QtWidgets.QLabel(self.Message)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 121, 21))
        self.label_2.setObjectName("label_2")
        
        ###########" message a encrypter"
        self.lineEdit = QtWidgets.QLineEdit(self.Message)
        self.lineEdit.setGeometry(QtCore.QRect(220, 80, 271, 33))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.Message)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        
        
        ########################################
        #######################################
        ###########################################
        ###############################""
        self.pushButton_3.clicked.connect(self.configurer_rotor)
        
        
        self.horizontalLayout_7.addWidget(self.pushButton_3)
        
        ########### bouton encrypter #################
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_7.addWidget(self.pushButton_4)
        
        ################edit here##################
        
        
        
        
        self.pushButton_4.clicked.connect(self.encryption)
        
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_7.addWidget(self.pushButton_2)
        
        self.pushButton_2.clicked.connect(self.rotate)
        
        self.pushButton_4.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        
        
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_7.addWidget(self.pushButton)
        
        self.pushButton.setEnabled(False)
        
        self.horizontalLayout_3.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Resultat = QtWidgets.QGroupBox(Form)
        self.Resultat.setObjectName("Resultat")
        self.label_9 = QtWidgets.QLabel(self.Resultat)
        self.label_9.setGeometry(QtCore.QRect(70, 80, 121, 21))
        self.label_9.setObjectName("label_9")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Resultat)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 80, 271, 33))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.Resultat)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        
        globals()["dict"] = dict

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    
    def slider_control(self):
        
        value = self.Slider.value()
        self.label_slider_1.setText(str(value))
        
    def slider_control_2(self):
        
        value = self.Slider_2.value()
        self.label_slider_2.setText(str(value))
        
    def slider_control_3(self):
        
        value = self.Slider_3.value()
        self.label_slider_3.setText(str(value))
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle("Enigma Simulator")
        
        
        self.pushButton_A.setText(_translate("Form", "A"))
        self.pushButton_B.setText(_translate("Form", "B"))
        self.pushButton_C.setText(_translate("Form", "C"))
        self.pushButton_D.setText(_translate("Form", "D"))
        self.pushButton_E.setText(_translate("Form", "E"))
        self.pushButton_F.setText(_translate("Form", "F"))
        self.pushButton_G.setText(_translate("Form", "G"))
        self.pushButton_H.setText(_translate("Form", "H"))
        self.pushButton_I.setText(_translate("Form", "I"))
        self.pushButton_J.setText(_translate("Form", "J"))
        self.pushButton_K.setText(_translate("Form", "K"))
        self.pushButton_L.setText(_translate("Form", "L"))
        self.pushButton_M.setText(_translate("Form", "M"))
        self.pushButton_N.setText(_translate("Form", "N"))
        self.pushButton_O.setText(_translate("Form", "O"))
        self.pushButton_P.setText(_translate("Form", "P"))
        self.pushButton_Q.setText(_translate("Form", "Q"))
        self.pushButton_R.setText(_translate("Form", "R"))
        self.pushButton_S.setText(_translate("Form", "S"))
        self.pushButton_T.setText(_translate("Form", "T"))
        self.pushButton_U.setText(_translate("Form", "U"))
        self.pushButton_V.setText(_translate("Form", "V"))
        self.pushButton_W.setText(_translate("Form", "W"))
        self.pushButton_X.setText(_translate("Form", "X"))
        self.pushButton_Y.setText(_translate("Form", "Y"))
        self.pushButton_Z.setText(_translate("Form", "Z"))
        self.groupBox_2.setTitle(_translate("Form", "Clé"))
        self.label_3.setText(_translate("Form", "ROTOR 1"))
        self.comboBox.setCurrentText(_translate("Form", "1"))
        self.comboBox.setItemText(0, _translate("Form", "1"))
        self.comboBox.setItemText(1, _translate("Form", "2"))
        self.comboBox.setItemText(2, _translate("Form", "3"))
        self.comboBox_2.setItemText(0, _translate("Form", "D"))
        self.comboBox_2.setItemText(1, _translate("Form", "G"))
        self.label_4.setText(_translate("Form", "0"))
        self.label_5.setText(_translate("Form", "ROTOR 2"))
        
        self.comboBox_3.setCurrentText(_translate("Form", "1"))
        self.comboBox_3.setItemText(0, _translate("Form", "1"))
        self.comboBox_3.setItemText(1, _translate("Form", "2"))
        self.comboBox_3.setItemText(2, _translate("Form", "3"))
        self.comboBox_4.setItemText(0, _translate("Form", "D"))
        self.comboBox_4.setItemText(1, _translate("Form", "G"))
        self.label_6.setText(_translate("Form", "0"))
        self.label_7.setText(_translate("Form", "ROTOR 3"))
        self.comboBox_5.setCurrentText(_translate("Form", "1"))
        self.comboBox_5.setItemText(0, _translate("Form", "1"))
        self.comboBox_5.setItemText(1, _translate("Form", "2"))
        self.comboBox_5.setItemText(2, _translate("Form", "3"))
        self.comboBox_6.setItemText(0, _translate("Form", "D"))
        self.comboBox_6.setItemText(1, _translate("Form", "G"))
        self.label_8.setText(_translate("Form", "0"))
        self.Message.setTitle(_translate("Form", "Message"))
        self.label_2.setText(_translate("Form", "Texte en clair"))
        self.label_2.setStyleSheet("""QLabel{ font-size: 18px;}""")
        self.pushButton_3.setText(_translate("Form", "Configurer"))
        self.pushButton_4.setText(_translate("Form", "Encrypter"))
        self.pushButton_2.setText(_translate("Form", "Etape suivante"))
        self.pushButton.setText(_translate("Form", "Décrypter"))
        self.Resultat.setTitle(_translate("Form", "Résultat :"))
        self.label_9.setText(_translate("Form", "Texte encrypté :"))
        self.label_9.setStyleSheet("""QLabel{ font-size: 18px;}""")
        
        self.pushButton.clicked.connect(self.decryption)
        
        self.pushButton.setStyleSheet("""QPushButton{width: 150px;
height: 30px;
	font-size: 16px;
	font-weight: bold;8color: blacblackackground: whwhite	border: 2px solid;
}
 QPushButton:hover {
	background: gray;
}
QPushButton:disabled {
	background: #453D3B ;
}""")
        self.pushButton_2.setStyleSheet("""QPushButton{width: 150px;
height: 30px;
	font-size: 16px;
	font-weight: bold;8color: blacblackackground: whwhite	border: 2px solid;
}
 QPushButton:hover {
	background: gray;
}
QPushButton:disabled {
	background: #453D3B ;
}""")
        self.pushButton_4.setStyleSheet("""QPushButton{width: 150px;
height: 30px;
	font-size: 16px;
	font-weight: bold;8color: blacblackackground: whwhite	border: 2px solid;
}
 QPushButton:hover {
	background: gray;
}
QPushButton:disabled {
	background: #453D3B ;
}""")
        self.pushButton_3.setStyleSheet("""QPushButton{width: 150px;
height: 30px;
	font-size: 16px;
	font-weight: bold;8color: blacblackackground: whwhite	border: 2px solid;
}
 QPushButton:hover {
	background: gray;
}
""")

        self.lineEdit.setStyleSheet("""QLineEdit{border-radius: 5px;border: 2px solid; height: 25px; font-size : 16px; font-weight: bold;}""")
        self.lineEdit_2.setStyleSheet("""QLineEdit{border-radius: 5px; border: 2px solid; height: 25px; font-size : 16px; font-weight: bold;}""")
        
        
        self.pushButton_111.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_112.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_113.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_114.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_115.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_116.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_117.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_118.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_119.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1110.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1111.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1112.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1113.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1114.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1115.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1116.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1117.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1118.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1119.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1120.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1121.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1122.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1123.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1124.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1125.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1126.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_121.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_122.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_123.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_124.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_125.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_126.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_127.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_128.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_129.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1210.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1211.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1212.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1213.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1214.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1215.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1216.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1217.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1218.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1219.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1220.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1221.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1222.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1223.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1224.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1226.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_1225.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_211.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_212.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_213.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_214.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_215.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_216.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_217.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_218.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_219.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2110.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2111.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2112.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2113.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2114.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2115.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2116.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2117.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2118.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2119.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2120.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2121.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2122.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2123.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2124.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2126.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2125.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_221.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_222.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_223.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_224.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_225.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_226.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_227.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_228.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_229.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2210.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2211.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2212.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2213.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2214.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2215.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2216.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2217.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2218.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2219.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2220.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2221.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2222.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2223.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2224.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2225.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_2226.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_311.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_312.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_313.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_314.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_315.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_316.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_317.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_318.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_319.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3110.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3111.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3112.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3113.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3114.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3115.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3116.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3117.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3118.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3119.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3120.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3121.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3122.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3123.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3124.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3125.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3126.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_321.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_322.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_323.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_324.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_325.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_326.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_327.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_328.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_329.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3210.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3211.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3212.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3213.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3214.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3215.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3216.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3217.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3218.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3219.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3220.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3221.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3222.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3223.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3224.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3225.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        self.pushButton_3226.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
        
        self.pushButton_R1.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: #D7ECD9; border: 1px solid;''')
        self.pushButton_R2.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: #D7ECD9; border: 1px solid;''')
        self.pushButton_R3.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: #D7ECD9; border: 1px solid;''')
        self.pushButton_R4.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: #D7ECD9; border: 1px solid;''')
        self.pushButton_R5.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: #D7ECD9; border: 1px solid;''')
        self.pushButton_R6.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: #D7ECD9; border: 1px solid;''')
        self.pushButton_R7.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: #D7ECD9; border: 1px solid;''')
        self.pushButton_R8.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: #D7ECD9; border: 1px solid;''')
        self.pushButton_R9.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: #D7ECD9; border: 1px solid;''')
        self.pushButton_R10.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: #D7ECD9; border: 1px solid;''')
        self.pushButton_R11.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: #D7ECD9; border: 1px solid;''')
        self.pushButton_R12.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: #D7ECD9; border: 1px solid;''')
        self.pushButton_R13.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: #D7ECD9; border: 1px solid;''')
        self.pushButton_R14.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: #D7ECD9; border: 1px solid;''')
        self.pushButton_R15.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: #D7ECD9; border: 1px solid;''')
        self.pushButton_R16.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: #D7ECD9; border: 1px solid;''')
        self.pushButton_R17.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: #D7ECD9; border: 1px solid;''')
        self.pushButton_R18.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: #D7ECD9; border: 1px solid;''')
        self.pushButton_R19.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: #D7ECD9; border: 1px solid;''')
        self.pushButton_R20.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: #D7ECD9; border: 1px solid;''')
        self.pushButton_R21.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: #D7ECD9; border: 1px solid;''')
        self.pushButton_R22.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: #D7ECD9; border: 1px solid;''')
        self.pushButton_R23.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: #D7ECD9; border: 1px solid;''')
        self.pushButton_R24.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: #D7ECD9; border: 1px solid;''')
        self.pushButton_R25.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: #D7ECD9; border: 1px solid;''')
        self.pushButton_R26.setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: #D7ECD9; border: 1px solid;''')
                
        
        
        self.pushButton_3.setStyleSheet("""QPushButton{border-radius: 5px; border: 2px solid; height: 35px; font-size : 16px; font-weight: bold;}
                                        QPushButton:hover{background-color:#6a635b; border-radius: 5px; border: 2px solid; height: 35px; font-size : 16px; font-weight: bold;}""")
        self.pushButton_4.setStyleSheet("""QPushButton{border-radius: 5px; border: 2px solid; height: 35px; font-size : 16px; font-weight: bold;}
                                        QPushButton:hover{background-color:#6a635b;border-radius: 5px; border: 2px solid; height: 35px; font-size : 16px; font-weight: bold;}""")
        self.pushButton.setStyleSheet("""QPushButton{border-radius: 5px; border: 2px solid; height: 35px; font-size : 16px; font-weight: bold;}
                                      QPushButton:hover{border-radius: 5px; border: 2px solid; height: 35px; font-size : 16px; font-weight: bold;}""")
        self.pushButton_2.setStyleSheet("""QPushButton{border-radius: 5px; border: 2px solid; height: 35px; font-size : 16px; font-weight: bold;}
                                        QPushButton:hover{background-color:#6a635b;background-color:#6a635b;border-radius: 5px; border: 2px solid; height: 35px; font-size : 16px; font-weight: bold;}""")
        
        
    def decryption(self):
        texte = self.lineEdit_2.text().upper()
        self.pushButton_4.setEnabled(False)
        if globals()["increment"] == 0 and texte != '' :
            
            texte = texte.replace(" ", "")
            pos = ord(texte[globals()["text_index"]]) - 65
            
            val_decalage = R11[pos]
            next_R21 = (pos + val_decalage) % 26 
            val_decalage = R21[next_R21]  
            next_R31 = (next_R21 + val_decalage) % 26
            val_decalage = R31[next_R31]
            next_reflecteur = (next_R31+ val_decalage) % 26
            val_decalage = Reflecteur[next_reflecteur]
            blue_R30 = (next_reflecteur + val_decalage) % 26
            val_decalage = R30[blue_R30] 
            blue_R20 = (blue_R30 + val_decalage) % 26
            val_decalage = R20[blue_R20]
            blue_R10 = (blue_R20 + val_decalage) % 26
            val_decalage = R10[blue_R10]
            blue_alphabet = (blue_R10 + val_decalage) % 26
            
            dict[str(pos)].setStyleSheet("background-color : red; color : white; font-size: 16px; font-weight: bold;width : 15px !important;")
            
            dict["12"+ str(pos + 1)].setStyleSheet("background-color : red; color : white; font-size: 16px; font-weight: bold;width : 15px !important;")
            dict["22"+ str(next_R21 + 1)].setStyleSheet("background-color : red; color : white; font-size: 16px; font-weight: bold;width : 15px !important;")
            dict["32"+ str(next_R31 + 1)].setStyleSheet("background-color : red; color : white; font-size: 16px; font-weight: bold;width : 15px !important;")
            
            dict["R"+ str(next_reflecteur + 1)].setStyleSheet("background-color : red; color : white; font-size: 16px; font-weight: bold;width : 15px !important;")
            
            dict["11"+ str(blue_R10 + 1)].setStyleSheet("background-color: #D7ECD9 !important; color : white; font-size: 16px; font-weight: bold;width : 15px !important;")
            dict["21"+ str(blue_R20 + 1)].setStyleSheet("background-color: #D7ECD9 !important; color : white; font-size: 16px; font-weight: bold;width : 15px !important;")
            dict["31"+ str(blue_R30 + 1)].setStyleSheet("background-color: #D7ECD9 !important; color : white; font-size: 16px; font-weight: bold;width : 15px !important;")
            
            dict[str(blue_alphabet)].setStyleSheet("background-color: #D7ECD9 !important; color : white; font-size: 16px; font-weight: bold;width : 15px !important;")
            
            
            encr = alphabet[blue_alphabet]
            
            globals()["texte_crypte"] += encr
            self.lineEdit.setText(globals()["texte_crypte"])
            
            print("encr",encr)
            globals()["increment"] += 1
            globals()["text_index"] += 1 
            
            if len(globals()["texte_crypte"]) == len(texte):
                self.pushButton_4.setEnabled(False)
                self.pushButton_2.setEnabled(False)
            case = {
        "pos": pos,
        "next_R21": next_R21,
        "next_R31": next_R31,
        "next_reflecteur" : next_reflecteur,
        "blue_R30" : blue_R30,
        "blue_R20" : blue_R20,
        "blue_R10" : blue_R10,
        "blue_alphabet" : blue_alphabet,
        "lettre" : alphabet[blue_alphabet]
        }
            globals()["case"] = case
                
        else:
            error = QMessageBox()
            error.setWindowTitle("Erreur")
            error.setText("Veuillez saisir le message à decrypter")
            error.setIcon(QMessageBox.Warning)
            x = error.exec_()
            print("You need to rotate first !")


    def encryption(self):
        texte = self.lineEdit.text().upper()
        self.pushButton.setEnabled(False)
        if globals()["increment"] == 0 and texte !='':
            
            texte = texte.replace(" ", "")
            pos = ord(texte[globals()["text_index"]]) - 65
            
            val_decalage = R11[pos]
            next_R21 = (pos + val_decalage) % 26 
            val_decalage = R21[next_R21]  
            next_R31 = (next_R21 + val_decalage) % 26
            val_decalage = R31[next_R31]
            next_reflecteur = (next_R31+ val_decalage) % 26
            val_decalage = Reflecteur[next_reflecteur]
            blue_R30 = (next_reflecteur + val_decalage) % 26
            val_decalage = R30[blue_R30] 
            blue_R20 = (blue_R30 + val_decalage) % 26
            val_decalage = R20[blue_R20]
            blue_R10 = (blue_R20 + val_decalage) % 26
            val_decalage = R10[blue_R10]
            blue_alphabet = (blue_R10 + val_decalage) % 26
            
            dict[str(pos)].setStyleSheet("background-color : #FFABAB; color : white; font-size: 16px; font-weight: bold;width : 15px !important; border:1px solid; border-radius:10px; height: 25px;")
            
            dict["12"+ str(pos + 1)].setStyleSheet("background-color : #FFABAB; color : white; font-size: 16px; font-weight: bold;width : 15px !important; border:1px solid; border-radius:10px; height: 25px;")
            dict["22"+ str(next_R21 + 1)].setStyleSheet("background-color : #FFABAB; color : white; font-size: 16px; font-weight: bold;width : 15px !important; border:1px solid; border-radius:10px; height: 25px;")
            dict["32"+ str(next_R31 + 1)].setStyleSheet("background-color : #FFABAB; color : white; font-size: 16px; font-weight: bold;width : 15px !important; border:1px solid; border-radius:10px; height: 25px;")
            
            dict["R"+ str(next_reflecteur + 1)].setStyleSheet("background-color : qlineargradient(spread:pad, x1:0.483424, y1:0.25, x2:0.471, y2:1, stop:0.207627 rgba(112, 142, 226, 255), stop:1 rgba(15, 112, 128, 255)); color : white; font-size: 16px; font-weight: bold; width : 15px !important;")
            
            dict["11"+ str(blue_R10 + 1)].setStyleSheet("background-color : #6EB5FF; color : white; font-size: 16px; font-weight: bold;width : 15px !important; border:1px solid; border-radius:10px; height: 25px;")
            dict["21"+ str(blue_R20 + 1)].setStyleSheet("background-color: #6EB5FF !important; color : white; font-size: 16px; font-weight: bold;width : 15px !important; border:1px solid; border-radius:10px; height: 25px;")
            dict["31"+ str(blue_R30 + 1)].setStyleSheet("background-color: #6EB5FF !important; color : white; font-size: 16px; font-weight: bold;width : 15px !important; border:1px solid; border-radius:10px; height: 25px;")
            
            dict[str(blue_alphabet)].setStyleSheet("background-color: #6EB5FF !important; color : white; font-size: 16px; font-weight: bold;width : 15px !important; border:1px solid; border-radius:10px; height: 25px;")
            
            
            encr = alphabet[blue_alphabet]
            
            globals()["texte_crypte"] += encr
            self.lineEdit_2.setText(globals()["texte_crypte"])
            
            print("encr",encr)
            globals()["increment"] += 1
            globals()["text_index"] += 1 
            
            if len(globals()["texte_crypte"]) == len(texte):
                self.pushButton_4.setEnabled(False)
                self.pushButton_2.setEnabled(False)
            case = {
        "pos": pos,
        "next_R21": next_R21,
        "next_R31": next_R31,
        "next_reflecteur" : next_reflecteur,
        "blue_R30" : blue_R30,
        "blue_R20" : blue_R20,
        "blue_R10" : blue_R10,
        "blue_alphabet" : blue_alphabet,
        "lettre" : alphabet[blue_alphabet]
        }
            globals()["case"] = case
                
        else:
            error = QMessageBox()
            error.setWindowTitle("Erreur")
            error.setText("Oops, Vous devez effectuer une rotation des rotors d'abord !")
            error.setIcon(QMessageBox.Warning)
            x = error.exec_()
            print("You need to rotate first !")

    def rotate(self):
        if globals()["increment"] != 0 :
            if (globals()["k1"] % 26) != 0 :
                
                if key[0, 1] == 'D':
                    globals()['R'+key[0, 0] + '0'] = np.roll(globals()['R' + key[0, 0] + '0'], 1)
                    globals()['R'+key[0, 0] + '1'] = np.roll(globals()['R' + key[0, 0] + '1'], 1)
                else:
                    globals()['R'+key[0, 0] + '0'] = np.roll(globals()['R' + key[0, 0] + '0'], -1)
                    globals()['R'+key[0, 0] + '1'] = np.roll(globals()['R' + key[0, 0] + '1'], -1)
                globals()["k1"] = globals()["k1"] + 1
            
            elif (globals()["k2"] % 26) != 0:
                
                if key[2, 1] == 'D':
                        globals()['R'+key[1, 0] + '0'] = np.roll(globals()['R' + key[1, 0] + '0'], 1)
                        globals()['R'+key[1, 0] + '1'] = np.roll(globals()['R' + key[1, 0] + '1'], 1)
                else:
                        globals()['R'+key[1, 0] + '0'] = np.roll(globals()['R' + key[1, 0] + '0'], -1)
                        globals()['R'+key[1, 0] + '1'] = np.roll(globals()['R' + key[1, 0] + '1'], -1)
                globals()["k2"] = globals()["k2"] + 1
            
            elif (globals()["k3"] % 26) != 0:
                if key[2, 1] == 'D':
                        globals()['R'+key[2, 0] + '0'] = np.roll(globals()['R' + key[2, 0] + '0'], 1)
                        globals()['R'+key[2, 0] + '1'] = np.roll(globals()['R' + key[2, 0] + '1'], 1)
                else:
                        globals()['R'+key[2, 0] + '0'] = np.roll(globals()['R' + key[2, 0] + '0'], -1)
                        globals()['R'+key[2, 0] + '1'] = np.roll(globals()['R' + key[2, 0] + '1'], -1)
                globals()["k3"] = globals()["k3"] + 1
                
            globals()["increment"] = 0
            
            if (globals()["k3"] % 26) == 0 :
                globals()["k1"] = 1
                globals()["k2"] = 1
                globals()["k3"] = 1
                
            self.pushButton_111.setText(str(R10[0]))
            self.pushButton_112.setText(str(R10[1]))
            self.pushButton_113.setText(str(R10[2]))
            self.pushButton_114.setText(str(R10[3]))
            self.pushButton_115.setText(str(R10[4]))
            self.pushButton_116.setText(str(R10[5]))
            self.pushButton_117.setText(str(R10[6]))
            self.pushButton_118.setText(str(R10[7]))
            self.pushButton_119.setText(str(R10[8]))
            self.pushButton_1110.setText(str(R10[9]))
            self.pushButton_1111.setText(str(R10[10]))
            
            self.pushButton_1112.setText(str(R10[11]))
            self.pushButton_1113.setText(str(R10[12]))
            self.pushButton_1114.setText(str(R10[13]))
            self.pushButton_1115.setText(str(R10[14]))
            self.pushButton_1116.setText(str(R10[15]))
            self.pushButton_1117.setText(str(R10[16]))
            self.pushButton_1118.setText(str(R10[17]))
            self.pushButton_1119.setText(str(R10[18]))
            self.pushButton_1120.setText(str(R10[19]))
            self.pushButton_1121.setText(str(R10[20]))
            self.pushButton_1122.setText(str(R10[21]))
            self.pushButton_1123.setText(str(R10[22]))
            self.pushButton_1124.setText(str(R10[23]))
            self.pushButton_1125.setText(str(R10[24]))
            self.pushButton_1126.setText(str(R10[25]))
            
            self.pushButton_121.setText(str(R11[0]))
            self.pushButton_122.setText(str(R11[1]))
            self.pushButton_123.setText(str(R11[2]))
            self.pushButton_124.setText(str(R11[3]))
            self.pushButton_125.setText(str(R11[4]))
            self.pushButton_126.setText(str(R11[5]))
            self.pushButton_127.setText(str(R11[6]))
            self.pushButton_128.setText(str(R11[7]))
            self.pushButton_129.setText(str(R11[8]))
            self.pushButton_1210.setText(str(R11[9]))
            self.pushButton_1211.setText(str(R11[10]))
            self.pushButton_1212.setText(str(R11[11]))
            self.pushButton_1213.setText(str(R11[12]))
            self.pushButton_1214.setText(str(R11[13]))
            self.pushButton_1215.setText(str(R11[14]))
            self.pushButton_1216.setText(str(R11[15]))
            self.pushButton_1217.setText(str(R11[16]))
            self.pushButton_1218.setText(str(R11[17]))
            self.pushButton_1219.setText(str(R11[18]))
            self.pushButton_1220.setText(str(R11[19]))
            self.pushButton_1221.setText(str(R11[20]))
            self.pushButton_1222.setText(str(R11[21]))
            self.pushButton_1223.setText(str(R11[22]))
            self.pushButton_1224.setText(str(R11[23]))
            self.pushButton_1225.setText(str(R11[24]))
            self.pushButton_1226.setText(str(R11[25]))
            
            ################### ROTOR 2 ######################3
            
            self.pushButton_211.setText(str(R20[0]))
            self.pushButton_212.setText(str(R20[1]))
            self.pushButton_213.setText(str(R20[2]))
            self.pushButton_214.setText(str(R20[3]))
            self.pushButton_215.setText(str(R20[4]))
            self.pushButton_216.setText(str(R20[5]))
            self.pushButton_217.setText(str(R20[6]))
            self.pushButton_218.setText(str(R20[7]))
            self.pushButton_219.setText(str(R20[8]))
            self.pushButton_2110.setText(str(R20[9]))
            self.pushButton_2111.setText(str(R20[10]))
            self.pushButton_2112.setText(str(R20[11]))
            self.pushButton_2113.setText(str(R20[12]))
            self.pushButton_2114.setText(str(R20[13]))
            self.pushButton_2115.setText(str(R20[14]))
            self.pushButton_2116.setText(str(R20[15]))
            self.pushButton_2117.setText(str(R20[16]))
            self.pushButton_2118.setText(str(R20[17]))
            self.pushButton_2119.setText(str(R20[18]))
            self.pushButton_2120.setText(str(R20[19]))
            self.pushButton_2121.setText(str(R20[20]))
            self.pushButton_2122.setText(str(R20[21]))
            self.pushButton_2123.setText(str(R20[22]))
            self.pushButton_2124.setText(str(R20[23]))
            self.pushButton_2125.setText(str(R20[24]))
            self.pushButton_2126.setText(str(R20[25]))
            
            
            self.pushButton_221.setText(str(R21[0]))
            self.pushButton_222.setText(str(R21[1]))
            self.pushButton_223.setText(str(R21[2]))
            self.pushButton_224.setText(str(R21[3]))
            self.pushButton_225.setText(str(R21[4]))
            self.pushButton_226.setText(str(R21[5]))
            self.pushButton_227.setText(str(R21[6]))
            self.pushButton_228.setText(str(R21[7]))
            self.pushButton_229.setText(str(R21[8]))
            self.pushButton_2210.setText(str(R21[9]))
            self.pushButton_2211.setText(str(R21[10]))
            self.pushButton_2212.setText(str(R21[11]))
            self.pushButton_2213.setText(str(R21[12]))
            self.pushButton_2214.setText(str(R21[13]))
            self.pushButton_2215.setText(str(R21[14]))
            self.pushButton_2216.setText(str(R21[15]))
            self.pushButton_2217.setText(str(R21[16]))
            self.pushButton_2218.setText(str(R21[17]))
            self.pushButton_2219.setText(str(R21[18]))
            self.pushButton_2220.setText(str(R21[19]))
            self.pushButton_2221.setText(str(R21[20]))
            self.pushButton_2222.setText(str(R21[21]))
            self.pushButton_2223.setText(str(R21[22]))
            self.pushButton_2224.setText(str(R21[23]))
            self.pushButton_2225.setText(str(R21[24]))
            self.pushButton_2226.setText(str(R21[25]))
        
        #################  ROTOR 3 ##########################
        
            self.pushButton_311.setText(str(R30[0]))
            self.pushButton_312.setText(str(R30[1]))
            self.pushButton_313.setText(str(R30[2]))
            self.pushButton_314.setText(str(R30[3]))
            self.pushButton_315.setText(str(R30[4]))
            self.pushButton_316.setText(str(R30[5]))
            self.pushButton_317.setText(str(R30[6]))
            self.pushButton_318.setText(str(R30[7]))
            self.pushButton_319.setText(str(R30[8]))
            self.pushButton_3110.setText(str(R30[9]))
            self.pushButton_3111.setText(str(R30[10]))
            self.pushButton_3112.setText(str(R30[11]))
            self.pushButton_3113.setText(str(R30[12]))
            self.pushButton_3114.setText(str(R30[13]))
            self.pushButton_3115.setText(str(R30[14]))
            self.pushButton_3116.setText(str(R30[15]))
            self.pushButton_3117.setText(str(R30[16]))
            self.pushButton_3118.setText(str(R30[17]))
            self.pushButton_3119.setText(str(R30[18]))
            self.pushButton_3120.setText(str(R30[19]))
            self.pushButton_3121.setText(str(R30[20]))
            self.pushButton_3122.setText(str(R30[21]))
            self.pushButton_3123.setText(str(R30[22]))
            self.pushButton_3124.setText(str(R30[23]))
            self.pushButton_3125.setText(str(R30[24]))
            self.pushButton_3126.setText(str(R30[25]))
            
            self.pushButton_321.setText(str(R31[0]))
            self.pushButton_322.setText(str(R31[1]))
            self.pushButton_323.setText(str(R31[2]))
            self.pushButton_324.setText(str(R31[3]))
            self.pushButton_325.setText(str(R31[4]))
            self.pushButton_326.setText(str(R31[5]))
            self.pushButton_327.setText(str(R31[6]))
            self.pushButton_328.setText(str(R31[7]))
            self.pushButton_329.setText(str(R31[8]))
            self.pushButton_3210.setText(str(R31[9]))
            self.pushButton_3211.setText(str(R31[10]))
            self.pushButton_3212.setText(str(R31[11]))
            self.pushButton_3213.setText(str(R31[12]))
            self.pushButton_3214.setText(str(R31[13]))
            self.pushButton_3215.setText(str(R31[14]))
            self.pushButton_3216.setText(str(R31[15]))
            self.pushButton_3217.setText(str(R31[16]))
            self.pushButton_3218.setText(str(R31[17]))
            self.pushButton_3219.setText(str(R31[18]))
            self.pushButton_3220.setText(str(R31[19]))
            self.pushButton_3221.setText(str(R31[20]))
            self.pushButton_3222.setText(str(R31[21]))
            self.pushButton_3223.setText(str(R31[22]))
            self.pushButton_3224.setText(str(R31[23]))
            self.pushButton_3225.setText(str(R31[24]))
            self.pushButton_3226.setText(str(R31[25]))
            
            case = globals()["case"]
            dict[str(case["pos"])].setStyleSheet("background-color : qlineargradient(spread:pad, x1:0.483424, y1:0.25, x2:0.471, y2:1, stop:0.207627 rgba(112, 142, 226, 255), stop:1 rgba(15, 112, 128, 255)); color : white; font-size: 16px; font-weight: bold; width : 15px !important;")
            dict["12"+ str(case["pos"] + 1)].setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
            dict["22"+ str(case["next_R21"] + 1)].setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
            dict["32"+ str(case["next_R31"] + 1)].setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
            
            dict["R"+ str(case["next_reflecteur"] + 1)].setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: #D7ECD9; border: 1px solid;''')
            
            dict["11"+ str(case["blue_R10"] + 1)].setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
            dict["21"+ str(case["blue_R20"] + 1)].setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
            dict["31"+ str(case["blue_R30"] + 1)].setStyleSheet('''width: 15px;height: 30px;font-size: 14px;font-weight: bold;border-radius:8px ;color: black;background: white;border: 1px solid; background: #D7ECD9;''')
            
            dict[str(case["blue_alphabet"])].setStyleSheet("background-color: #D7ECD9 !important; color : white; font-size: 16px; font-weight: bold;width : 15px !important;")
        else:
            print("increment error")
            
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    width = 1900
    height = 1000
    Form.setFixedSize(width, height)
    Form.show()

    sys.exit(app.exec_())