import tkinter
from tkinter import *
from tkinter import filedialog as fdi
import cmi_fisa_b
import cmi_pacient_b


def get_selected_row(event):
    try:
        global selected_tuple
        index = lista_pacienti.curselection()[0]
        selected_tuple = lista_pacienti.get(index)
        efdo.delete(0, END)
        efdo.insert(END, selected_tuple[1])
        en.delete(0, END)
        en.insert(END, selected_tuple[2])
        ep.delete(0, END)
        ep.insert(END, selected_tuple[3])
        ea.delete(0, END)
        ea.insert(END, selected_tuple[4])
        ev.delete(0, END)
        ev.insert(END, selected_tuple[5])
        ecnp.delete(0, END)
        ecnp.insert(END, selected_tuple[6])
        enrt.delete(0, END)
        enrt.insert(END, selected_tuple[7])
        emp.delete(0, END)
        emp.insert(END, selected_tuple[8])
        eahc.delete(0, END)
        eahc.insert(END, selected_tuple[9])
        eap.delete(0, END)
        eap.insert(END, selected_tuple[10])
        eal.delete(0, END)
        eal.insert(END, selected_tuple[11])
        etu.delete(0, END)
        etu.insert(END, selected_tuple[12])
        edg.delete(0, END)
        edg.insert(END, selected_tuple[13])
        eds.delete(0, END)
        eds.insert(END, selected_tuple[14])
        eec.delete(0, END)
        eec.insert(END, selected_tuple[15])
    except IndexError:
        pass


def comanda_vizualizare():
    lista_pacienti.delete(0, END)
    for row in cmi_fisa_b.vizualizeaza():
        lista_pacienti.insert(END, row)


def comanda_cautare():
    lista_pacienti.delete(0, END)
    for row in cmi_fisa_b.cauta(foaie_de_observatie.get(), nume.get(), prenume.get(), adresa.get(), varsta.get(),
                                cnp.get(), nr_telefon.get(), motiv.get(), antecedente_heredo.get(),
                                antecedente_personale.get(), alergii.get(), tratamente_urmate.get(),
                                diagnostic_general.get(), diagnostic_stomatologic.get(), examene_complementare.get()):
        lista_pacienti.insert(END, row)


def comanda_adaugare():
    cmi_fisa_b.adauga(foaie_de_observatie.get(), nume.get(), prenume.get(), adresa.get(), varsta.get(),
                      cnp.get(), nr_telefon.get(), motiv.get(), antecedente_heredo.get(),
                      antecedente_personale.get(), alergii.get(), tratamente_urmate.get(),
                      diagnostic_general.get(), diagnostic_stomatologic.get(), examene_complementare.get())
    lista_pacienti.delete(0, END)
    lista_pacienti.insert(END, (foaie_de_observatie.get(), nume.get(), prenume.get(), adresa.get(), varsta.get(),
                                cnp.get(), nr_telefon.get(), motiv.get(), antecedente_heredo.get(),
                                antecedente_personale.get(), alergii.get(), tratamente_urmate.get(),
                                diagnostic_general.get(), diagnostic_stomatologic.get(), examene_complementare.get()))


def comanda_modificare():
    cmi_fisa_b.modifica(selected_tuple[0], foaie_de_observatie.get(), nume.get(), prenume.get(), adresa.get(),
                        varsta.get(), cnp.get(), nr_telefon.get(), motiv.get(), antecedente_heredo.get(),
                        antecedente_personale.get(), alergii.get(), tratamente_urmate.get(),
                        diagnostic_general.get(), diagnostic_stomatologic.get(), examene_complementare.get())


