import sqlite3 as sq3
class yap():
    tab = sq3.connect("Deneme")
    im_tab = tab.cursor()
    def __init__(self):
        self.kod()
    def kod(self):
        self.im_tab.execute("SELECT * FROM takim")
        self.veri = self.im_tab.fetchall()
        for i in range(len(self.veri)-1):
            for j in range(len(self.veri)-1):
                if int(self.veri[i][4]) < int(self.veri[j][4]):
                    self.veri[i], self.veri[j] = self.veri[j], self.veri[i]
                else:
                    continue
        print(self.veri)
        for i in range(len(self.veri)-1):
            for j in range(len(self.veri)-1):
                if (int(self.veri[j][5])+int(self.veri[j][6])) < (int(self.veri[j+1][5])+int(self.veri[j+1][6])):
                    if int(self.veri[i][4]) == int(self.veri[j][4]):
                        self.veri[i], self.veri[j+1] = self.veri[j+1], self.veri[i]

        print(self.veri)
anan = yap()
