import threading
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import sqlite3 as sq3
from MainWindow_python import *
from PyQt5.QtWidgets import QApplication
from Mac_Gor_python import *
import sonuc_gir_python as sonuc
import time
import konu_gor_python as konu_g

class MainPage(QMainWindow):

    def __init__(self):
        super().__init__()
        self.main = Ui_MainWindow()
        self.main.setupUi(self)
        self.main.Tak_Ekle_3.clicked.connect(self.open_tak_ekle)
        self.main.Tak_Cik.clicked.connect(self.open_tak_cik)
        self.main.Juri_Gir.clicked.connect(self.open_juri_ekle)
        self.main.Juri_Cik.clicked.connect(self.open_juri_cik)
        self.main.Baslat.clicked.connect(self.open_mac_gor)
        self.main.Sonuc.clicked.connect(self.sonuc_gir)
        self.main.Konu_Gos.clicked.connect(self.konu_gor)
        self.tak_ekle = Takim_Ekle_Page()
        self.tak_cik = Takim_Cikar_Page()
        self.jur_gir = Juri_Gir_Page()
        self.jur_cik = Juri_Cikar_Page()
        self.tur_sec = Tur_Page()
        self.sonuc_gir = Sonuc_Gir_Page()
        self.konu_gor = Konu_Gor_Page()

    def sonuc_gir(self):
        self.sonuc_gir.show()

    def open_mac_gor(self):
        self.tur_sec.show()

    def open_tak_ekle(self):
        self.tak_ekle.show()

    def open_tak_cik(self):
        self.tak_cik.show()

    def open_juri_ekle(self):
        self.jur_gir.show()

    def open_juri_cik(self):
        self.jur_cik.show()

    def konu_gor(self):
        self.konu_gor.show()

class Takim_Ekle_Page(QWidget):

    def __init__(self):
        super().__init__()
        loadUi("Takim_Ekle.ui", self)
        self.Kaydet.clicked.connect(self.open_spe_ekle_the)
        self.tab = sq3.connect("Marmara Acik", check_same_thread= False)
        self.im_tab = self.tab.cursor()

    def open_spe_ekle_the(self):
        threading.Thread(target=self.open_spe_ekle,).start()

    def open_spe_ekle(self):
        self.spe_1 = ('"{}"').format(self.lineEdit_3.text())
        self.spe_2 = ('"{}"').format(self.lineEdit_2.text())
        self.speaker_takim = ('"{}"').format(self.lineEdit.text())
        self.spe_uni = ('"{}"').format(self.lineEdit_4.text())
        self.im_tab.execute("CREATE TABLE IF NOT EXISTS takim(uni,takim,bir,iki,t_pua,bi_pua,ik_pua)")
        self.im_tab.execute(("INSERT INTO takim VALUES({},{}, {}, {},0,0,0)").format(self.spe_uni,self.speaker_takim,self.spe_1,self.spe_2))
        self.tab.commit()

class Takim_Cikar_Page(QWidget):

    tab = sq3.connect("Marmara Acik", check_same_thread= False)
    im_tab = tab.cursor()

    def __init__(self):
        super().__init__()
        loadUi("Takim_Cikar.ui", self)
        self.C_Tak_P.clicked.connect(self.open_cik_tak)

    def open_cik_tak(self):
        self.tak_ad = ('"{}"').format(self.C_Tak_Ad.text())
        self.im_tab.execute(("DELETE FROM takim where takim= {}").format(self.tak_ad))
        self.tab.commit()
        self.tab.close()
        self.close()

class Juri_Gir_Page(QWidget):

    def __init__(self):
        super().__init__()
        loadUi("Juri_Gir.ui", self)

class Juri_Cikar_Page(QWidget):

    def __init__(self):
        super().__init__()
        loadUi("Juri_Cikar.ui", self)