def comanda_stergere():
    def sterge_pacient():
        cmi_fisa_b.sterge(selected_tuple[0])
        window_notificare_stergere = Tk()
        lnotif = Label(window_notificare_stergere, text='Datele pacientului au fost sterse!', font=('Aerial 10'),
                       anchor=CENTER)
        lnotif.grid(row=0, column=2)
        f1 = window_stergere.destroy
        f2 = window_notificare_stergere.destroy
        bnotif = Button(window_notificare_stergere, text='OK', font=Canvas, command=lambda: [f1(), f2()])
        bnotif.grid(row=1, column=2)
        window_notificare_stergere.title('Confirmare')
        window_notificare_stergere.geometry('290x80')
        window_notificare_stergere.mainloop()
        window_notificare_stergere.destroy()

    window_stergere = Tk()
    lavert = Label(window_stergere, text='Esti sigur ca vrei sa stergi acest pacient?', font=('Aerial 10'),
                   anchor=CENTER)
    lavert.grid(row=0, column=2, columnspan=2)
    byes = Button(window_stergere, text='Da', font=Canvas, anchor=CENTER, command=sterge_pacient)
    byes.grid(row=2, column=2)
    bno = Button(window_stergere, text='Nu', font=Canvas, anchor=CENTER, command=window_stergere.destroy)
    bno.grid(row=2, column=3)
    window_stergere.title("Avertizare")
    window_stergere.geometry('300x80')
    window_stergere.mainloop()


def comanda_elimina_campuri():
    efdo.delete(0, END)
    en.delete(0, END)
    ep.delete(0, END)
    ea.delete(0, END)
    ev.delete(0, END)
    ecnp.delete(0, END)
    enrt.delete(0, END)
    emp.delete(0, END)
    eahc.delete(0, END)
    eap.delete(0, END)
    eal.delete(0, END)
    etu.delete(0, END)
    edg.delete(0, END)
    eds.delete(0, END)
    eec.delete(0, END)
    edata.delete(0, END)
    edinte.delete(0, END)
    ediag.delete(0, END)
    etra.delete(0, END)


def get_selected_row_vizite(event):
    try:
        global selected_tuple_vizite
        index = lista_vizite_pacient.curselection()[0]
        selected_tuple_vizite = lista_vizite_pacient.get(index)
        enviz.delete(0, END)
        enviz.insert(END, selected_tuple_vizite[1])
        epviz.delete(0, END)
        epviz.insert(END, selected_tuple_vizite[2])
        edata.delete(0, END)
        edata.insert(END, selected_tuple_vizite[3])
        edinte.delete(0, END)
        edinte.insert(END, selected_tuple_vizite[4])
        ediag.delete(0, END)
        ediag.insert(END, selected_tuple_vizite[5])
        etra.delete(0, END)
        etra.insert(END, selected_tuple_vizite[6])
    except IndexError:
        pass


def comanda_vizualizare_vizite():
    lista_vizite_pacient.delete(0, END)
    for row in cmi_pacient_b.vizualizeaza_vizita():
        lista_vizite_pacient.insert(END, row)


def comanda_cautare_vizite():
    lista_vizite_pacient.delete(0, END)
    for row in cmi_pacient_b.cauta_vizita(nume.get(), prenume.get(), edata.get(), edinte.get(), ediag.get(),
                                          etra.get()):
        lista_vizite_pacient.insert(END, row)


def comanda_adaugare_vizite():
    cmi_pacient_b.adauga_vizita(nume.get(), prenume.get(), edata.get(), edinte.get(), ediag.get(),
                                etra.get())
    lista_vizite_pacient.delete(0, END)
    lista_vizite_pacient.insert(END, (nume.get(), prenume.get(), edata.get(), edinte.get(), ediag.get(),
                                      etra.get()))


def comanda_modificare_vizite():
    cmi_pacient_b.modifica_vizita(selected_tuple_vizite[0], nume.get(), prenume.get(), edata.get(), edinte.get(),
                                  ediag.get(), etra.get())


