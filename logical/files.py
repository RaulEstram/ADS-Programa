from tkinter.filedialog import asksaveasfile


class FilesManager:

    @staticmethod
    def saveDictAsCsvFile(data: str) -> bool:
        """
        Función para Guardar en un archivo txt un str mediante un explorador de archivos

        :param data: El str que se guarda en el archivo txt
        :return: Retorna True si se guardo correctamente de lo contrario regresa un False
        """
        try:
            with asksaveasfile(mode="wb", title="Guardar archivo",
                               filetypes=(("Guardar como txt", ".txt"), ("ALL FILES", ".*")),
                               defaultextension=".txt") as file:
                file.write(bytes(data, "utf-8"))
                file.close()
            return True
        except AttributeError:
            pass
        except KeyError:
            pass
        return False
