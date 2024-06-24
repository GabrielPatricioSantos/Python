from avaliacao import Avaliacao

class Jogos:

    jogos = []

    def __init__(this,nome,categoria): # __init__ = construtor
       this._nome = nome.title() # .title() = mantém a primeira letra maiúsucula
       this._categoria = categoria.upper() # .upper () = coloca todas as letras maiúsuclas
       this._ativo = False # _.atributo = torna o atributo privado
       this._avaliacao = [] 
       this._descricao = []
       Jogos.jogos.append(this)

    def __str__(this): # a função especial __str__ lista em forma de texto os atributos do objeto
        return f'{this._nome} | {this._categoria}'
    
    @classmethod #permite que o método seja usado sem instanciar a classe inteira
    def listarJogos(cls):
        print(f'{'Nome do jogo: '.ljust(25)} | {'Categoria do Jogo: '.ljust(25)} |{'Nota: '.ljust(25)} | {'Status: '}')
        for jogo in cls.jogos:  #Jogos = classe / jogos = array
            print(f'{jogo._nome.ljust(25)} | {jogo._categoria.ljust(25)} |{jogo.media_avaliacoes} | {jogo.ativo}')

    @property # pega um atributo (no caso, ativo) e modifica a leitura de um atributo
    # Nesse caso, ao invés de retornar TRUE ou FALSE no parâmetro 'ativo', retornará o resultado da função
    def ativo(this): 
        return '✔️' if this._ativo else '❌' 
    
    def alternar_estado(this):
        this._ativo = not this._ativo # not - inverte o valor atribuido ( true - false / false - true)
    
    def receber_avaliacao (this, cliente, nota):
        avaliacao = Avaliacao(cliente,nota) 
        this._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes (this):
        if not this._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in this._avaliacao)# sum = soma
        quantidade_de_notas = len(this._avaliacao) # len =  atribui o nº de atributos na lista
        #round = arredondamento
        media = round(soma_das_notas / quantidade_de_notas , 1) # , 1 = nº de casas decimais
        return media
    
    def adicionar_descricao_jogo(this, descricao):
        this._descricao.append(descricao)
        
    




