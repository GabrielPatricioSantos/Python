from jogos import Jogos

class DescricaoJogo(Jogos): # torna a classe DescricaoJogo uma classe "filha" da classe principal (Jogos)
    def __init__(this, nome, descricao, modo):
        super().__init__(nome) # super().__init__ -> inicializa os atributos indicados da classe Pai
        this._descricao = descricao
        this._modo = modo
