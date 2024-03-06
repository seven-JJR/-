import os

from PyQt5.QtWidgets import QMessageBox,QInputDialog
from PyQt5.QtWidgets import QMainWindow,QApplication,QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot,QTimer,QDateTime
from NEWuntitled2K_125 import  Ui_MainWindow
import random
import shutil

class MainWindow(QMainWindow ,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.timer=QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        self.pushButton_7.clicked.connect(self.choujiang)
        self.pushButton_8.clicked.connect(self.stop)
        #self.pushButton_3.clicked.connect(self.shezhi)
        self.pushButton_10.clicked.connect(self.clear)
        self.label_3.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        font = QtGui.QFont()
        font.setPointSize(17)
        font_1 = QtGui.QFont()
        font_1.setPointSize(17)
        self.label_2.setFont(font_1)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
                                   "    color: #ffffff;\n"
                                   "}")
        self.label_3.setObjectName("label_3")


    def clear(self):
        shutil.copy('D:\\data\\name.txt', 'D:\\name.txt')
        shutil.copy('D:\\data\\record.txt', 'D:\\record.txt')
        self.radioButton_8.setCheckable(True)
        self.radioButton_7.setCheckable(True)
        self.radioButton_6.setCheckable(True)
        self.radioButton_9.setCheckable(True)
        self.radioButton_10.setCheckable(True)
        self.radioButton_11.setCheckable(True)
        QMessageBox.information(MainWindow,'提示','重置成功')

    def choujiang(self):
        names_222 = open('D:\\name.txt', encoding='utf8')
        names_222_222 = str(names_222.read())
        names_222_222_222 = names_222_222.split('\n')
        if '' in names_222_222_222:
            names_222_222_222.remove('')
        names_222.close()
        if self.radioButton_9.isChecked()==False and self.radioButton_10.isChecked()==False and self.radioButton_11.isChecked()==False and self.radioButton_7.isChecked()==False and self.radioButton_6.isChecked()==False and self.radioButton_8.isChecked()==False:
            QMessageBox.information(MainWindow,'提示','请先设置奖别')
        elif self.radioButton_10.isChecked()==True and len(names_222_222_222) < 4:
            QMessageBox.information(MainWindow, '提示', '名单人数不足')
        elif self.radioButton_9.isChecked() == True and len(names_222_222_222) < 2:
            QMessageBox.information(MainWindow, '提示', '名单人数不足')
        elif self.radioButton_11.isChecked() == True and len(names_222_222_222) < 6:
            QMessageBox.information(MainWindow, '提示', '名单人数不足')
        elif self.radioButton_7.isChecked() == True and len(names_222_222_222) < 10:
            QMessageBox.information(MainWindow, '提示', '名单人数不足')
        elif self.radioButton_6.isChecked() == True and len(names_222_222_222) < 10:
            QMessageBox.information(MainWindow, '提示', '名单人数不足')
        elif self.radioButton_8.isChecked() == True and len(names_222_222_222) < 20:
            QMessageBox.information(MainWindow, '提示', '名单人数不足')
        else:
            self.label_4.clear()
            self.label.setStyleSheet("")
        #global cycle
        #if cycle=='':
            #QMessageBox.information(MainWindow,'提示','请设置奖池',QMessageBox.Ok)
        #else:
            font_1 = QtGui.QFont()
            font_1.setPointSize(36)
            self.label_2.setFont(font_1)
            self.timer_1 = QTimer()
            self.timer_1.start(10)
            self.timer_1.timeout.connect(self.name_list)
    def stop(self):
        self.timer_1.stop()
        #global cycle
        if self.radioButton_9.isChecked():
            font_77 = QtGui.QFont()
            font_77.setPointSize(48)
            self.label_4.setFont(font_77)
            self.label.setStyleSheet("border-image: url(:/jp_1_1/jp1.png);")
            self.label_4.setText(' 漫游者耳机')
            font_2 = QtGui.QFont()
            font_2.setPointSize(96)
            self.label_2.setFont(font_2)
            names_2 = open('D:\\name.txt', encoding='utf8')
            names_2_2 = str(names_2.read())
            names_2_2_2 = names_2_2.split('\n')
            if '' in names_2_2_2:
                names_2_2_2.remove('')
            names_2.close()
            zhongjiang_list_2= random.sample(names_2_2_2, 2)
            text_2 = ''
            record_1 = open('D:\\record.txt', 'a', encoding='utf8')
            for name_2 in zhongjiang_list_2:
                text_2 = text_2 + '   '+name_2 + '\n'
                names_2_2_2.remove(name_2)
                record_1.write('一等奖:'+name_2+'\n')
            record_1.close()
            self.label_2.setText('\n'+text_2)
            x2='\n'.join(map(str,names_2_2_2))
            os.remove('D:\\name.txt')
            f_2_2 = open('D:\\name.txt', 'w+', encoding='utf8')
            f_2_2.write(x2)
            f_2_2.close()
            self.radioButton_9.setCheckable(False)
        elif self.radioButton_10.isChecked():
            font_77 = QtGui.QFont()
            font_77.setPointSize(40)
            self.label_4.setFont(font_77)
            self.label_4.setText('  小米蓝牙音箱')
            self.label.setStyleSheet("border-image: url(:/jp_1_1/jp2.png);")
            font_3 = QtGui.QFont()
            font_3.setPointSize(76)
            self.label_2.setFont(font_3)
            names_3 = open('D:\\name.txt', encoding='utf8')
            names_3_3 = str(names_3.read())
            names_3_3_3 = names_3_3.split('\n')
            if '' in names_3_3_3:
                names_3_3_3.remove('')
            names_3.close()
            zhongjiang_list_3=random.sample(names_3_3_3,4)
            text_3 = ''
            record_2 = open('D:\\record.txt', 'a', encoding='utf8')
            for name_3 in zhongjiang_list_3:
                text_3 = text_3 + '      '+name_3 + '\n'
                names_3_3_3.remove(name_3)
                record_2.write('二等奖:' + name_3 + '\n')
            record_2.close()
            self.label_2.setText(text_3)
            x3 = '\n'.join(map(str, names_3_3_3))
            os.remove('D:\\name.txt')
            f_3_3 = open('D:\\name.txt', 'w+', encoding='utf8')
            f_3_3.write(x3)
            f_3_3.close()
            self.radioButton_10.setCheckable(False)
        elif self.radioButton_11.isChecked():
            font_77 = QtGui.QFont()
            font_77.setPointSize(40)
            self.label_4.setFont(font_77)
            self.label_4.setText(' ZNNCO充电宝')
            self.label.setStyleSheet("border-image: url(:/jp_1_1/jp3.png);")
            font_4 = QtGui.QFont()
            font_4.setPointSize(58)
            self.label_2.setFont(font_4)
            names_4 = open('D:\\name.txt', encoding='utf8')
            names_4_4 = str(names_4.read())
            names_4_4_4 = names_4_4.split('\n')
            if '' in names_4_4_4:
                names_4_4_4.remove('')
            names_4.close()
            zhongjiang_list_4=random.sample(names_4_4_4,6)
            text_4 = ''
            record_3 = open('D:\\record.txt', 'a', encoding='utf8')
            for name_4 in zhongjiang_list_4:
                text_4 = text_4 +'             '+ name_4 + '\n'
                names_4_4_4.remove(name_4)
                record_3.write('三等奖:' + name_4 + '\n')
            record_3.close()
            self.label_2.setText(text_4)
            x4 = '\n'.join(map(str, names_4_4_4))
            os.remove('D:\\name.txt')
            f_4_4 = open('D:\\name.txt', 'w+', encoding='utf8')
            f_4_4.write(x4)
            f_4_4.close()
            self.radioButton_11.setCheckable(False)
        elif self.radioButton_7.isChecked():
            font_77 = QtGui.QFont()
            font_77.setPointSize(48)
            self.label_4.setFont(font_77)
            self.label_4.setText(' 恒温暖桌垫')
            self.label.setStyleSheet("border-image: url(:/jp_1_1/jp4.png);")
            font_5 = QtGui.QFont()
            font_5.setPointSize(35)
            self.label_2.setFont(font_5)
            names_5 = open('D:\\name.txt', encoding='utf8')
            names_5_5 = str(names_5.read())
            names_5_5_5 = names_5_5.split('\n')
            if '' in names_5_5_5:
                names_5_5_5.remove('')
            names_5.close()
            zhongjiang_list_5 = random.sample(names_5_5_5, 10)
            text_5 = ''
            record_4 = open('D:\\record.txt', 'a', encoding='utf8')
            for name_5 in zhongjiang_list_5:
                text_5 = text_5 +'                              '+ name_5 + '\n'
                names_5_5_5.remove(name_5)
                record_4.write('四等奖:' + name_5 + '\n')
            record_4.close()
            self.label_2.setText(text_5)
            x5 = '\n'.join(map(str, names_5_5_5))
            os.remove('D:\\name.txt')
            f_5_5 = open('D:\\name.txt', 'w+', encoding='utf8')
            f_5_5.write(x5)
            f_5_5.close()
            self.radioButton_7.setCheckable(False)
        elif self.radioButton_6.isChecked():
            font_77 = QtGui.QFont()
            font_77.setPointSize(40)
            self.label_4.setFont(font_77)
            self.label_4.setText('  夜伴荤素集结')
            self.label.setStyleSheet("border-image: url(:/jp_1_1/jp5.png);")
            font_6 = QtGui.QFont()
            font_6.setPointSize(35)
            self.label_2.setFont(font_6)
            names_6 = open('D:\\name.txt', encoding='utf8')
            names_6_6 = str(names_6.read())
            names_6_6_6 = names_6_6.split('\n')
            if '' in names_6_6_6:
                names_6_6_6.remove('')
            names_6.close()
            zhongjiang_list_6 = random.sample(names_6_6_6, 10)
            text_6 = ''
            record_5 = open('D:\\record.txt', 'a', encoding='utf8')
            for name_6 in zhongjiang_list_6:
                text_6 = text_6 + '                              ' + name_6 + '\n'
                names_6_6_6.remove(name_6)
                record_5.write('五等奖:' + name_6 + '\n')
            record_5.close()
            self.label_2.setText(text_6)
            x6 = '\n'.join(map(str, names_6_6_6))
            os.remove('D:\\name.txt')
            f_6_6 = open('D:\\name.txt', 'w+', encoding='utf8')
            f_6_6.write(x6)
            f_6_6.close()
            self.radioButton_6.setCheckable(False)
        elif self.radioButton_8.isChecked():
            font_77 = QtGui.QFont()
            font_77.setPointSize(51)
            self.label_4.setFont(font_77)
            self.label_4.setText('   闪迪U盘')
            self.label.setStyleSheet("border-image: url(:/jp_1_1/jp6.png);")
            font_7 = QtGui.QFont()
            font_7.setPointSize(35)
            self.label_2.setFont(font_7)
            names_7 = open('D:\\name.txt', encoding='utf8')
            names_7_7 = str(names_7.read())
            names_7_7_7 = names_7_7.split('\n')
            if '' in names_7_7_7:
                names_7_7_7.remove('')
            names_7.close()
            zhongjiang_list_7 = random.sample(names_7_7_7, 20)
            record_6 = open('D:\\record.txt', 'a', encoding='utf8')
            name_list7=[]
            for name_7 in zhongjiang_list_7:
                name_list7.append(name_7)
                names_7_7_7.remove(name_7)
                record_6.write('六等奖:' + name_7 + '\n')
            record_6.close()
            text7='                '+name_list7[0]+'  '+name_list7[1]+'\n'+'                '+name_list7[2]+'  '+name_list7[3]+'\n'+'                '+name_list7[4]+'  '+name_list7[5]+'\n'+'                '+name_list7[6]+'  '+name_list7[7]+'\n'+'                '+name_list7[8]+'  '+name_list7[9]+'\n'+'                '+name_list7[10]+'  '+name_list7[11]+'\n'+'                '+name_list7[12] + '  ' + name_list7[13] + '\n'+'                '+name_list7[14]+'  '+name_list7[15]+'\n'+'                '+name_list7[16]+'  '+name_list7[17]+'\n'+'                '+name_list7[18]+'  '+name_list7[19]
            self.label_2.setText(text7)
            x7 = '\n'.join(map(str, names_7_7_7))
            os.remove('D:\\name.txt')
            f_7_7 = open('D:\\name.txt', 'w+', encoding='utf8')
            f_7_7.write(x7)
            f_7_7.close()
            self.radioButton_8.setCheckable(False)
    def name_list(self):
        names_1 = open('D:\\name.txt', encoding='utf8')
        names_1_1 = str(names_1.read())
        names_1_1_1 = names_1_1.split('\n')
        names_1.close()
        long = len(names_1_1_1) - 1
        name_1=names_1_1_1[random.randint(0,long)]
        name_2=names_1_1_1[random.randint(0,long)]
        name_3=names_1_1_1[random.randint(0,long)]
        name_4=names_1_1_1[random.randint(0,long)]
        name_5=names_1_1_1[random.randint(0,long)]
        name_6=names_1_1_1[random.randint(0,long)]
        name_7=names_1_1_1[random.randint(0,long)]
        name_8=names_1_1_1[random.randint(0,long)]
        name_9=names_1_1_1[random.randint(0,long)]
        name_10 = names_1_1_1[random.randint(0, long)]
        X='                            '
        text=X+name_1+'\n'+X+name_2+'\n'+X+name_3+'\n'+X+name_4+'\n'+X+name_5+'\n'+X+name_6+'\n'+X+name_7+'\n'+X+name_8+'\n'+X+name_9+'\n'+X+name_10
        self.label_2.setText(text)



    def showTime(self):
        # 获取系统当前时间
        time = QDateTime.currentDateTime()
        # 设置系统时间的显示格式
        timeDisplay = time.toString('yyyy-MM-dd hh:mm:ss')
        # 在标签上显示时间
        self.label_3.setText(' '+timeDisplay)
if __name__=='__main__':
    import sys
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)#自适应分辨率
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=MainWindow()
    MainWindow.show()
    sys.exit(app.exec())
#MainWindow.setStyleSheet("#MainWindow {background-image: url(:/beijing_1_1/1.jpeg);}")
#MainWindow.setStyleSheet("#MainWindow {background-image: url(:/beijing_2_2/3.jpeg);}")
#self.label.setAttribute(QtCore.Qt.WA_TranslucentBackground)