def comanda_stergere_vizite():
    def sterge_pacient():
        index = lista_vizite_pacient.curselection()[0]
        selected_tuple_vizite = lista_vizite_pacient.get(index)
        cmi_pacient_b.sterge_vizita(selected_tuple_vizite[0])
        window_notificare_stergere = Tk()
        lnotif = Label(window_notificare_stergere, text='Datele vizitei au fost sterse!', font=('Aerial 10'),
                       anchor=CENTER)
        lnotif.grid(row=0, column=2)
        f1 = window_stergere.destroy
        f2 = window_notificare_stergere.destroy
        bnotif = Button(window_notificare_stergere, text='OK', font=Canvas, command=lambda: [f1(), f2()])
        bnotif.grid(row=1, column=2)
        window_notificare_stergere.title('Confirmare')
        window_notificare_stergere.geometry('270x70')
        window_notificare_stergere.mainloop()
        window_notificare_stergere.destroy()

    window_stergere = Tk()
    lavert = Label(window_stergere, text='Esti sigur ca vrei sa stergi datele acestei vizite?', font=('Aerial 10'),
                   anchor=CENTER)
    lavert.grid(row=0, column=2, columnspan=2)
    byes = Button(window_stergere, text='Da', font=Canvas, anchor=CENTER, command=sterge_pacient)
    byes.grid(row=2, column=2)
    bno = Button(window_stergere, text='Nu', font=Canvas, anchor=CENTER, command=window_stergere.destroy)
    bno.grid(row=2, column=3)
    window_stergere.title("Avertizare")
    window_stergere.geometry('360x80')
    window_stergere.mainloop()


def deschide_fisier():
    return fdi.askopenfile()


window = Tk()
window.title("CMI DR. Craciun Florentina-Liliana")
# window.state('zoomed') # full screen
window.geometry('1300x850')
# window.attributes('-alpha', 0.9) # opacity


image_wall = PhotoImage(file='bg_photo.PNG')
imagel = Label(window, image=image_wall)
imagel.place(x=-200, y=-0.5)

lfont = 'Helvetica 9 bold'

# =======================================================================
# Date pacient de introdus

lfdo = Label(window, text='FOAIE DE OBSERVATIE nr', font=lfont, bg='white')
lfdo.grid(row=0, column=0, sticky=E)

foaie_de_observatie = StringVar()
efdo = Entry(window, textvariable=foaie_de_observatie, width=15, font=Canvas, bd=3)
efdo.grid(row=0, column=1, sticky=W)

ln = Label(window, text='NUME', font=lfont, bg='white')
ln.grid(row=1, column=0, sticky=E)

nume = StringVar()
en = Entry(window, textvariable=nume, font=Canvas, bd=3)
en.grid(row=1, column=1, sticky=W)

lp = Label(window, text='PRENUME', font=lfont, bg='white')
lp.grid(row=2, column=0, sticky=E)

prenume = StringVar()
ep = Entry(window, textvariable=prenume, font=Canvas, bd=3)
ep.grid(row=2, column=1, sticky=W)

la = Label(window, text='ADRESA', font=lfont, bg='white')
la.grid(row=3, column=0, sticky=E)

adresa = StringVar()
ea = Entry(window, textvariable=adresa, font=Canvas, bd=3)
ea.grid(row=3, column=1, sticky=W)

lv = Label(window, text='VARSTA', font=lfont, bg='white')
lv.grid(row=4, column=0, sticky=E)

varsta = StringVar()
ev = Entry(window, textvariable=varsta, font=Canvas, bd=3)
ev.grid(row=4, column=1, sticky=W)

lcnp = Label(window, text='CNP', font=lfont, bg='white')
lcnp.grid(row=5, column=0, sticky=E)

cnp = StringVar()
ecnp = Entry(window, textvariable=cnp, font=Canvas, bd=3)
ecnp.grid(row=5, column=1, sticky=W)

lnrt = Label(window, text='NR. TELEFON', font=lfont, bg='white')
lnrt.grid(row=6, column=0, sticky=E)

nr_telefon = StringVar()
enrt = Entry(window, textvariable=nr_telefon, font=Canvas, bd=3)
enrt.grid(row=6, column=1, sticky=W)

lmp = Label(window, text='MOTIVUL PREZENTARII', font=lfont, bg='white')
lmp.grid(row=7, column=0, sticky=E)

motiv = StringVar()
emp = Entry(window, textvariable=motiv, font=Canvas, bd=3)
emp.grid(row=7, column=1, sticky=W)

lahc = Label(window, text='ANTECEDENTE HEREDO-COLATERALE', font=lfont, bg='white')
lahc.grid(row=8, column=0, sticky=E)