class Tur_Page(QWidget):

    tab = sq3.connect("Marmara Acik", check_same_thread= False)
    im_tab = tab.cursor()

    def __init__(self):
        super().__init__()
        loadUi("tur.ui", self)
        self.Kaydet.clicked.connect(self.open_tur_ac_the)

    def open_tur_ac_the(self):
        self.open_tur_ac()

    def konu(self):
        global konu
        konu = ('{}').format(self.Konu.toPlainText())

    def konu_the(self):
        threading.Thread(target = self.konu,).start()

    def info(self):
        global info
        info = ('{}').format(self.Info.toPlainText())

    def info_the(self):
        threading.Thread(target = self.info,).start()

    def open_tur_ac(self):
        global tur
        tur = ('{}').format(self.Tur.text())
        self.info_the()
        self.konu_the()
        self.mac_gor = Mac_Gor_Page()
        self.im_tab.execute((f"CREATE TABLE IF NOT EXISTS {tur}(SALON,HA,MA,HK,MK,JUR)"))
        self.tab.commit()
        self.mac_gor.show()
        self.close()

class Mac_Gor_Page(QWidget):

    tab = sq3.connect("Marmara Acik", check_same_thread= False)
    im_tab = tab.cursor()

    def __init__(self):
        super().__init__()
        self.mac_gor = Ui_Form()
        self.mac_gor.setupUi(self)
        threading.Thread(target=self.loaddata,).start()
        self.mac_gor.Kaydet.clicked.connect(self.the_open_kaydet)

    def loaddata(self):
        time.sleep(1)
        global sayi
        self.im_tab.execute("SELECT takim,t_pua FROM takim")
        self.takimlar = self.im_tab.fetchall()
        uzun = len(self.takimlar)
        for i in range(uzun-1):
            for j in range(uzun-1):
                if int((self.takimlar[j])[1])>int((self.takimlar[j+1])[1]):
                    self.takimlar[i], self.takimlar[j+1] = self.takimlar[j+1], self.takimlar[i]
                else:
                    continue
        if uzun %4 >0 :
            sayi = int((uzun -(uzun %4) +4)/4)
        else:
            sayi = int(uzun/4)

        for i in range(sayi):
            if tur == "birinci":
                ha = random.choice(self.takimlar)
                self.takimlar.remove(ha)
                ma = random.choice(self.takimlar)
                self.takimlar.remove(ma)
                hk = random.choice(self.takimlar)
                self.takimlar.remove(hk)
                mk = random.choice(self.takimlar)
                self.takimlar.remove(mk)
                self.tak_for = (None,ha[0],ma[0],hk[0],mk[0],None)
                self.im_tab.execute((f"INSERT INTO {tur} VALUES(?, ?, ?, ?, ? ,?)"),self.tak_for)
                self.tab.commit()
            else:
                self.tak_for = (None,(self.takimlar[0])[0],(self.takimlar[1])[0],(self.takimlar[2])[0],(self.takimlar[3])[0],None)
                self.im_tab.execute((f"INSERT INTO {tur} VALUES(?, ?, ?, ?, ? ,?)"),self.tak_for)
                self.tab.commit()
                for a in range(4):
                    self.takimlar.remove(self.takimlar[0])
        self.im_tab.execute(f"SELECT HA,MA,HK,MK FROM {tur}")
        self.new_tak = self.im_tab.fetchall()
        self.tak_sayi = len(self.new_tak)
        for i in range(sayi):
            currentRowCount = self.mac_gor.tableWidget.rowCount()
            self.mac_gor.tableWidget.insertRow(currentRowCount)
            b=1
            for s in range(4):
                self.mac_gor.tableWidget.setItem(i,b,QtWidgets.QTableWidgetItem((self.new_tak[i])[s]))
                b=b+1
    def the_open_kaydet(self):
        threading.Thread(target = self.open_kaydet,).start()

    def open_kaydet(self):
        time.sleep(1)
        for i in range(0,sayi):
            sal_no = str(("{}").format(self.mac_gor.tableWidget.item(i,0).text()))
            juri_isim = str(("{}").format(self.mac_gor.tableWidget.item(i,5).text()))
            self.im_tab.execute(f"UPDATE {tur} SET SALON = ? WHERE rowid = {i+1}",[sal_no])
            self.im_tab.execute(f"UPDATE {tur} SET JUR = ? WHERE rowid = {i+1}",[juri_isim])
            self.tab.commit()

