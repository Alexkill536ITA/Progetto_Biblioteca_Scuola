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
        connection = sqlite3.connect("Database/libreria.db") #VS Code Debug
        # connection = sqlite3.connect("../Database/libreria.db") #Bin.exe fine
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
                sql_command = "INSERT INTO maestre(cognome,nome,password,amministratore) VALUES ('"+cognome+"','"+nome+"','"+password+"','"+amministratore+"')"
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
    if len(newpassword)>0 and len(newpassword)<=5:
        connection = Connect_db()
        crsr = connection.cursor()
        sql_command = "UPDATE db_admin, SET password = '"+ newpassword +"'"
        crsr.execute(sql_command)
        connection.commit()
        connection.close()
    else:
        return("Il valore inserito in PASSWORD non valido / Campo Vuoto")

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
            if type(password) == str and len(password)>0 and len(password)<=5:
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

def edit_book(titolo,autore,genere,foto,disponibilità,id_Book):
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
    if len(name_admin)>0 and type(name_admin) == str:
        if len(surname_Admin)>0 and type(surname_Admin) == str:
            connection = Connect_db()
            crsr = connection.cursor()
            sql_command = "DELETE FROM maestre WHERE nome='"+ name_admin +"' AND surname='"+surname_Admin+"'"
            crsr.execute(sql_command)
            connection.commit()
            connection.close()
        else:
            return("Il valore inserito in COGNOME non valido / Campo Vuoto")
    else:
        return("Il valore inserito in NOME non valido / Campo Vuoto")

#-----------------------------------------------------------------------------#
    
def delete_name_client(name_Client,surname_Client):
    if len(name_Client)>0 and type(name_Client) == str:
        if len(surname_Client)>0 and type(surname_Client) == str:
            connection = Connect_db()
            crsr = connection.cursor()
            sql_command = "DELETE FROM bambini WHERE nome='"+ name_Client +"' AND cognome='"+surname_Client+"'"
            crsr.execute(sql_command)
            connection.commit()
            connection.close()
        else:
            return("Il valore inserito in COGNOME non valido / Campo Vuoto")
    else:
        return("Il valore inserito in NOME non valido / Campo Vuoto")

#-----------------------------------------------------------------------------#

def delete_id_admin(id_Admin):
    if len(id_Admin)>0:
        connection = Connect_db()
        crsr = connection.cursor()
        sql_command = "DELETE FROM maestre WHERE  id='"+ id_Admin +"'"
        crsr.execute(sql_command)
        connection.commit()
        connection.close()
    else:
        return("Il valore inserito nel campo ID_Admin è Vuoto")

#-----------------------------------------------------------------------------#

def delete_id_client(id_Clinet):
    if len(id_Clinet)>0:
        connection = Connect_db()
        crsr = connection.cursor()
        sql_command = "DELETE FROM bambini WHERE  id='"+ id_Clinet +"'"
        crsr.execute(sql_command)
        connection.commit()
        connection.close()
    else:
        return("Il valore inserito nel campo ID_Client è Vuoto")

#-----------------------------------------------------------------------------#

def delete_title_book(title_Book):
    if len(title_Book)>0 and type(title_Book) == str:
        connection = Connect_db()
        crsr = connection.cursor()
        sql_command = "DELETE FROM libri WHERE titilo = '"+ title_Book +"'"
        crsr.execute(sql_command)
        connection.commit()
        connection.close()
    else:
        return("Il valore inserito in TITOLO non valido / Campo Vuoto")

#-----------------------------------------------------------------------------#

def delete_id_book(id_Book):
    if len(id_Book)>0:
        connection = Connect_db()
        crsr = connection.cursor()
        sql_command = "DELETE FROM libri WHERE id='"+ id_Book +"'"
        crsr.execute(sql_command)
        connection.commit()
        connection.close()
    else:
        return("Il valore inserito nel campo ID_Book è Vuoto")

#----------------------------------------END----------------------------------#

#-----------------------------------------------------------------------------#
#                     Eliminazione Prestiti NULL DataBase                     #
#-----------------------------------------------------------------------------#

def delete_log_null(id_Client):
    if len(id_Client)>0:
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
    else:
        return("Il valore inserito in COGNOME non valido / Campo Vuoto")

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
    sql_command = "SELECT id,cognome,nome,amministatore FROM maestre"
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

#-----------------------------------------------------------------------------#

