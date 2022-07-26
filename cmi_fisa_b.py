import sqlite3
from pprint import pprint


def connect():
    conn = sqlite3.connect('cmi_cfl.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS cmi (id INTEGER PRIMARY KEY, foaie_de_observatie text, nume text, '
                'prenume text, adresa text, varsta text, cnp text, nr_telefon text, motiv text, '
                'antecedente_heredo text, antecedente_personale text, alergii text, tratamente_urmate text, '
                'diagnostic_general text, diagnostic_stomatologic text, examene_complementare text)')
    conn.commit()
    conn.close()


def adauga(foaie_de_observatie, nume, prenume, adresa, varsta, cnp, nr_telefon, motiv, antecedente_heredo,
           antecedente_personale, alergii, tratamente_urmate, diagnostic_general, diagnostic_stomatologic,
           examene_complementare):
    conn = sqlite3.connect('cmi_cfl.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO cmi VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                (foaie_de_observatie, nume, prenume, adresa, varsta, cnp, nr_telefon, motiv, antecedente_heredo,
                 antecedente_personale, alergii, tratamente_urmate, diagnostic_general, diagnostic_stomatologic,
                 examene_complementare))
    conn.commit()
    conn.close()


def vizualizeaza():
    conn = sqlite3.connect('cmi_cfl.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM cmi')
    rows = cur.fetchall()
    conn.close()
    return rows


def cauta(foaie_de_observatie='', nume='', prenume='', adresa='', varsta='', cnp='', nr_telefon='', motiv='',
          antecedente_heredo='', antecedente_personale='', alergii='', tratamente_urmate='', diagnostic_general='',
          diagnostic_stomatologic='', examene_complementare=''):
    conn = sqlite3.connect('cmi_cfl.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM cmi WHERE foaie_de_observatie=? OR nume=? OR prenume=? OR adresa=? OR varsta=? OR cnp=? '
                'OR nr_telefon=? OR motiv=? OR antecedente_heredo=? OR antecedente_personale=? OR alergii=? OR '
                'tratamente_urmate=? OR diagnostic_general=? OR diagnostic_stomatologic=? OR examene_complementare=?',
                (foaie_de_observatie, nume, prenume, adresa, varsta, cnp, nr_telefon, motiv, antecedente_heredo,
                 antecedente_personale, alergii, tratamente_urmate, diagnostic_general, diagnostic_stomatologic,
                 examene_complementare))
    rows = cur.fetchall()
    conn.close()
    return rows


def sterge(id):
    conn = sqlite3.connect('cmi_cfl.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM cmi WHERE id=?', (id,))
    conn.commit()
    conn.close()


def modifica(id, foaie_de_observatie, nume, prenume, adresa, varsta, cnp, nr_telefon, motiv, antecedente_heredo,
             antecedente_personale, alergii, tratamente_urmate, diagnostic_general, diagnostic_stomatologic,
             examene_complementare):
    conn = sqlite3.connect('cmi_cfl.db')
    cur = conn.cursor()
    cur.execute('UPDATE cmi SET foaie_de_observatie=?, nume=?, prenume=?, adresa=?, varsta=?, cnp=?, nr_telefon=?, '
                'motiv=?, antecedente_heredo=?, antecedente_personale=?, alergii=?, tratamente_urmate=?, '
                'diagnostic_general=?, diagnostic_stomatologic=?, examene_complementare=? WHERE id=?',
                (foaie_de_observatie, nume, prenume, adresa, varsta, cnp, nr_telefon, motiv, antecedente_heredo,
                 antecedente_personale, alergii, tratamente_urmate, diagnostic_general, diagnostic_stomatologic,
                 examene_complementare, id))
    conn.commit()
    conn.close()


connect()
