#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
#sucelje za "admina": kalendar u kojem ce svaki admin moci unjeti svoj 
#raspored smjene. Moze odabrati dane i sate. 
#takoder moze pogledati raspored samo za sebe, tj rezerviorane termine.

#sucelje za korisnika(veternira): 
#upitnik s pitanjima na koja ce 
#se moci odgovoriti ili oznacavanjem kucice ili upisivanjem s tipkovnice
#pitanja: kojeg veterinara zelite? (kucica)
#koja je vasa zivotinja? (kucica pas, macka, itd ili upis iz tipkovnice 
#ako je nesto sto nije navedeno)
#razlog posjeta (kucica i upis s tipkovnice)

#neka od pitanja tj odgovora otvaraju nova pitanja
#termin koji vam odgovara (mjesec dana unaprijed) i onda se bira ovisno
#o veterinaru tj njegovoj smjeni neki od slobodnih termina koji
#takoder ovisi i o duljini trajanja posjeta (uanprijed odredeno kada se
#oznaci razlog posjeta)
#nakon ispnjavanja ankete dobije se kratki podsjetnik koji se mozda moze
#isprintat
#takoder se i adminov rapored moze isprintati

from Tkinter import *
from datetime import timedelta
import tkFont
import sqlite3 as lite
import calendar as cal
import datetime
import time


