###############################################################################
#                                                                             #
#                           Modulo Connesione DataBase                        #
#                           Crato da Alizzi Alessandro                        #
#                           Copyright By Bjarka Energy®                       #
#                                                                             #
###############################################################################

import os
import threading
import time
import shutil
import sqlite3
from sqlite3 import Error

#-----------------------------------------------------------------------------#
#                       Connesione e Verifica del DataBase                    #
#-----------------------------------------------------------------------------#

stat = ""

def Connect_db():
    global stat
    try:
        print(os.getcwd())
        # connection = sqlite3.connect("Database/libreria.db") #VS Code Debug
        connection = sqlite3.connect("../Database/libreria.db") #Bin.exe fine
    except Error as e:
        print(e)
    stat = connection
    return connection

def close_db():
    stat.close()

def backup_db():
    i = 0
    active = True
    path_Root = os.getcwd()
    path_Original = path_Root+"..\\Database\\libreria.db"
    shutil.copy(path_Original, path_Root+'..\\Database_backup\\libreria.db')
    path_Backup = path_Root+"..\\Database_backup\\libreria.db"
 
    if os.path.exists(path_Root+"..\\Database_backup\\libreria.db"):
        if(time.strftime("%d")== "01"):
            shutil.copy(path_Backup, path_Root+'..\\Database_backup_month\\libreria.db')
        else:
            if(os.path.exists(path_Root+"..\\Database_backup\\libreria.db.8")== False):
                while active:
                    if(os.path.exists(path_Root+"..\\Database_backup\\libreria.db."+str(i))== False):
                        shutil.copy(path_Original,path_Root+"..\\Database_backup\\libreria.db."+str(i))
                        break
                    else:
                        i=i+1
            else:
                os.remove(path_Root+"\\Database_backup\\libreria.db.0")
                shutil.copy(path_Original,path_Root+"\\Database_backup\\libreria.db."+str(0))

def Ripristino(Selezione):
    path_Root = os.getcwd()
    if os.path.exists(Selezione):
         shutil.copy(Selezione,path_Root+"..\\Database\\libreria.db")
         return "Ripristino completato"
    else:
        return "Errore File non esiste"

#-----------------------------------------------------------------------------#

# Importare sul Main File

# import threading
# import time

# thread = threading.Thread(target = backup_db)
# thread.start()

#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#
#                          Inserimento dati nel DataBase                      #
#-----------------------------------------------------------------------------#

def insert_book(Titolo,Autore,Genere,cover):
    if type(Titolo) == str and len(Titolo)>0:
        if type(Autore) == str and len(Autore)>0:
            if type(Genere) == str and len(Genere)>0:
                if type(cover) == str and len(cover)>0:
                    connection = Connect_db()
                    crsr = connection.cursor()
                    sql_command = "INSERT INTO libri(titolo,autore,genere,foto,disponibilià) VALUES ("+ Titolo +", "+ Autore + ", "+ Genere +", "+ cover +",1)"
                    crsr.execute(sql_command)
                    connection.commit()
                    connection.close()
                else :
                    return("Il valore inserito in FOTO non valido / Campo Vuoto")
            else :
                return("Il valore inserito in GENERE non valido / Campo Vuoto")
        else :
            return("Il valore inserito in AUTORE non valido / Campo Vuoto")
    else :
        return("Il valore inserito in TITOLO non valido / Campo Vuoto")

#-----------------------------------------------------------------------------#

def insert_admin(nome,cognome,password,amministratore):
    if type(nome) == str and len(nome)>0:
        if type(cognome) == str and len(cognome)>0:
            if type(password) == str and len(password)>0:
                connection = Connect_db()
                crsr = connection.cursor()
                sql_command = "INSERT INTO maestre(nome,cognome,password,amministratore) VALUES ('"+nome+"','"+cognome+"','"+password+"','"+amministratore+"')"
                crsr.execute(sql_command)
                connection.commit()
                connection.close()
            else :
                return("Il valore inserito in PASSWORD non valido / Campo Vuoto")
        else :
            return("Il valore inserito in COGNOME non valido / Campo Vuoto")
    else:
        return("Il valore inserito in NOME non valido / Campo Vuoto")

