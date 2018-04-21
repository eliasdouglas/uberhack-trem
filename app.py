from flask import Flask, request


class App(Flask):
    """comentario"""

    def __init__(self, name):
        super(App, self).__init__(name)

        # Inicializa as rotas
        self.add_url_rule('/',
                          methods=['GET'],
                          view_func=self.__hello)

        self.add_url_rule('/trace-routes',
                          methods=['POST'],
                          view_func=self.__trace_routes)

    def __hello(self):
        """testa se o servidor está em execução"""
        return "Server is alive!"

    def __trace_routes(self):
        """traça rotas de acordo com a origem de destino passado por parâmetro"""
        routes = []

        # TODO obter rotas do google api
        # TODO obter rota da uber api

        return routes


if __name__ == "__main__":
    App(__name__).run('0.0.0.0', port=5000)