class VetOs(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="#829ED5")   
        self.parent = parent
        self.font=tkFont.Font(size=11)
        self.font2=tkFont.Font(weight="bold")
        self.initUI()
      
    def initUI(self):
        self.parent.title(u"vetOS")
        self.pack(fill=BOTH, expand=1)
        
        string=u"vetOS - aplikacija za veterinare"
        L1 = Label(self, text=string,  font=self.font2, bg="#829ed5")
        L1.pack()
        L1.place(x=400, y=100, anchor=CENTER)
        
        B1 = Button(self, text =u"Nova rezervacija", command=self.narudzba)
        B1.pack()
        B1.place(x=400, y=400, anchor=CENTER)
        
        B2 = Button(self, text =u"Prikaz rasporeda", command=self.raspored)
        B2.pack()
        B2.place(x=400, y=450, anchor=CENTER)
         
    def raspored(self):
        
        self.raspored = Toplevel(bg="#829ed5")
        self.raspored.geometry ("1000x800+100+100")
        self.raspored.title(u"raspored")
        
        okvir1 =  Frame (self.raspored, bg="#829ed5")
        okvir1.pack()
        okvir1.place(x=500, y=50, anchor=CENTER)
        
        dugme_vet1 = Button(okvir1, text =u"1. veterinar")
        dugme_vet1.grid(column=1, row=1, sticky=N, padx=10 , pady=10)
       
        dugme_vet2 = Button(okvir1, text =u"2. veterinar")
        dugme_vet2.grid(column=2, row=1, sticky=N, padx=10 , pady=10)
            
            
        dugme_vet3 = Button(okvir1, text =u"3. veterinar")
        dugme_vet3.grid(column=3, row=1, sticky=N, padx=10 , pady=10)
        
               
        okvir2 = Frame (self.raspored, bg="#A1B7E2")
        okvir2.pack()
        okvir2.place(x=500, y=150, anchor = CENTER)
       
        lista = self.setDan()
                
        dan1 = Label(okvir2, text=lista[0], bg="#829ED5", font=self.font2)
        dan1.grid(column=1, row=1, sticky=N, padx=25, pady=10)
        
        dan2 = Label(okvir2, text=lista[1], bg="#829ED5", font=self.font2)
        dan2.grid(column=2, row=1, sticky=N, padx=25, pady=10)
        
        dan3 = Label(okvir2, text=lista[2], bg="#829ED5", font=self.font2)
        dan3.grid(column=3, row=1, sticky=N, padx=25, pady=10)
        
        dan4 = Label(okvir2, text=lista[3], bg="#829ED5", font=self.font2)
        dan4.grid(column=4, row=1, sticky=N, padx=25, pady=10)
        
        dan5 = Label(okvir2, text=lista[4], bg="#829ED5", font=self.font2)
        dan5.grid(column=5, row=1, sticky=N, padx=25, pady=10)
        
        dan6 = Label(okvir2, text=lista[5], bg="#829ED5", font=self.font2)
        dan6.grid(column=6, row=1, sticky=N, padx=25, pady=10)
        
    def setDan(self):
        
        d = timedelta(days=1)
        lista= [None] * 6       
        for i in range (6):
            if (i==0):
                lista[i] = datetime.date.today() - d
            elif (i==1): 
                lista[i] = datetime.date.today()
            else:
                lista[i] = lista[i-1] + d
        return lista
        
                     
    def narudzba(self): 
    
        self.narudzba = Toplevel(bg="#829ED5" )
        self.narudzba.geometry ("1000x1000+400+50")
        self.narudzba.title(u"Nova rezervacija")
        
        L1 = Label(self.narudzba, text=u"Unesite rezervaciju:", font=self.font2, bg="#829ED5")
        L1.pack()
        L1.place(x=150, y=80, anchor=W)
        
        L2 = Label (self.narudzba, text=u"Odaberite vetrinara kod kojeg želite pregled:", 
        font=self.font, bg="#829ED5")
        L2.pack()
        L2.place(x=150, y=130, anchor=W)
        
        self.var=IntVar()
        
        R1 = Radiobutton(self.narudzba, text=u"1. veterinar", 
        command=self.setVet, variable=self.var, value=1,  bg="#829ED5")
        R1.config(highlightthickness=0)
        R1.pack()
        R1.place(x=150, y=150, anchor=W)
        
        R2 = Radiobutton(self.narudzba, text=u"2. veterinar", 
        command=self.setVet, variable=self.var, value=2, bg="#829ED5")
        R2.config(highlightthickness=0)
        R2.pack()
        R2.place(x=150, y=170, anchor=W)

        R3 = Radiobutton(self.narudzba, text=u"3. veterinar", 
        command=self.setVet, variable=self.var, value=3, bg="#829ED5")
        R3.config(highlightthickness=0)
        R3.pack()
        R3.place(x=150, y=190, anchor=W)
         
        L3 = Label(self.narudzba, text=u"Vrsta životinje:",font=self.font, bg="#829ED5")
        L3.pack()
        L3.place(x=150, y=230, anchor=W)
       
        self.var1=IntVar()
        
        R4 = Radiobutton(self.narudzba, text=u"pas", variable=self.var1, 
        command=self.setVrsta, value=1,  bg="#829ED5")
        R4.config(highlightthickness=0)
        R4.pack()
        R4.place(x=150, y=250, anchor=W)
       
        R5 = Radiobutton(self.narudzba, text=u"mačka", variable=self.var1,
        command=self.setVrsta, value=2,  bg="#829ED5")
        R5.config(highlightthickness=0)
        R5.pack()
        R5.place(x=150, y=270, anchor=W)
        
        R6 = Radiobutton(self.narudzba, text=u"mala životinja (hrčak, ptica...)", 
        variable=self.var1, value=3, command=self.setVrsta, bg="#829ED5")
        R6.config(highlightthickness=0)
        R6.pack()
        R6.place(x=150, y=290, anchor=W)
        
        R7 = Radiobutton(self.narudzba, text=u"ostalo", variable=self.var1, 
        value=4,  command=self.zivotinja, bg="#829ED5")
        R7.config(highlightthickness=0)
        R7.pack()
        R7.place(x=150, y=310, anchor=W)
        
        L4 = Label(self.narudzba, text=u"Ime životinje:", font=self.font, bg="#829ED5")
        L4.pack()
        L4.place(x=150, y=350, anchor=W)
        
        self.E4 = Entry(self.narudzba, width=20)
        self.E4.pack()
        self.E4.place(x=150, y=370, anchor=W)

        B4 = Button(self.narudzba, text =u"Potvrdi unos", command=self.setImeZiv)
        B4.pack()
        B4.place(x=600, y=365, anchor=CENTER)
        
        L5 = Label(self.narudzba, text=u"Vaše ime i prezime:", font=self.font, bg="#829ED5")
        L5.pack()
        L5.place(x=150, y=410, anchor=W)
        
        self.E5 = Entry(self.narudzba, width=30)
        self.E5.pack()
        self.E5.place(x=150, y=430, anchor=W)
        
        B5 = Button(self.narudzba, text =u"Potvrdi unos", command=self.setImeVla)
        B5.pack()
        B5.place(x=600, y=430, anchor=CENTER)
        
        L6 = Label(self.narudzba, text=u"Razlog dolaska:", font=self.font, bg="#829ED5")
        L6.pack()
        L6.place(x=150, y=470, anchor=W)
       
        self.var2=IntVar()
        
        R8 = Radiobutton(self.narudzba, text=u"pregled", variable=self.var2, 
        value=1, command=self.setRazlog, bg="#829ED5")
        R8.config(highlightthickness=0)
        R8.pack()
        R8.place(x=150, y=490, anchor=W)
       
        R10 = Radiobutton(self.narudzba, text=u"pretraga", variable=self.var2,
        value=2,  command=self.setRazlog, bg="#829ED5")
        R10.config(highlightthickness=0)
        R10.pack()
        R10.place(x=150, y=510, anchor=W)
        
        R11 = Radiobutton(self.narudzba, text=u"cijepljenje/čipiranje", variable=self.var2,
        value=3, command=self.setRazlog, bg="#829ED5")
        R11.config(highlightthickness=0)
        R11.pack()
        R11.place(x=150, y=530, anchor=W)
        
        
        R12 = Radiobutton(self.narudzba, text=u"kontrola", variable=self.var2,
        value=4, command=self.setRazlog, bg="#829ED5")
        R12.config(highlightthickness=0)
        R12.pack()
        R12.place(x=150, y=550, anchor=W)
        
        R13 = Radiobutton(self.narudzba, text=u"operacija", variable=self.var2, 
        command=self.setRazlog, value=5, bg="#829ED5")
        R13.config(highlightthickness=0)
        R13.pack()
        R13.place(x=150, y=570, anchor=W)
        
        R14 = Radiobutton(self.narudzba, text=u"ostalo", variable=self.var2, value=6,
        command=self.razlog, bg="#829ED5")
        R14.config(highlightthickness=0)
        R14.pack()
        R14.place(x=150, y=590, anchor=W)
        
        L7 = Label(self.narudzba, text=u"Odaberite datum:", font=self.font, bg="#829ED5")
        L7.pack()
        L7.place(x=150, y=650, anchor=W)

        now = datetime.datetime.now()
        self.setDate(now.month, now.year)
        
        self.calOkvir = Frame(self.narudzba)
        self.calOkvir.pack()
        self.calOkvir.place(x=150, y=760, anchor=W)

        self.Lcal = Label(self.calOkvir, text=self.prikaz_mjeseca, font='courier',
        bg="#829ED5")
        self.Lcal.pack(fill=BOTH)
        # Lcal.place(padx=3, pady=5, anchor=S)
        self.Bprev = Button(self.calOkvir, text="<", font='courier', bg="#829ED5")
        self.Bprev.pack(side=LEFT)
        self.Bprev.bind("<Button-1>", self.prevCallback)
        self.Bnext = Button(self.calOkvir, text=">", font='courier', bg="#829ED5")
        self.Bnext.bind("<Button-1>", self.nextCallback)
        self.Bnext.pack(side=RIGHT)

        
        L8 = Label(self.narudzba, text=u"Odaberite vrijeme:", font=self.font, bg="#829ED5")
        L8.pack()
        L8.place(x=500, y=650, anchor=W)
        L9 = Label(self.narudzba, text=u"YYYY-MM-DD HH:MM", font=self.font, bg="#829ED5")
        L9.pack()
        L9.place(x=500, y=675, anchor=W)

        self.E8 = Entry(self.narudzba, width=20)
        self.E8.pack()
        self.E8.place(x=500, y=700, anchor=W)

        B8 = Button(self.narudzba, text =u"Potvrdi unos", command=self.setDatum)
        B8.pack()
        B8.place(x=500, y=750, anchor=W)

        B2 = Button(self.narudzba, text =u"Potvrdi rezervaciju", command=self.insertBase)
        B2.pack()
        B2.place(x=200, y=950, anchor=CENTER)

        """L2 = Label(narudzba, text="Koja je vaša životinja?")
        L2.grid(column=2,row=4,sticky=W)
        self.zivotinja = StringVar()
        self.unos2 = Entry(narudzba,textvariable=self.zivotinja, width=20)
        self.unos2.grid(column=2, row=4, sticky=W)
        self.unos2.bind("<Return>", self.OnPressEnter)
        self.zivotinja.set(u"Ovdje unesi ime životnje.")
        self.potvrda2 = Button(narudzba, text ="Potvrda", command=self.OnPressButton)
        self.potvrda2.grid(column=2, row=5, sticky=W)

        L3 = Label(narudzba, text="Razlog posjeta?")
        L3.grid(column=2,row=6,sticky=W)
        self.razlog_posjeta = StringVar()
        self.unos3 = Text(narudzba, width=60, height=10)
        self.unos3.grid(column=2, row=7, sticky=W)
        # self.unos3.bind("<Return>", self.OnPressEnter)
        self.razlog_posjeta.set(u"Ovdje unesi razlog posjeta.")
        self.potvrda3 = Button(narudzba, text ="Potvrda", command=self.OnPressButton)
        self.potvrda3.grid(column=2, row=8, sticky=W)"""
    
    def zivotinja(self):
        self.zivotinja = StringVar()
        self.zivotinja.set(u"Ovdje unesite vrstu životnje:")
        self.unos2 = Entry(self.narudzba, textvariable=self.zivotinja, width=30)
        self.unos2.pack()
        self.unos2.place(x=250, y=305)
        self.var1.set(4)
        B = Button(self.narudzba, text =u"Potvrdi unos", command=self.setVrsta)
        B.pack()
        B.place(x=600, y=315, anchor=CENTER)
        
    def razlog(self):
        self.unos3 = Text(self.narudzba, width=35, height=2)        
        self.unos3.insert(INSERT, u"ostalo")
        self.unos3.pack()
        self.unos3.place(x=250, y=585)
        self.var2.set(6)
        B = Button(self.narudzba, text =u"Potvrdi unos", command=self.setRazlog)
        B.pack()
        B.place(x=600, y=600, anchor=CENTER)
        
    def setVet(self):
        if (self.var.get()==1) : self.vet=u"1. veterinar"
        elif (self.var.get()==2): self.vet=u"2. veterinar"
        elif (self.var.get()==3): self.vet=u"3. veterinar"
        else: self.vet="nema unosa"
        
        print self.vet
        print self.var.get()
        return self.vet
        
    def setVrsta(self):
        if (self.var1.get()==1) : self.vrsta=u"pas"
        elif (self.var1.get()==2): self.vrsta=u"mačka"
        elif (self.var1.get()==3): self.vrsta=u"mala zivotinja"
        elif (self.var1.get()==4): self.vrsta=self.zivotinja.get()
        else: self.vrsta=u"nema unosa"
       
        return self.vrsta

    def setImeZiv(self):
        self.imeZiv = self.E4.get()
        print self.imeZiv
        return self.imeZiv

    def setImeVla(self):
        self.imeVla = self.E5.get()
        print self.imeVla
        return self.imeVla

    def setRazlog(self):
        if (self.var2.get()==1) : self.razlog=u"pregled"
        elif (self.var2.get()==2): self.razlog=u"pretraga"
        elif (self.var2.get()==3): self.razlog=u"cijepljenje/čipiranje"
        elif (self.var2.get()==4): self.razlog=u"kontrola"
        elif (self.var2.get()==5): self.razlog=u"operacija"
        elif (self.var2.get()==6): self.razlog=self.unos3.get(0.1, END)
        else: self.vrsta=u"nema unosa"
       
        return self.razlog

    def setDatum(self):
        datum = self.E8.get()

        return datum

    def prevCallback(self, event):
        self.Lcal.pack_forget()
        self.Bprev.pack_forget()
        self.Bnext.pack_forget()
        self.prevMonth()
        
        self.Lcal = Label(self.calOkvir, text=self.prikaz_mjeseca, font='courier',
        bg="#829ED5")
        self.Lcal.pack(fill=BOTH)
        self.Bprev.pack(side=LEFT)
        self.Bnext.pack(side=RIGHT)
        
    def nextCallback(self, event):
        self.Lcal.pack_forget()
        self.Bprev.pack_forget()
        self.Bnext.pack_forget()
        self.nextMonth()
        
        self.Lcal = Label(self.calOkvir, text=self.prikaz_mjeseca, font='courier',
        bg="#829ED5")
        self.Lcal.pack(fill=BOTH)
        self.Bprev.pack(side=LEFT)
        self.Bnext.pack(side=RIGHT)

    def setDate(self, month, year):
        self.year = year
        self.month = month
        self.prikaz_mjeseca = cal.month(self.year, self.month)
        print self.prikaz_mjeseca

    def prevMonth(self):
        month = self.month - 1
        if (month == 0): 
            month = 12
            year = self.year - 1
        else:
            year = self.year
        self.setDate(month, year)

    def nextMonth(self):
        month = self.month + 1
        if (month == 13):
            month = 1
            year = self.year + 1
        else:
            year = self.year
        self.setDate(month, year)

    def insertBase(self):
        vet = self.setVet()
        vrsta = self.setVrsta()
        imeZiv = self.setImeZiv()
        imeVla = self.setImeVla()
        razlog = self.setRazlog()
        datum = self.setDatum()
        print vet, vrsta, imeZiv, razlog, datum 
        dodajNarudzbu(vet, vrsta, imeZiv, imeVla, razlog, datum)
        printQuery()

