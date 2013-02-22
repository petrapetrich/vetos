#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
#sucelje za "admina": kalendar u kojem ce svaki admin moci unjeti svoj 
#raspored smjene. Moze odabrati dane i sate. 
#takoder moze pogledati raspored samo za sebe, tj rezerviorane termine.

#sucelje za korisnika(veternira): otvori se mali upitnik s pitanjima na koja ce 
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
        
        B1 = Button(self, text ="Nova narudzba", command=self.narudzba)
        B1.pack()
        B2 = Button(self, text ="Uvid u raspored", command=self.raspored)
        B2.pack()

    def raspored(self):
        # The Toplevel widget is used to provide a separate window
        # container.
        prozor_raspored= Toplevel(bg="white")
        prozor_raspored.geometry ("800x600+400+400")
        prozor_raspored.title("Raspored")
        
        B1 = Button(prozor_raspored, text ="Nova narudzba", command=self.narudzba)
        B1.pack()
    
    def narudzba(self):
         prozor_narudzba= Toplevel(bg="white")
         prozor_narudzba.geometry ("800x600+400+400")
         prozor_narudzba.title("Nova narudzba")
        
        
def main():
  
    root = Tk()
    root.geometry("800x600+300+300")
    app = VetOs(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
