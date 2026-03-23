class Curso():
    def __init__(self, co_curso: int, nome: str):
        self.__co_curso = co_curso
        self.__nome = nome

#: ID do curso
    @property
    def get_id(self):
        return self.__co_curso
    

#: Nome do curso:
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, new_NOME: str):
        self.__nome = new_nome.strip()