#-----------------------------------------------------------------------------#

def insert_client(cognome,nome,classe,anni,foto):
    if type(nome) == str and len(nome)>0:
        if type(cognome) == str and len(cognome)>0:
            if type(classe) == str and len(classe)>0:
                if type(anni) == str and len(anni)>0:
                    connection = Connect_db()
                    crsr = connection.cursor()
                    sql_command = "INSERT INTO bambini (cognome,nome,classe,anni,foto) VALUES ('"+cognome+"','"+nome+"','"+classe+"',"+anni+","+foto+")"
                    crsr.execute(sql_command)
                    connection.commit()
                    connection.close()
                else :
                    return("Il valore inserito in ANNI non valido / Campo Vuoto")
            else :
                return("Il valore inserito in CLASSE non valido / Campo Vuoto")
        else :
            return("Il valore inserito in COGNOME non valido / Campo Vuoto")
    else :
        return("Il valore inserito in NOME non valido / Campo Vuoto")

#----------------------------------------END----------------------------------#

#-----------------------------------------------------------------------------#
#                           Modifica dati nel DataBase                        #
#-----------------------------------------------------------------------------#

def rest_admin(newpassword):
    connection = Connect_db()
    crsr = connection.cursor()
    sql_command = "UPDATE db_admin, SET password = '"+ newpassword +"'"
    crsr.execute(sql_command)
    connection.commit()
    connection.close()

#-----------------------------------------------------------------------------#

def edit_client(cognome,nome,classe,anni,foto,id_Client):
    if type(nome) == str and len(nome)>0:
        if type(cognome) == str and len(cognome)>0:
            if type(classe) == str and len(classe)>0:
                if type(anni) == str and len(anni)>0:
                    connection = Connect_db()
                    crsr = connection.cursor()
                    sql_command = "UPDATE bambini SET cognome='"+cognome+"', nome='"+nome+"', classe='"+classe+"', anni='"+anni+"', foto='"+foto+"' WHERE id='"+id_Client+"'"
                    crsr.execute(sql_command)
                    connection.commit()
                    connection.close()
                else :
                    return("Il valore inserito in ANNI non valido / Campo Vuoto")
            else :
                return("Il valore inserito in CLASSE non valido / Campo Vuoto")
        else :
            return("Il valore inserito in COGNOME non valido / Campo Vuoto")
    else :
        return("Il valore inserito in NOME non valido / Campo Vuoto")

#-----------------------------------------------------------------------------#

def edit_admin(nome,cognome,password,amministratore,id_Admin):
    if type(nome) == str and len(nome)>0:
        if type(cognome) == str and len(cognome)>0:
            if type(password) == str and len(password)>0:
                connection = Connect_db()
                crsr = connection.cursor()
                sql_command = "UPDATE bambini SET nome='"+nome+"', cognome='"+cognome+"', password='"+password+"', amministratore='"+amministratore+"' WHERE id='"+id_Admin+"'"
                crsr.execute(sql_command)
                connection.commit()
                connection.close()
            else :
                return("Il valore inserito in PASSWORD non valido / Campo Vuoto")
        else :
            return("Il valore inserito in COGNOME non valido / Campo Vuoto")
    else:
        return("Il valore inserito in NOME non valido / Campo Vuoto")

#-----------------------------------------------------------------------------#

def edit_admin(titolo,autore,genere,foto,disponibilità,id_Book):
    if type(titolo) == str and len(titolo)>0:
        if type(autore) == str and len(autore)>0:
            if type(genere) == str and len(genere)>0:
                connection = Connect_db()
                crsr = connection.cursor()
                sql_command = "UPDATE libri SET titolo='"+titolo+"', autore='"+autore+"', genere='"+genere+"', foto='"+foto+"', disponibilità='"+disponibilità+"' WHERE id='"+id_Book+"'"
                crsr.execute(sql_command)
                connection.commit()
                connection.close()
            else :
                return("Il valore inserito in GENERE non valido / Campo Vuoto")
        else :
            return("Il valore inserito in AUTORE non valido / Campo Vuoto")
    else:
        return("Il valore inserito in TITOLO non valido / Campo Vuoto")