antecedente_heredo = StringVar()
eahc = Entry(window, textvariable=antecedente_heredo, font=Canvas, bd=3)
eahc.grid(row=8, column=1, sticky=W)

lap = Label(window, text='ANTECEDENTE PERSONALE', font=lfont, bg='white')
lap.grid(row=9, column=0, sticky=E)

antecedente_personale = StringVar()
eap = Entry(window, textvariable=antecedente_personale, font=Canvas, bd=3)
eap.grid(row=9, column=1, sticky=W)

lal = Label(window, text='ALERGII', font=lfont, bg='white')
lal.grid(row=10, column=0, sticky=E)

alergii = StringVar()
eal = Entry(window, textvariable=alergii, font=Canvas, bd=3)
eal.grid(row=10, column=1, sticky=W)

ltu = Label(window, text='TRATAMENTE URMATE', font=lfont, bg='white')
ltu.grid(row=11, column=0, sticky=E)

tratamente_urmate = StringVar()
etu = Entry(window, textvariable=tratamente_urmate, font=Canvas, bd=3)
etu.grid(row=11, column=1, sticky=W)

ldg = Label(window, text='DIAGNOSTIC GENERAL', font=lfont, bg='white')
ldg.grid(row=12, column=0, sticky=E)

diagnostic_general = StringVar()
edg = Entry(window, textvariable=diagnostic_general, font=Canvas, bd=3)
edg.grid(row=12, column=1, sticky=W)

lds = Label(window, text='DIAGNOSTIC STOMATOLOGIC', font=lfont, bg='white')
lds.grid(row=13, column=0, sticky=E)

diagnostic_stomatologic = StringVar()
eds = Entry(window, textvariable=diagnostic_stomatologic, font=Canvas, bd=3)
eds.grid(row=13, column=1, sticky=W)

lec = Label(window, text='EXAMENE COMPLEMENTARE', font=lfont, bg='white')
lec.grid(row=14, column=0, sticky=E)

examene_complementare = StringVar()
eec = Entry(window, textvariable=examene_complementare, font=Canvas, bd=3)
eec.grid(row=14, column=1, sticky=W)

# =======================================================================
# Lista pacienti
bgbuttons = '#E0FFFF'

badauga = Button(window, text='Adauga pacient', width=15, command=comanda_adaugare, bd=3, bg=bgbuttons)
badauga.grid(row=3, column=2)

bcauta = Button(window, text='Cauta pacient', width=15,  command=comanda_cautare, bd=3, bg=bgbuttons)
bcauta.grid(row=4, column=2)

bviz = Button(window, text='Afiseaza pacienti', width=15, command=comanda_vizualizare, bd=3, bg=bgbuttons)
bviz.grid(row=5, column=2)

bmodif = Button(window, text='Modifica date', width=15, command=comanda_modificare, bd=3, bg=bgbuttons)
bmodif.grid(row=7, column=2)

bsterg = Button(window, text='Sterge pacient', width=15, command=comanda_stergere, bd=3, bg='#FF4500')
bsterg.grid(row=8, column=2)

bviz = Button(window, text='Adauga vizita', width=15, command=comanda_adaugare_vizite, bd=3, bg=bgbuttons)
bviz.grid(row=16, column=2)

bcviz = Button(window, text='Cauta vizite', width=15, command=comanda_cautare_vizite, bd=3, bg=bgbuttons)
bcviz.grid(row=17, column=2)

baviz = Button(window, text='Afiseaza vizite', width=15, command=comanda_vizualizare_vizite, bd=3, bg=bgbuttons)
baviz.grid(row=18, column=2)

bmviz = Button(window, text='Modifica date', width=15, command=comanda_modificare_vizite, bd=3, bg=bgbuttons)
bmviz.grid(row=20, column=2)

bsviz = Button(window, text='Sterge vizita', width=15, command=comanda_stergere_vizite, bd=3, bg='#FF4500')
bsviz.grid(row=21, column=2)

belim = Button(window, text='Sterge campuri', width=11, command=comanda_elimina_campuri, bd=3, bg=bgbuttons)
belim.grid(row=15, column=1, sticky=W)