def show_libri_inpossesso(id_bambino):
    connection = Connect_db()
    crsr = connection.cursor()
    sql_command = "SELECT * FROM PRESTITI WHERE codice_bambino=?"
    result = crsr.execute(sql_command,(id_bambino))
    return result

#-----------------------------------------------------------------------------#

def show_book_by_ID(id_book):
    connection = Connect_db()
    crsr = connection.cursor()
    sql_command = "SELECT titolo,foto FROM libri WEHRE id='"+id_book+"'"
    result = crsr.execute(sql_command)
    return result

#-----------------------------------------------------------------------------#

def show_book_by_ID_all(id_book):
    connection = Connect_db()
    crsr = connection.cursor()
    sql_command = "SELECT * FROM libri WEHRE id='"+id_book+"'"
    result = crsr.execute(sql_command)
    return result

#-----------------------------------------------------------------------------#

def show_book_Disponibili():
    connection = Connect_db()
    crsr = connection.cursor()
    sql_command = "SELECT * FROM LIBRI WHERE disponibile=1"
    result = crsr.execute(sql_command)
    return result

#-----------------------------------------------------------------------------#

#----------------------------------FILTRO-------------------------------------#

# def query_cast(db_name,camp_filter,key_serch):
#     connection = Connect_db()
#     crsr = connection.cursor()
#     sql_command = "SELECT * FROM "+ db_name +" WHERE " + camp_filter + " LIKE '"+ key_serch +"%' NOT IN(name = 'password,question,resonse,avatar,copertina')"
#     result = crsr.execute(sql_command)
#     return result

#-----------------------------------------------------------------------------#

def filter_ID_book(id_Book):
    if len(id_Book)>0 and type(id_Book)==str:
        connection = Connect_db()
        crsr = connection.cursor()
        sql_command = "SELECT * FROM libri WHERE id='"+ id_Book +"'"
        result = crsr.execute(sql_command)
        return result
    else:
        return("Il valore inserito in TITOLO non valido / Campo Vuoto")

#-----------------------------------------------------------------------------#

def filter_book(titolo):
    if len(titolo)>0 and type(titolo)==str:
        connection = Connect_db()
        crsr = connection.cursor()
        sql_command = "SELECT * FROM libri WHERE titolo='"+ titolo +"'"
        result = crsr.execute(sql_command)
        return result
    else:
        return("Il valore inserito in TITOLO non valido / Campo Vuoto")

#-----------------------------------------------------------------------------#

def filter_to_autore_book(autore):
    if len(autore)>0 and type(autore)==str:
        connection = Connect_db()
        crsr = connection.cursor()
        sql_command = "SELECT * FROM libri WHERE autore='"+ autore +"'"
        result = crsr.execute(sql_command)
        return result
    else:
        return("Il valore inserito in AUTORE non valido / Campo Vuoto")

#-----------------------------------------------------------------------------#

def filter_ID_to_Client(id_Client):
    if len(id_Client)>0 and type(id_Client)==str:
        connection = Connect_db()
        crsr = connection.cursor()
        sql_command = "SELECT * FROM bambini WHERE id ='"+id_Client+"'"
        result = crsr.execute(sql_command)
        return result
    else:
        return("Il valore inserito in ID non valido / Campo Vuoto")

#-----------------------------------------------------------------------------#

def filter_name_to_Client(name_Client):
    if len(name_Client)>0 and type(name_Client)==str:
        connection = Connect_db()
        crsr = connection.cursor()
        sql_command = "SELECT * FROM bambini WHERE nome ='"+name_Client+"'"
        result = crsr.execute(sql_command)
        return result
    else:
        return("Il valore inserito in NOME non valido / Campo Vuoto")

#-----------------------------------------------------------------------------#

def filter_cognome_to_Client(cognome_Client):
    if len(cognome_Client)>0 and type(cognome_Client)==str:
        connection = Connect_db()
        crsr = connection.cursor()
        sql_command = "SELECT * FROM bambini WHERE cognome ='"+cognome_Client+"'"
        result = crsr.execute(sql_command)
        return result
    else:
        return("Il valore inserito in Cognome non valido / Campo Vuoto")

#-----------------------------------------------------------------------------#

def filter_classe_to_Client(classe_Client):
    if len(classe_Client)>0 and type(classe_Client)==str:
        connection = Connect_db()
        crsr = connection.cursor()
        sql_command = "SELECT * FROM bambini WHERE classe ='"+classe_Client+"'"
        result = crsr.execute(sql_command)
        return result
    else:
        return("Il valore inserito in Classe non valido / Campo Vuoto")