def main():
    createTable()
    printQuery()
    imeVet = "1. veterinar"
    printVet(imeVet)

    root = Tk()
    root.geometry("800x600+400+100")
    app = VetOs(root)
    root.mainloop()  

    # Close connection to Db
    queryCurs.close()

createDb = lite.connect('test.db')
queryCurs = createDb.cursor()

def createTable():
    queryCurs.execute('''CREATE TABLE IF NOT EXISTS narudzba 
    (id INTEGER PRIMARY KEY, veterinar TEXT, vrsta TEXT, imeZiv TEXT, 
    imeVla TEXT, razlog TEXT, datum DATETIME)''')

def dodajNarudzbu(veterinar, vrsta, imeZiv, imeVla, razlog, datum):
    queryCurs.execute('''INSERT INTO narudzba 
        (veterinar, vrsta, imeZiv, imeVla, razlog, datum) VALUES (?, ?, ?, ?, ?, ?)''',
        (veterinar, vrsta, imeZiv, imeVla, razlog, datum))
    # Important for writing changes to database file!
    createDb.commit()

def printQuery():
    queryCurs.execute("SELECT * FROM narudzba")
    for i in queryCurs:
        print i

def printVet(imeVet):
    vet = imeVet
    queryCurs.execute('''SELECT datum, vrsta, imeZiv, razlog FROM narudzba WHERE
    veterinar = ? ORDER BY DATETIME(datum, 'localtime')''', (vet,))
    for i in queryCurs:
        print i[0]
    return queryCurs

if __name__ == '__main__':
    main()  
