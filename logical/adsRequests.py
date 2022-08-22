import requests
import json
from tkinter import messagebox


class ADS:

    # Constructor
    def __init__(self):
        self._token = "TnEWAPDi8n5R3taijqXleJDTZ5LNDr2LMJjOOsec"
        self._endpoint = "https://api.adsabs.harvard.edu/v1/search/query?q={key}&rows=200&fl=author,title,pub,bibcode,doi,volume,year,page_range,links_data&sort=date desc"
        # TODO: Cambiar datos al desplegar

    def getDataByKey(self, key: str, cache) -> bool:
        """
        Función que realiza la petición al ENDPOINT , y que muestra y guarda la información en la interfaz de search.

        :param key: Llave de la búsqueda
        :param cache: Interfaz con la propiedad .data donde almacenara la información recopilada como un dict limpio
        :return: Retorna True si se realizó la tarea satisfactoriamente, de lo contrario retorna un False
        """
        try:
            response = requests.get(self._endpoint.format(key=key), headers={'Authorization': 'Bearer ' + self._token})
            cache.reloadTextArea(self._getStrAllArticles(response.json()))
            cache.data = self._getCleanDictWithAllArticles(response.json())
        except Exception:
            messagebox.showerror("Error conexión API",
                                 "Se produjo un error al realizar o al procesar la petición a la API")
        return True

    def getStrData(self, key: str) -> str:
        """
        Función que realiza una petición al ENDPOINT y que regresa la información limpia para el usuario final


        :param key: Llave de la búsqueda
        :return: Un str con la información recopilada limpia
        """
        response = requests.get(self._endpoint.format(key=key), headers={'Authorization': 'Bearer ' + self._token})
        data = self._getStrAllArticles(response.json())
        return data

    def getDictData(self, key: str) -> dict:
        """
        Función para realizar una petición al ENDPOINT y que regresa un dict con la información limpia

        :param key: Llave de la búsqueda
        :return: Retorna un dict con la información recopilada limpia
        """

        response = requests.get(self._endpoint.format(key=key), headers={'Authorization': 'Bearer ' + self._token})
        data = self._getCleanDictWithAllArticles(response.json())
        return data

    @staticmethod
    def _getCleanDataByArticle(data: dict) -> dict:
        """
        Función que regresa un dict con la información de un artículo

        :param data: Un dict con la información del artículo en sucio
        :return: Un dict con la información del artículo en limpio
        """
        keys = data.keys()
        return {
            'authors': "".join(map(str, data['author'])),
            'title': data['title'][0],
            'pub': data['pub'],
            'url': "url",
            'bibcode': data['bibcode'],
            'doi': data['doi'][0],
            'page_range': data['page_range'] if 'page_range' in keys else "Undefined",
            'volume': data['volume'],
            'year': data['year'],
        }

    def _getStrAllArticles(self, data: dict) -> str:
        """
        Función para obtener un str con la información de los artículos.

        :param data: Un dict con la información obtenida de la petición al ENDPOINT.
        :return: Un str con la información de los artículos.
        """
        result = ""
        for element in data['response']['docs']:

            url_list = ""
            authors_list = ""
            dic_data = self._getCleanDataByArticle(element)
            if 'links_data' in element.keys():
                for elem in element["links_data"]:
                    res = json.loads(elem)
                    if res["type"] == "pdf":
                        url_list += "\n    • Academic pdf: {pdf}".format(pdf=res["url"])
                    if res["type"] == "electr":
                        url_list += "\n    • Online: {online}".format(online=res["url"])
                url_list += "\n    • ADS: https://ui.adsabs.harvard.edu/abs/{bibcode}/abstract".format(
                    bibcode=dic_data['bibcode'])
            else:
                url_list = "No hay URLs"

            for elem in element['author']:
                authors_list += "\n    • {author}".format(author=elem)

            item = ' • Authores: {authors}\n • Título del artículo: {title}\n • Revista: {pub}\n • URL: {url}\n' \
                   ' • BIBCODE: {bibcode}\n • DOI: {doi}\n • Páginas: {page_range}\n • Volumen: {volume}\n' \
                   ' • Año: {year}\n'.format(
                authors=authors_list,
                title=dic_data['title'],
                pub=dic_data['pub'],
                url=url_list,
                bibcode=dic_data['bibcode'],
                doi=dic_data['doi'],
                page_range=dic_data['page_range'],
                volume=dic_data['volume'],
                year=dic_data['year'],
            )
            result += item + "\n\n"

        return result

    def _getCleanDictWithAllArticles(self, data: dict) -> dict:
        """
        Función que realiza una petición al ENDPOINT y que regresa la información limpia para el usuario final

        :param data: Un dict con la información obtenida de la petición al ENDPOINT.
        :return: Un dict con la información de todos los artículos en limpio
        """
        dict_data = {}
        count = 0
        for element in data['response']['docs']:
            element_data = self._getCleanDataByArticle(element)
            dict_data[count] = element_data
            count += 1
        return dict_data
