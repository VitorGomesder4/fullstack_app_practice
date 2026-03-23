import datetime

class ALUNO():
    def __init__(
        self, co_aluno: int, dt_nascimento: datetime, sg_sexo: str, nome: str, 
        co_estadocivil: str, no_pai: str, no_mae: str):

        self.dt_nascimento = dt_nascimento #datetime
        self.sg_sexo = sg_sexo #size_limit of 1 char
        self.nome = nome #size_limit of 20 char
        self.co_estadocivil = co_estadocivil #size_limit of 1 char
        self.no_pai = no_pai #size_limit of 70 char
        self.no_mae = no_mae #size_limit of 70 char