#----------------------------------------END----------------------------------#

#-----------------------------------------------------------------------------#
#                          Eliminazione dati nel DataBase                     #
#-----------------------------------------------------------------------------#

def delete_name_admin(name_admin,surname_Admin):
    connection = Connect_db()
    crsr = connection.cursor()
    sql_command = "DELETE FROM maestre WHERE nome='"+ name_admin +"' AND surname='"+surname_Admin+"'"
    crsr.execute(sql_command)
    connection.commit()
    connection.close()

#-----------------------------------------------------------------------------#
    
def delete_name_client(name_Client,surname_Client):
    connection = Connect_db()
    crsr = connection.cursor()
    sql_command = "DELETE FROM bambini WHERE nome='"+ name_Client +"' AND cognome='"+surname_Client+"'"
    crsr.execute(sql_command)
    connection.commit()
    connection.close()

#-----------------------------------------------------------------------------#

def delete_id_admin(id_Admin):
    connection = Connect_db()
    crsr = connection.cursor()
    sql_command = "DELETE FROM maestre WHERE  id='"+ id_Admin +"'"
    crsr.execute(sql_command)
    connection.commit()
    connection.close()

#-----------------------------------------------------------------------------#

def delete_id_client(id_Clinet):
    connection = Connect_db()
    crsr = connection.cursor()
    sql_command = "DELETE FROM bambini WHERE  id='"+ id_Clinet +"'"
    crsr.execute(sql_command)
    connection.commit()
    connection.close()

#-----------------------------------------------------------------------------#

def delete_title_book(title_Book):
    connection = Connect_db()
    crsr = connection.cursor()
    sql_command = "DELETE FROM libri WHERE titilo = '"+ title_Book +"'"
    crsr.execute(sql_command)
    connection.commit()
    connection.close()

#-----------------------------------------------------------------------------#

def delete_id_book(id_Book):
    connection = Connect_db()
    crsr = connection.cursor()
    sql_command = "DELETE FROM libri WHERE id='"+ id_Book +"'"
    crsr.execute(sql_command)
    connection.commit()
    connection.close()

#----------------------------------------END----------------------------------#

#-----------------------------------------------------------------------------#
#                     Eliminazione Prestiti NULL DataBase                     #
#-----------------------------------------------------------------------------#

def delete_log_null(id_Client):
    connection = Connect_db()
    crsr = connection.cursor()
    sql_command = "SELECT count*(codice_bambino) FROM prestiti WHERE id_bambino='"+id_Client+"'	AND data_restituzione=null"
    crsr.execute(sql_command)
    if len(crsr.fetchall())>0:
        sql_command = "DELETE FROM prestiti WHERE codice_bambino ='"+id_Client+"'"
        crsr.execute(sql_command)
        sql_command = "DELETE FROM bambini WHERE id='"+id_Client+"'"
        crsr.execute(sql_command)
        connection.commit()
    else:
        return("Non sono presenti PRESTITI")

#----------------------------------------END----------------------------------#

#-----------------------------------------------------------------------------#
#                   Visualizatore tabelle e filtro DataBase                   #
#-----------------------------------------------------------------------------#

def show_table():
    connection = Connect_db()
    crsr = connection.cursor()
    sql_command = "SELECT name FROM sqlite_master where type= 'table' NOT IN(name = 'sqlite_sequence')"
    result = crsr.execute(sql_command)
    return result

#-----------------------------------------------------------------------------#

def show_admin():
    connection = Connect_db()
    crsr = connection.cursor()
    #sql_command = "SELECT * FROM db_admin" #Tutti i campi
    sql_command = "SELECT * FROM maestre"
    result = crsr.execute(sql_command)
    return result

#-----------------------------------------------------------------------------#

def show_client():
    connection = Connect_db()
    crsr = connection.cursor()
    sql_command = "SELECT * FROM bambini"
    result = crsr.execute(sql_command)
    return result

