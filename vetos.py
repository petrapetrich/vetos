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
import tkFont
import sqlite3 as lite


class VetOs(Frame):

  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="#829ED5")   
        self.parent = parent
        self.font=tkFont.Font(size=11)
        self.font2=tkFont.Font(weight="bold")
        self.initUI()
      
    def initUI(self):
        self.parent.title("vetOS")
        self.pack(fill=BOTH, expand=1)
        
        string="""vetOS - aplikacija za veterinare """
        L1 = Label(self, text=string,  font=self.font2, bg="#829ED5")
        L1.pack()
        L1.place(x=400, y=100, anchor=CENTER)
        
        B1 = Button(self, text ="Nova rezervacija", command=self.narudzba)
        B1.pack()
        B1.place(x=400, y=400, anchor=CENTER)
        
        B2 = Button(self, text ="Prikaz rasporeda", command=self.raspored)
        B2.pack()
        B2.place(x=400, y=450, anchor=CENTER)
         
    def raspored(self):
        
        raspored = Toplevel(bg="#829ED5")
        raspored.geometry ("1000x800+400+200")
        raspored.title("Raspored")
        
                     
    def narudzba(self): 
    
       
        self.narudzba = Toplevel(bg="#829ED5" )
        self.narudzba.geometry ("1000x1000+400+200")
        self.narudzba.title("Nova rezervacija")
        
        L1 = Label(self.narudzba, text="Unesite rezervaciju:", font=self.font2, bg="#829ED5")
        L1.pack()
        L1.place(x=150, y=80, anchor=W)
        
        L2 = Label (self.narudzba, text="Odaberite vetrinara kod kojeg želite pregled:", font=self.font, bg="#829ED5")
        L2.pack()
        L2.place(x=150, y=130, anchor=W)
        
        var=IntVar()
        
        R1 = Radiobutton(self.narudzba, text="1. veterinar", variable=var, value=1,  bg="#829ED5")
        R1.config(highlightthickness=0)
        R1.pack()
        R1.place(x=150, y=150, anchor=W)
        


        R2 = Radiobutton(self.narudzba, text="2. veterinar", variable=var, value=2, bg="#829ED5")
        R2.config(highlightthickness=0)
        R2.pack()
        R2.place(x=150, y=170, anchor=W)

        R3 = Radiobutton(self.narudzba, text="3. veterinar", variable=var, value=3, bg="#829ED5")
        R3.config(highlightthickness=0)
        R3.pack()
        R3.place(x=150, y=190, anchor=W)
        
       
        L3 = Label(self.narudzba, text="Vrsta životinje:",font=self.font, bg="#829ED5")
        L3.pack()
        L3.place(x=150, y=230, anchor=W)
       
        var1=IntVar()
        
        R4 = Radiobutton(self.narudzba, text="pas", variable=var1, value=1,  bg="#829ED5")
        R4.config(highlightthickness=0)
        R4.pack()
        R4.place(x=150, y=250, anchor=W)
       
        R5 = Radiobutton(self.narudzba, text="mačka", variable=var1, value=2,  bg="#829ED5")
        R5.config(highlightthickness=0)
        R5.pack()
        R5.place(x=150, y=270, anchor=W)
        
        R6 = Radiobutton(self.narudzba, text="mala životinja (hrčak, ptica...)", variable=var1, value=3, bg="#829ED5")
        R6.config(highlightthickness=0)
        R6.pack()
        R6.place(x=150, y=290, anchor=W)
        
        R7 = Radiobutton(self.narudzba, text="ostalo", variable=var1, value=4,  command=self.zivotinja, bg="#829ED5")
        R7.config(highlightthickness=0)
        R7.pack()
        R7.place(x=150, y=310, anchor=W)
        
        L4 = Label(self.narudzba, text="Ime životinje:", font=self.font, bg="#829ED5")
        L4.pack()
        L4.place(x=150, y=350, anchor=W)
        
        E4 = Entry(self.narudzba, width=20)
        E4.pack()
        E4.place(x=150, y=370, anchor=W)
        
        L5 = Label(self.narudzba, text="Vaše ime i prezime:", font=self.font, bg="#829ED5")
        L5.pack()
        L5.place(x=150, y=410, anchor=W)
        
        E5 = Entry(self.narudzba, width=30)
        E5.pack()
        E5.place(x=150, y=430, anchor=W)
        
        
        L6 = Label(self.narudzba, text="Razlog dolaska:", font=self.font, bg="#829ED5")
        L6.pack()
        L6.place(x=150, y=470, anchor=W)
       
        var2=IntVar()
        
        R8 = Radiobutton(self.narudzba, text="pregled", variable=var2, value=1, bg="#829ED5")
        R8.config(highlightthickness=0)
        R8.pack()
        R8.place(x=150, y=490, anchor=W)
       
        R10 = Radiobutton(self.narudzba, text="pretraga", variable=var2, value=2,  bg="#829ED5")
        R10.config(highlightthickness=0)
        R10.pack()
        R10.place(x=150, y=510, anchor=W)
        
        R11 = Radiobutton(self.narudzba, text="cijepljenje/čipiranje", variable=var2, value=3,  bg="#829ED5")
        R11.config(highlightthickness=0)
        R11.pack()
        R11.place(x=150, y=530, anchor=W)
        
        
        R12 = Radiobutton(self.narudzba, text="kontrola", variable=var2, value=4, bg="#829ED5")
        R12.config(highlightthickness=0)
        R12.pack()
        R12.place(x=150, y=550, anchor=W)
        
        R13 = Radiobutton(self.narudzba, text="operacija", variable=var2, value=5, bg="#829ED5")
        R13.config(highlightthickness=0)
        R13.pack()
        R13.place(x=150, y=570, anchor=W)
        
        R14 = Radiobutton(self.narudzba, text="ostalo", variable=var2, value=6,command=self.razlog, bg="#829ED5")
        R14.config(highlightthickness=0)
        R14.pack()
        R14.place(x=150, y=590, anchor=W)
        
        
        L7 = Label(self.narudzba, text="Odaberite datum:", font=self.font, bg="#829ED5")
        L7.pack()
        L7.place(x=150, y=700, anchor=W)
        
        L8 = Label(self.narudzba, text="Odaberite vrijeme:", font=self.font, bg="#829ED5")
        L8.pack()
        L8.place(x=500, y=700, anchor=W)

        B2 = Button(self.narudzba, text ="Potvrdi rezervaciju", command=self.narudzba)
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
        self.potvrda3.grid(column=2, row=8, sticky=W)
        
    
    def zivotinja(self):
        self.zivotinja = StringVar()
        self.unos2 = Entry(self.narudzba, textvariable=self.zivotinja, width=30)
        self.unos2.pack()
        self.unos2.place(x=250, y=305)
        self.zivotinja.set(u"Ovdje unesite vrstu životnje:")
        
    def razlog(self):
        self.razlog_posjeta = StringVar()
        self.unos3 = Text(self.narudzba, width=30, height=6)        
        self.unos3.pack()
        self.unos3.place(x=250, y=585)

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