class Sonuc_Gir_Page(QWidget):

    tab = sq3.connect("Marmara Acik", check_same_thread=False)
    tab_im = tab.cursor()

    def __init__(self):
        super().__init__()
        self.sonuc_gir = sonuc.Ui_Form()
        self.sonuc_gir.setupUi(self)
        self.tab_im.execute("SELECT name FROM sqlite_master WHERE type='table'")
        self.turlar = self.tab_im.fetchall()
        self.sonuc_gir.Salon_2.insertItem(0,"Seçiniz")
        for i in range(len(self.turlar)):
            if self.turlar[i][0]=="takim":
                pass
            else:
                self.sonuc_gir.Salon_2.addItem(self.turlar[i][0])
        self.sonuc_gir.Salon_2.currentIndexChanged['QString'].connect(self.tur_gir)
        self.sonuc_gir.Salon.currentIndexChanged['QString'].connect(self.salon_gir)
        self.sonuc_gir.Kaydet.clicked.connect(self.the_open_sonuc_gir)

    def tur_gir(self, current_text):
        global tur_Secimi
        tur_Secimi = current_text
        self.tab_im.execute(f"SELECT SALON FROM {current_text}")
        salon = self.tab_im.fetchall()
        self.sonuc_gir.Salon.clear()
        self.sonuc_gir.Salon.insertItem(0,"Seçiniz")
        for i in range(len(salon)):
            self.sonuc_gir.Salon.addItem(salon[i][0])

    def salon_gir(self, current_text):
        global mac
        global takim
        self.c_t = current_text
        self.tab_im.execute(f"SELECT * FROM {tur_Secimi}")
        mac = self.tab_im.fetchall()
        self.tab_im.execute("SELECT takim, bir, iki FROM takim")
        takim = self.tab_im.fetchall()
        self.salon_gir_kom_the()

    def salon_gir_kom_the(self):
        threading.Thread(target = self.salon_gir_kom,).start()

    def salon_gir_kom(self):
        self.sonuc_gir.HA1.clear()
        self.sonuc_gir.HA2.clear()
        self.sonuc_gir.MA1.clear()
        self.sonuc_gir.MA2.clear()
        self.sonuc_gir.HK1.clear()
        self.sonuc_gir.HK2.clear()
        self.sonuc_gir.MK1.clear()
        self.sonuc_gir.MK2.clear()
        uzun = len(takim)
        if uzun %4 >0 :
            sayi = int((uzun -(uzun %4) +4)/4)
        else:
            sayi = int(uzun/4)
        for i in range(sayi):
            if mac[i][0] == self.c_t:
                self.sonuc_gir.HA.setText(mac[i][1])
                self.sonuc_gir.MA.setText(mac[i][2])
                self.sonuc_gir.HK.setText(mac[i][3])
                self.sonuc_gir.MK.setText(mac[i][4])
                for a in range(len(takim)):
                    c = ("{}").format(takim[a][1])
                    d = ("{}").format(takim[a][2])
                    if mac[i][1] == takim[a][0]:
                        self.sonuc_gir.HA1.addItem(c)
                        self.sonuc_gir.HA1.addItem(d)
                        self.sonuc_gir.HA2.addItem(c)
                        self.sonuc_gir.HA2.addItem(d)
                    if mac[i][2] == takim[a][0]:
                        self.sonuc_gir.MA1.addItem(c)
                        self.sonuc_gir.MA1.addItem(d)
                        self.sonuc_gir.MA2.addItem(c)
                        self.sonuc_gir.MA2.addItem(d)
                    if mac[i][3] == takim[a][0]:
                        self.sonuc_gir.HK1.addItem(c)
                        self.sonuc_gir.HK1.addItem(d)
                        self.sonuc_gir.HK2.addItem(c)
                        self.sonuc_gir.HK2.addItem(d)
                    if mac[i][4] == takim[a][0]:
                        self.sonuc_gir.MK1.addItem(c)
                        self.sonuc_gir.MK1.addItem(d)
                        self.sonuc_gir.MK2.addItem(c)
                        self.sonuc_gir.MK2.addItem(d)

    def the_open_sonuc_gir(self):
        threading.Thread(target = self.open_sonuc_gir,).start()

    def open_sonuc_gir(self):
        HA1P = int(self.sonuc_gir.HA1P.text())
        HA2P = int(self.sonuc_gir.HA2P.text())
        MA1P = int(self.sonuc_gir.MA1P.text())
        MA2P = int(self.sonuc_gir.MA2P.text())
        HK1P = int(self.sonuc_gir.HK1P.text())
        HK2P = int(self.sonuc_gir.HK2P.text())
        MK1P = int(self.sonuc_gir.MK1P.text())
        MK2P = int(self.sonuc_gir.MK2P.text())
        HA1 = self.sonuc_gir.HA1.currentText()
        HA2 = self.sonuc_gir.HA2.currentText()
        MA1 = self.sonuc_gir.MA1.currentText()
        MA2 = self.sonuc_gir.MA2.currentText()
        HK1 = self.sonuc_gir.HK1.currentText()
        HK2 = self.sonuc_gir.HK2.currentText()
        MK1 = self.sonuc_gir.MK1.currentText()
        MK2 = self.sonuc_gir.MK2.currentText()
        HA = self.sonuc_gir.HA.text()
        MA = self.sonuc_gir.MA.text()
        HK = self.sonuc_gir.HK.text()
        MK = self.sonuc_gir.MK.text()
        hap = HA1P+HA2P
        map = MA1P+MA2P
        hkp = HK1P+HK2P
        mkp = MK1P+MK2P
        liste = [(HA,hap),(MA,map),(HK,hkp),(MK,mkp)]
        for i in range(3):
            for j in range(3):
                if int((liste[j])[1])>int((liste[j+1])[1]):
                    liste[i], liste[j+1] = liste[j+1], liste[i]
                else:
                    continue
        self.tab_im.execute("SELECT takim,t_pua FROM takim")
        puan = self.tab_im.fetchall()
        self.tab_im.execute("SELECT bir,bi_pua FROM takim ")
        bi_k = self.tab_im.fetchall()
        self.tab_im.execute("SELECT iki, ik_pua FROM takim")
        ik_k = self.tab_im.fetchall()
        for i in range(len(puan)):
            if puan[i][0] == liste[0][0]:
                new_p = [str(int(puan[i][1]) + 0),liste[0][0]]
                self.tab_im.execute("UPDATE takim SET t_pua = ? WHERE takim = ?",new_p)
                self.tab.commit()
            if puan[i][0] == liste[1][0]:
                new_p = [str(int(puan[i][1]) + 1),liste[1][0]]
                self.tab_im.execute("UPDATE takim SET t_pua = ? WHERE takim = ?",new_p)
                self.tab.commit()
            if puan[i][0] == liste[2][0]:
                new_p = [str(int(puan[i][1]) + 2),liste[2][0]]
                self.tab_im.execute("UPDATE takim SET t_pua = ? WHERE takim = ?",new_p)
                self.tab.commit()
            if puan[i][0] == liste[3][0]:
                new_p = [str(int(puan[i][1]) + 3),liste[3][0]]
                self.tab_im.execute("UPDATE takim SET t_pua = ? WHERE takim = ?",new_p)
                self.tab.commit()
        for i in range(len(puan)):
            if HA1 == ik_k[i][0]:
                new_p = [str(int(bi_k[i][1])+int(HA1P)),bi_k[i][0]]
                self.tab_im.execute("UPDATE takim SET ik_pua = ? WHERE bir = ?",new_p)
                self.tab.commit()
            if HA2 == ik_k[i][0]:
                new_p = [str(int(bi_k[i][1])+int(HA2P)),bi_k[i][0]]
                self.tab_im.execute("UPDATE takim SET ik_pua = ? WHERE bir = ?",new_p)
                self.tab.commit()
            if MA1 == ik_k[i][0]:
                new_p = [str(int(bi_k[i][1])+int(MA1P)),bi_k[i][0]]
                self.tab_im.execute("UPDATE takim SET ik_pua = ? WHERE bir = ?",new_p)
                self.tab.commit()
            if MA2 == ik_k[i][0]:
                new_p = [str(int(bi_k[i][1])+int(MA2P)),bi_k[i][0]]
                self.tab_im.execute("UPDATE takim SET ik_pua = ? WHERE bir = ?",new_p)
                self.tab.commit()
            if HK1 == ik_k[i][0]:
                new_p = [str(int(bi_k[i][1])+int(HK1P)),bi_k[i][0]]
                self.tab_im.execute("UPDATE takim SET ik_pua = ? WHERE bir = ?",new_p)
                self.tab.commit()
            if HK2 == ik_k[i][0]:
                new_p = [str(int(bi_k[i][1])+int(HK2P)),bi_k[i][0]]
                self.tab_im.execute("UPDATE takim SET ik_pua = ? WHERE bir = ?",new_p)
                self.tab.commit()
            if MK1 == ik_k[i][0]:
                new_p = [str(int(bi_k[i][1])+int(MK1P)),bi_k[i][0]]
                self.tab_im.execute("UPDATE takim SET ik_pua = ? WHERE bir = ?",new_p)
                self.tab.commit()
            if MK2 == ik_k[i][0]:
                new_p = [str(int(bi_k[i][1])+int(MK2P)),bi_k[i][0]]
                self.tab_im.execute("UPDATE takim SET ik_pua = ? WHERE bir = ?",new_p)
                self.tab.commit()
        for i in range(len(puan)):
            if HA1 == bi_k[i][0]:
                new_p = [str(int(bi_k[i][1])+int(HA1P)),bi_k[i][0]]
                self.tab_im.execute("UPDATE takim SET bi_pua = ? WHERE bir = ?",new_p)
                self.tab.commit()
            if HA2 == bi_k[i][0]:
                new_p = [str(int(bi_k[i][1])+int(HA2P)),bi_k[i][0]]
                self.tab_im.execute("UPDATE takim SET bi_pua = ? WHERE bir = ?",new_p)
                self.tab.commit()
            if MA1 == bi_k[i][0]:
                new_p = [str(int(bi_k[i][1])+int(MA1P)),bi_k[i][0]]
                self.tab_im.execute("UPDATE takim SET bi_pua = ? WHERE bir = ?",new_p)
                self.tab.commit()
            if MA2 == bi_k[i][0]:
                new_p = [str(int(bi_k[i][1])+int(MA2P)),bi_k[i][0]]
                self.tab_im.execute("UPDATE takim SET bi_pua = ? WHERE bir = ?",new_p)
                self.tab.commit()
            if HK1 == bi_k[i][0]:
                new_p = [str(int(bi_k[i][1])+int(HK1P)),bi_k[i][0]]
                self.tab_im.execute("UPDATE takim SET bi_pua = ? WHERE bir = ?",new_p)
                self.tab.commit()
            if HK2 == bi_k[i][0]:
                new_p = [str(int(bi_k[i][1])+int(HK2P)),bi_k[i][0]]
                self.tab_im.execute("UPDATE takim SET bi_pua = ? WHERE bir = ?",new_p)
                self.tab.commit()
            if MK1 == bi_k[i][0]:
                new_p = [str(int(bi_k[i][1])+int(MK1P)),bi_k[i][0]]
                self.tab_im.execute("UPDATE takim SET bi_pua = ? WHERE bir = ?",new_p)
                self.tab.commit()
            if MK2 == bi_k[i][0]:
                new_p = [str(int(bi_k[i][1])+int(MK2P)),bi_k[i][0]]
                self.tab_im.execute("UPDATE takim SET bi_pua = ? WHERE bir = ?",new_p)
                self.tab.commit()
        self.sonuc_gir.HAP.setText(str(hap))
        self.sonuc_gir.MAP.setText(str(map))
        self.sonuc_gir.HKP.setText(str(hkp))
        self.sonuc_gir.MKP.setText(str(mkp))
        self.sonuc_gir.HA1P.clear()
        self.sonuc_gir.HA2P.clear()
        self.sonuc_gir.MA1P.clear()
        self.sonuc_gir.MA2P.clear()
        self.sonuc_gir.HK1P.clear()
        self.sonuc_gir.HK2P.clear()
        self.sonuc_gir.MK1P.clear()
        self.sonuc_gir.MK2P.clear()

class Konu_Gor_Page(QWidget):

    def __init__(self):
        super().__init__()
        self.konu_gor = konu_g.Ui_Form()
        self.konu_gor.setupUi(self)
        self.konu_gor.Konu.clicked.connect(self.the_Konu)
        self.konu_gor.Info.clicked.connect(self.the_Info)

    def the_Konu(self):
        threading.Thread(target = self.Konu,).start()

    def the_Info(self):
        threading.Thread(target = self.Info,).start()

    def Konu(self):
        self.konu_gor.Konu_Gor.setText(konu)

    def Info(self):
        self.konu_gor.Info_Gor.setText(info)


app = QApplication([])
window = MainPage()
window.show()
app.exec()
