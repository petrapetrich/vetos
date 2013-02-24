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
        
        L1 = Label(narudzba, text="Unesi narudzba")
        L1.pack()
        L1.place(relx=0.5, rely=0.1, anchor=CENTER)
        
        L2 = Label(narudzba, text="Koja je vaša životinja?")
        L2.pack()
        L2.place(relx=0.5, rely=0.2, anchor=CENTER)
        L3 = Label(narudzba, text="Ralog posjeta?")
        L3.pack()
        L3.place(relx=0.5, rely=0.3, anchor=CENTER)

        # self.entry je dostupan svim f u klasi
        # self.entryVariable = StringVar()
        # self.entry = Entry(narudzba,textvariable=self.entryVariable, width=50)
        # self.entry.focus_set()
        # self.entry.pack()
        # self.place(relx=0.5, rely=0.35, anchor=CENTER)
        # self.entry.bind("<Return>", self.OnPressEnter)
        # self.entryVariable.set(u"Enter text here.")
        # self.labelVariable = StringVar()
        # label = Label(self,textvariable=self.labelVariable, anchor="w",fg="white",bg="blue")

    # def OnPressEnter(self,event):
    #     # self.labelVariable.set( self.entryVariable.get()+" (You pressed ENTER)" )
    #     self.entry.focus_set()
    #     self.entry.selection_range(0, END)

def main():
  
    root = Tk()
    root.geometry("800x600+400+100")
    app = VetOs(root)
    root.mainloop()  

if __name__ == '__main__':
    main()  
