import os

from tkinter import messagebox
import mariadb as m

from database.queriesManager import QueriesManager as qm


# Clase que administrara la conexión a la base de datos.
class DataBaseManager:

    # Constructor
    def __init__(self):
        self._conn = None
        self._cursor = None
        self._status = False
        try:
            self._conn = m.Connection(
                user=os.environ.get("USER_DB"),
                password=os.environ.get("PASSWORD_DB"),
                host=os.environ.get("HOST_DB"),
                port=int(os.environ.get("PORT_DB")),
                database=os.environ.get("DATABASE_DB")
            )
            self._cursor = self._conn.cursor()
            self._status = True
        except m.OperationalError:
            messagebox.showerror("Error en la conexión a la DB",
                                 "Se produjo un Error al intentar conectarse a la base de datos")

    def getStatus(self):
        """
        Función que retorno el estado de nuestra coneccion

        :return: True o False dependiendo de si la conexión a la base de datos fue hecha.
        """
        return self._status

    def query(self, query: str, data: tuple) -> bool:
        """
        Función para ejecutar un solo Query

        :param query: Instrucción SQL
        :param data: Valores que tendrá la Instrucción SQL
        :return: True si se ejecuta adecuadamente
        """

        self._cursor.execute(query, data)
        self._conn.commit()
        return True

    def queries(self, data: dict) -> bool:
        """
        Función para ejecutar varias instrucciones SQL

        :param data: Dict con el formato { int :{'query':'…', 'values':'…'}}
        :return: True si se ejecutaron adecuadamente
        """

        for item in data.keys():
            try:
                self._cursor.execute(data[item]['query'], data[item]['values'])
            except m.IntegrityError:
                try:
                    values = ()
                    self._cursor.execute(os.environ.get("SELECT_QUERY"), (data[item]['values'][3], data[item]['values'][4]))
                    for response in self._cursor:
                        values = data[item]['values'] + response
                    self._cursor.execute(os.environ.get("UPDATE_QUERY"), values)
                except m.ProgrammingError:
                    messagebox.showerror("Error en la conexión a la DB",
                                         "Se produjo un Error al intentar guardar los datos.")
                    break
                except m.Error:
                    messagebox.showerror("Error en la conexión a la DB",
                                         "Se produjo un Error al intentar guardar los datos.")
                    break
            except m.Error:
                messagebox.showerror("Error en la conexión a la DB",
                                     "Se produjo un Error al intentar guardar los datos.")
                break
        self._conn.commit()
        messagebox.showinfo("información guardada", "La información se guardo satisfactoriamente en la base de datos.")
        return True

    def executeQueriesByDict(self, *args):
        """
        Función que ejecutar varias instrucciones SQL, al cual se le pasara como argumento otra variable
        para personalizar un poco más las instrucciones SQL

        :param args: Dict limpio con los datos recopilados de la API y str con el nombre del autor de los artículos
        :return: True si se ejecutaron adecuadamente
        """
        data = qm.createInfoForQueries(args[1], args[0])
        self.queries(data)