llista = Label(window, text='LISTA PACIENTI', font='Helvetica 10 bold', bg='white', justify=CENTER)
llista.grid(row=2, column=3, columnspan=2, sticky=S)

sb1 = Scrollbar(window, orient=VERTICAL)
sb1.grid(row=2, column=5, rowspan=12, sticky=W)
sb1h = Scrollbar(window, orient=HORIZONTAL)
sb1h.grid(row=12, column=3, columnspan=6)

lista_pacienti = Listbox(window, height=15, width=40, bd=3)
lista_pacienti.grid(row=1, column=3, rowspan=13, columnspan=2)

lista_pacienti.configure(yscrollcommand=sb1.set, xscrollcommand=sb1h.set)
sb1.configure(command=lista_pacienti.yview)
sb1h.configure(command=lista_pacienti.xview)

lista_pacienti.bind('<<ListboxSelect>>', get_selected_row)

bdeschid = Button(window, text='Radiografie', width=11, command=deschide_fisier, bd=3, bg=bgbuttons)
bdeschid.grid(row=23, column=1, sticky=S)

# =======================================================================
# Lista consultatii pacient

llista_vizite = Label(window, text='LISTA VIZITE PACIENT', font='Helvetica 10 bold', bg='white', justify=CENTER)
llista_vizite.grid(row=15, column=3, columnspan=2, sticky=S)

sb2 = Scrollbar(window, orient=VERTICAL)
sb2.grid(row=15, column=5, rowspan=12, sticky=W)
sb2h = Scrollbar(window, orient=HORIZONTAL)
sb2h.grid(row=25, column=3, columnspan=3, sticky=S)

lista_vizite_pacient = Listbox(window, height=12, width=40, bd=3)
lista_vizite_pacient.grid(row=16, column=3, rowspan=9, columnspan=2)

lista_vizite_pacient.configure(yscrollcommand=sb2.set, xscrollcommand=sb2h.set)
sb2.configure(command=lista_vizite_pacient.yview)
sb2h.configure(command=lista_vizite_pacient.xview)

lista_vizite_pacient.bind('<<ListboxSelect>>', get_selected_row_vizite)

lnviz = Label(window, text='NUME', font=lfont, bg='white')
lnviz.grid(row=16, column=0, sticky=E)

enviz = StringVar()
enviz = Entry(window, textvariable=nume, width=15, font=Canvas, bd=3)
enviz.grid(row=16, column=1, sticky=SW)

lpviz = Label(window, text='PRENUME', font=lfont, bg='white')
lpviz.grid(row=17, column=0, sticky=E)

epviz = StringVar()
epviz = Entry(window, textvariable=prenume, width=15, font=Canvas, bd=3)
epviz.grid(row=17, column=1, sticky=W)

ldata = Label(window, text='DATA', font=lfont, bg='white')
ldata.grid(row=18, column=0, sticky=E)

edata = StringVar()
edata = Entry(window, textvariable=edata, width=15, font=Canvas, bd=3)
edata.grid(row=18, column=1, sticky=W)

ldinte = Label(window, text='DINTE', font=lfont, bg='white')
ldinte.grid(row=19, column=0, sticky=E)

edinte = StringVar()
edinte = Entry(window, textvariable=edinte, width=15, font=Canvas, bd=3)
edinte.grid(row=19, column=1, sticky=W)

ldiag = Label(window, text='DIAGNOSTIC', font=lfont, bg='white')
ldiag.grid(row=20, column=0, sticky=E)

ediag = StringVar()
ediag = Entry(window, textvariable=ediag, width=40, font=Canvas, bd=3)
ediag.grid(row=20, column=1)

ltra = Label(window, text='TRATAMENT', font=lfont, bg='white')
ltra.grid(row=21, column=0, sticky=E)

etra = StringVar()
etra = Entry(window, textvariable=etra, width=40, font=Canvas, bd=3)
etra.grid(row=21, column=1)

# =======================================================================

window.mainloop()

# pyinstaller --onefile --window cmi_fisa_f.py
