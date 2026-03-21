class Curso():
    def __init__(self, CO_CURSO: int, NOME: str):
        self.__CO_CURSO = CO_CURSO
        self.__NOME = NOME

#: ID do curso
    @property
    def get_id(self):
        return self.__CO_CURSO
    

#: Nome do curso:
    @property
    def NOME(self):
        return self.__NOME

    @NOME.setter
    def NOME(self, new_NOME: str):
        self.__NOME = new_NOME.strip()