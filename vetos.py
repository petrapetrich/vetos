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
import sqlite3 as lite


class VetOs(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
        self.parent = parent
        self.initUI()
        
    def initUI(self):
        self.parent.title("vetOS")
        self.pack(fill=BOTH, expand=1)
        
        string="""VetOS - aplikacija za veterinare """
        L1 = Label(self, text=string)
        L1.pack()
        L1.place(relx=0.5, rely=0.1, anchor=CENTER)
        B1 = Button(self, text ="Nova narudzba", command=self.narudzba)
        B1.pack()
        B1.place(relx=0.5, rely=0.8, anchor=CENTER)
        B2 = Button(self, text ="Prikaz rasporeda", command=self.raspored)
        B2.pack()
        B2.place(relx=0.5, rely=0.9, anchor=CENTER)


    def raspored(self):
        # The Toplevel widget is used to provide a separate window
        # container.
        raspored = Toplevel(bg="white")
        raspored.geometry ("800x600+400+200")
        raspored.title("Raspored")
        L1 = Label(raspored, text="Prikaz rasporeda")
        L1.pack()
        L1.place(relx=0.5, rely=0.1, anchor=CENTER)
        
        B1 = Button(raspored, text ="Nova narudzba", command=self.narudzba)
        B1.pack()
        B1.place(relx=0.5, rely=0.8, anchor=CENTER)

    
    def narudzba(self):
        narudzba = Toplevel(bg="white")
        narudzba.geometry ("800x600+400+200")
        narudzba.title("Nova narudzba")
        narudzba.grid()
        
        L1 = Label(narudzba, text="Unesi narudzbu")
        L1.grid(column=3,row=1,sticky=N, columnspan=4)
        
        L2 = Label(narudzba, text="Koja je vaša životinja?")
        L2.grid(column=2,row=3,sticky=W)
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
        self.potvrda3.grid(column=2, row=8, sticky=W)

        for child in narudzba.winfo_children():
            child.grid_configure(padx=10, pady=10)

    def OnPressEnter(self,event):
        self.prikaz.set( self.zivotinja.get())
        self.prikaz2.focus_set()
        self.prikaz2.selection_range(0, END)

    def OnPressButton(self):
        print self.razlog_posjeta.get()
        dodajNarudzbu('kurevija', 'pas', 'loro', 'cijepljenje', '2013-02-25', '16:00')
        printQuery()

def main():
    createTable()
    printQuery()

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
    (id INTEGER PRIMARY KEY, veterinar TEXT, vrsta TEXT, ime TEXT, 
    razlog TEXT, datum TEXT, vrijeme TEXT)''')

def dodajNarudzbu(veterinar, vrsta, ime, razlog, datum, vrijeme):
    queryCurs.execute('''INSERT INTO narudzba 
        (veterinar, vrsta, ime, razlog, datum, vrijeme) VALUES (?, ?, ?, ?, ?, ?)''',
        (veterinar, vrsta, ime, razlog, datum, vrijeme))
    # Important for writing changes to database file!
    createDb.commit()

def printQuery():
    queryCurs.execute("SELECT * FROM narudzba")
    for i in queryCurs:
        print i

if __name__ == '__main__':
    main()  
