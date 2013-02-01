#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#sucelje za "admina": kalendar u kojem ce svaki admin moci unjeti svoj 
#raspored smjene. Moze odabrati dane i sate. 
#takoder moze pogledati raspored samo za sebe, tj rezerviorane termine.

#sucelje za  korisnika: otvori se mali upitnik s pitanjima na koja ce 
#se moci odgovoriti ili oznacavanjem kucice ili upisivanjem s tipkovnice
#pitanja: kojeg veterinara zelite? (kucica)
#koja je vasa zivotinja? (kucica pas, macka, itd ili upis iz tipkovnice 
#ako je nesto sto nije navedeno)
#
#razlog posjeta (kucica i upis s tipkovnice)
#neka od pitanja tj odgovora otvaraju nova pitanja
#termin koji vam odgovara (mjesec dana unaprijed) i onda se bira ovisno
#o veterinaru tj njegovoj smjeni neki od slobodnih termina koji
#takoder ovisi i o duljini trajanja posjeta (uanprijed odredeno kada se
#oznaci razlog posjeta)
#nakon ispnjavanja ankete dobije se kratki podsjetnik koji se mozda moze
#isprintat
#takoder se i adminov rapored moze isprintati


from tkinter import *




def main():
    


    app = Tk()
    app.title("vetOS")
    app.geometry('800x600+100+100')

    
    button1 = Button(app, text="Nova narudzba", width=30)
    button1.pack(side='left', padx=15,pady=15)
    
    button2 = Button(app, text="Unesi raspored", width=30)
    button2.pack(side='right', padx=15,pady=15)
    
    app.mainloop()

    
    return 0

if __name__ == '__main__':
    main()