#-----------------------------------------------------------------------------#

def filter_id_to_maestre(id_Admin):
    if len(id_Admin)>0 and type(id_Admin)==str:
        connection = Connect_db()
        crsr = connection.cursor()
        sql_command = "SELECT * FROM maestre WHERE id ='"+id_Admin+"'"
        result = crsr.execute(sql_command)
        return result
    else:
        return("Il valore inserito in ID non valido / Campo Vuoto")

#-----------------------------------------------------------------------------#

def filter_name_to_maestre(name_Admin):
    if len(name_Admin)>0 and type(name_Admin)==str:
        connection = Connect_db()
        crsr = connection.cursor()
        sql_command = "SELECT * FROM maestre WHERE nome ='"+name_Admin+"'"
        result = crsr.execute(sql_command)
        return result
    else:
        return("Il valore inserito in NOME non valido / Campo Vuoto")

#-----------------------------------------------------------------------------#

def filter_cognome_to_maestre(cognome_Admin):
    if len(cognome_Admin)>0 and type(cognome_Admin)==str:
        connection = Connect_db()
        crsr = connection.cursor()
        sql_command = "SELECT * FROM maestre WHERE cognome ='"+cognome_Admin+"'"
        result = crsr.execute(sql_command)
        return result
    else:
        return("Il valore inserito in Cognome non valido / Campo Vuoto")

#-----------------------------------------------------------------------------#

def filter_Login_Client(name_Client,surname_Client):
    if len(name_Client)>0 and type(name_Client)==str:
        if len(surname_Client)>0 and type(surname_Client)==str:
            connection = Connect_db()
            crsr = connection.cursor()
            sql_command = "SELECT * FROM bambini WHERE nome='"+name_Client+"' AND cognome='"+surname_Client+"'"
            result = crsr.execute(sql_command)
            return result
        else:
            return("Il valore inserito in COGNOME non valido / Campo Vuoto")
    else:
        return("Il valore inserito in NOME non valido / Campo Vuoto")

#-----------------------------------------------------------------------------#

def filter_Login_maestre(name_Admin,password_Admin):
    if len(name_Admin)>0 and type(name_Admin)==str:
        if len(password_Admin)>0:
            connection = Connect_db()
            crsr = connection.cursor()
            sql_command = "SELECT * FROM maestre WHERE nome=? AND password=?;"
            crsr.execute(sql_command,(name_Admin,password_Admin))
            result = crsr.execute(sql_command,(name_Admin,password_Admin))
            return result
        else:
            return("Il valore inserito in PASSWORD non valido / Campo Vuoto")
    else:
        return("Il valore inserito in NOME non valido / Campo Vuoto")

#------------------------------------END--------------------------------------#

#-----------------------------------------------------------------------------#
#                       Pretito e Restituzione DataBase                       #
#-----------------------------------------------------------------------------#

def add_logs_book(id_Client,id_Book):
    if len(id_Client)>0:
        if len(id_Book)>0:
            connection = Connect_db()
            crsr = connection.cursor()
            sql_command = "INSERT INTO prestiti(codice_bambino,codice_libro,data_prestito) VALUES("+ id_Client +","+ id_Book +","+ time.strftime("%d/%m/%Y") +")"
            crsr.execute(sql_command)
            connection.commit()

            sql_command = "UPDATE libri SET disponibilità = 0 WHERE id='"+id_Book+"'"
            crsr.execute(sql_command)
            connection.commit()
            connection.close()
        else:
            return("Il valore inserito in ID_Bimbo non valido / Campo Vuoto")
    else:
        return("Il valore inserito in ID_Libro non valido / Campo Vuoto")

#-----------------------------------------------------------------------------#

def romve_logs_book(id_Log,id_Book):
    if len(id_Log)>0:
        if len(id_Book):
            connection = Connect_db()
            crsr = connection.cursor()
            sql_command = "UPDATE prestiti SET data_restituzione = '"+ time.strftime("%d/%m/%Y") +"' WHERE id='"+id_Log+"'"
            crsr.execute(sql_command)
            connection.commit()

            sql_command = "UPDATE db_libri SET disponibilità = 1 WHERE id='"+id_Book+"'"
            crsr.execute(sql_command)
            connection.commit()
            connection.close()
        else:
            return("Il valore inserito in ID_Libro non valido / Campo Vuoto")
    else:
        return("Il valore inserito in ID_Prestito non valido / Campo Vuoto")

#----------------------------------------END----------------------------------#