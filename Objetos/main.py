from jogos import Jogos # importa a classe do arquivo jogos (arquivo da classe)

jogo_fifa = Jogos('ea fc', 'mobile')
descricao_fifa = ("EA FC É UM JOGO DE FUTEBOL" ,"Multiplayer")
jogo_fifa.alternar_estado()
jogo_fifa.adicionar_descricao_jogo(descricao_fifa)


def main():
    print(jogo_fifa)


if __name__ == '__main__':
      main()




