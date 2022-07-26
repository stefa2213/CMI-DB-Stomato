import sqlite3
from pprint import pprint


def connect_vizita():
    conn = sqlite3.connect('cmi_cfl.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS vizite (id INTEGER PRIMARY KEY, nume text, prenume text, '
                'data text, dinte text, diagnostic text, tratament text)')
    conn.commit()
    conn.close()


def adauga_vizita(nume, prenume, data, dinte, diagnostic, tratament):
    conn = sqlite3.connect('cmi_cfl.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO vizite VALUES (NULL,?,?,?,?,?,?)',
                (nume, prenume, data, dinte, diagnostic, tratament))
    conn.commit()
    conn.close()


def vizualizeaza_vizita():
    conn = sqlite3.connect('cmi_cfl.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM vizite')
    rows = cur.fetchall()
    conn.close()
    return rows


def cauta_vizita(nume='', prenume='', data='', dinte='', diagnostic='', tratament=''):
    conn = sqlite3.connect('cmi_cfl.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM vizite WHERE nume=? OR prenume=? OR data=? OR dinte=? OR diagnostic=? OR tratament=?',
                (nume, prenume, data, dinte, diagnostic, tratament))
    rows = cur.fetchall()
    conn.close()
    return rows


def sterge_vizita(id):
    conn = sqlite3.connect('cmi_cfl.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM vizite WHERE id=?', (id,))
    conn.commit()
    conn.close()


def modifica_vizita(id, nume, prenume, data, dinte, diagnostic, tratament):
    conn = sqlite3.connect('cmi_cfl.db')
    cur = conn.cursor()
    cur.execute('UPDATE vizite SET nume=?, prenume=?, data=?, dinte=?, diagnostic=?, tratament=? WHERE id=?',
                (nume, prenume, data, dinte, diagnostic, tratament, id))
    conn.commit()
    conn.close()


connect_vizita()
