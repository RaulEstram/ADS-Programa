import os


class QueriesManager:

    @staticmethod
    def createPreSqlQueries(data: dict, author: str) -> str:
        """

        :param data:
        :param author:
        :return:
        """

        queries = ""
        for item in data.keys():
            articule = data[item]
            try:
                fpage = articule['page_range'].split("-")[0] if articule['page_range'] != "Undefined" else None
                lpage = articule['page_range'].split("-")[1] if articule['page_range'] != "Undefined" else None
            except IndexError:
                fpage = articule['page_range'] if articule['page_range'] != "Undefined" else None
                lpage = articule['page_range'] if articule['page_range'] != "Undefined" else None

            query = os.environ.get("INSERT_QUERY_SHOW").format(
                autor=author,
                title=articule['title'],
                pub=articule['pub'],
                bibcode=articule['bibcode'],
                doi=articule['doi'],
                fpage=fpage,
                lpage=lpage,
                volume=articule['volume'],
                year=articule['year']
            )
            queries += query + "\n"
        return queries

    # Crear la informacion de los queries
    @staticmethod
    def createInfoForQueries(data: dict, author: str) -> dict:
        queries = {}
        for item in range(len(data)):

            articule = data[item]

            try:
                fpage = articule['page_range'].split("-")[0] if articule['page_range'] != "Undefined" else None
                lpage = articule['page_range'].split("-")[1] if articule['page_range'] != "Undefined" else None
            except IndexError:
                fpage = articule['page_range'] if articule['page_range'] != "Undefined" else None
                lpage = articule['page_range'] if articule['page_range'] != "Undefined" else None

            query = os.environ.get("INSERT_QUERY")
            values = (
                author,
                articule['title'],
                articule['pub'],
                articule['bibcode'],
                articule['doi'],
                fpage,
                lpage,
                articule['volume'],
                articule['year'],
            )
            queries[item] = {
                "query": query,
                "values": values
            }
        return queries