#-----------------------------------------------------------------------------#

def show_book():
    connection = Connect_db()
    crsr = connection.cursor()
    sql_command = "SELECT * FROM libri"
    result = crsr.execute(sql_command)
    return result

#-----------------------------------------------------------------------------#

def show_type():
    connection = Connect_db()
    crsr = connection.cursor()
    sql_command = "SELECT * FROM generi"
    result = crsr.execute(sql_command)
    return result

#-----------------------------------------------------------------------------#

def show_logs_book():
    connection = Connect_db()
    crsr = connection.cursor()
    sql_command = "SELECT * FROM prestiti"
    result = crsr.execute(sql_command)
    return result

#----------------------------------FILTRO-------------------------------------#

# def query_cast(db_name,camp_filter,key_serch):
#     connection = Connect_db()
#     crsr = connection.cursor()
#     sql_command = "SELECT * FROM "+ db_name +" WHERE " + camp_filter + " LIKE '"+ key_serch +"%' NOT IN(name = 'password,question,resonse,avatar,copertina')"
#     result = crsr.execute(sql_command)
#     return result

#-----------------------------------------------------------------------------#

def filter_book(titolo):
    connection = Connect_db()
    crsr = connection.cursor()
    sql_command = "SELECT id,titolo,autore,disponibilità,datainsterimento libri FROM libri WHERE titolo='"+ titolo +"'"
    result = crsr.execute(sql_command)
    return result

#-----------------------------------------------------------------------------#

def filter_name_to_Client(name_Client):
    connection = Connect_db()
    crsr = connection.cursor()
    sql_command = "SELECT id,nome,cognome,classe,foto FROM bambini WHERE id ='"+name_Client+"'"
    result = crsr.execute(sql_command)
    return result

#-----------------------------------------------------------------------------#

def filter_name_to_maestre(name_Admin):
    connection = Connect_db()
    crsr = connection.cursor()
    sql_command = "SELECT id,nome,cognome,foto FROM maestre WHERE id='"+name_Admin+"'"
    result = crsr.execute(sql_command)
    return result

#-----------------------------------------------------------------------------#

def filter_Login_Client(name_Client,surname_Client):
    connection = Connect_db()
    crsr = connection.cursor()
    sql_command = "SELECT * FROM bambini WHERE nome='"+name_Client+"' AND cognome='"+surname_Client+"'"
    result = crsr.execute(sql_command)
    return result

#-----------------------------------------------------------------------------#

def filter_Login_maestre(name_Admin,password_Admin):
    connection = Connect_db()
    crsr = connection.cursor()
    sql_command = "SELECT * FROM maestre WHERE nome='"+name_Admin+"' AND password='"+password_Admin+"'"
    result = crsr.execute(sql_command)
    return result

#------------------------------------END--------------------------------------#

#-----------------------------------------------------------------------------#
#                       Pretito e Restituzione DataBase                       #
#-----------------------------------------------------------------------------#

def add_logs_book(id_bimbo,id_libro):
    connection = Connect_db()
    crsr = connection.cursor()
    sql_command = "INSERT INTO prestiti(codice_bambino,codice_libro,data_prestito) VALUES("+ id_bimbo +","+ id_libro +","+ time.strftime("%d/%m/%Y") +")"
    crsr.execute(sql_command)
    connection.commit()

    sql_command = "UPDATE libri SET disponibilità = 0 WHERE id='"+id_libro+"'"
    crsr.execute(sql_command)
    connection.commit()
    connection.close()

#-----------------------------------------------------------------------------#

def romve_logs_book(id_Log,id_Book):
    connection = Connect_db()
    crsr = connection.cursor()
    sql_command = "UPDATE prestiti SET data_restituzione = '"+ time.strftime("%d/%m/%Y") +"' WHERE id='"+id_Log+"'"
    crsr.execute(sql_command)
    connection.commit()

    sql_command = "UPDATE db_libri SET disponibilità = 1 WHERE id='"+id_Book+"'"
    crsr.execute(sql_command)
    connection.commit()
    connection.close()    

#----------------------------------------END----------------------------------#