import tkinter as tk

from elements.customButton import CustomButton
from elements.customEntry import CustomEntry
from elements.customLabel import CustomLabel
from elements.customTextArea import CustomTextArea
from elements.windowsText import WindowsText
from elements.customEntryMessage import EntryMessage

from logical.adsRequests import ADS
from logical.files import FilesManager as fm

from database.databaseManager import DataBaseManager
from database.queriesManager import QueriesManager as qm


class Search(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self._master = master
        self.buscadorEntry = None
        self.buscarButton = None
        self.buscarLabel = None
        self.textArea = None
        self.area = None
        self.botonCSV = None
        self.botonQueries = None
        self.data = {}
        self.obtenerTexto = None
        self.botonSave = None
        self.ads = ADS()
        self.config(
            bg="#fff"
        )
        self.loadWidgets()
        self.responsive()
        self.connection = None

    def loadWidgets(self):
        self.buscarLabel = CustomLabel(self, "Buscar:")
        self.buscarLabel.grid(row=1, column=1, sticky="nsew")
        self.buscarLabel.config(font=("Arial", 16))

        self.buscadorEntry = CustomEntry(self)
        self.buscadorEntry.grid(row=1, column=2, columnspan=6, sticky="nsew", padx=10)
        self.buscadorEntry.config(font=("Arial", 14))

        self.buscarButton = CustomButton(self, "Buscar",
                                         lambda: self.ads.getDataByKey(self.buscadorEntry.get(), self))
        self.buscarButton.grid(row=1, column=8, sticky="nsew")

        self.area = tk.Frame(self)
        self.area.grid(row=3, rowspan=14, column=1, columnspan=8, sticky="nsew")

        self.textArea = CustomTextArea(self.area)

        self.botonCSV = CustomButton(self, "Guardar txt", command=lambda: fm.saveDictAsCsvFile(
            self.textArea.getText()))  # TODO: cambiar command
        self.botonCSV.grid(row=18, column=1, padx=5, sticky="nsew")

        self.botonQueries = CustomButton(self, "Ver Queries", command=self.showQueries)
        self.botonQueries.grid(row=18, column=2, padx=5, sticky="nsew")

        self.botonSave = CustomButton(self, "Limpiar", command=lambda: self.reloadTextArea(""))
        self.botonSave.grid(row=18, column=7, padx=5, sticky="nsew")

        self.botonSave = CustomButton(self, "Guardar", command=self.saveDataInDataBase)
        self.botonSave.grid(row=18, column=8, padx=5, sticky="nsew")

    def responsive(self):
        row = 20
        columns = 10
        for i in range(row):
            self.rowconfigure(i, weight=1)
        for i in range(columns):
            self.columnconfigure(i, weight=10)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

    def reloadTextArea(self, txt):
        self.textArea.deleteText()
        self.textArea.setText(txt)

    def showQueries(self):
        WindowsText(
            "Estos Queries Son una Previsualización, puede que contengan algún tipo de error\n\n" +
            qm.createPreSqlQueries(self.data, "User"), "Queries")

    def saveDataInDataBase(self):
        self.connection = DataBaseManager()
        if self.connection.getStatus():
            EntryMessage("Ingrese el Author", "Digite el Author", self.connection.executeQueriesByDict, self.data)
