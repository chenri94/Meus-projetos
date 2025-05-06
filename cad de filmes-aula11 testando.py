#Crie um programa para cadastrar filmes utilizando o conceito de vetores, matrizes e funções.

#banco de dados, lista:
#tem que ter ao menos dois dados, nome do filme e o ano,
#esse tipo é matriz, lista de listas.

import time

bd_filmes = [
    ['Interestelar', 2015, 'Ficção'],
    ['Titanic', 1997, 'Drama'],
    ['Star Wars: Episódio 6', 2022, 'Ficção']
    ['Conclave', 2024, 'Drama']
]
#criar função de listar filmes
#for para percorrer apenas as listas e não item por item
def listar_filmes(bd):
    for i in range(len(bd)):
        print(f'{i+1} - {bd[i][0]} - {bd[i][1]} - {bd[i][2]}')


#função de cadastrar filmes
#a bd do listar filmes é diferente da bd do cadastrar
#o return quer dizer que os dados cadastrados serão salvos, fora da função
def cadastrar_filme(bd, titulo, ano, categoria):
    filme = [titulo, ano, categoria]
    bd.append(filme)
    return bd


#função para alterar filmes
def alterar_filme(bd):
    try:
        for i in range(len(bd)):
            print(f'{i + 1} - {bd[i][0]} - {bd[i][1]} - {bd[i][2]}')
        escolha = int(input('Digite o número do filme que deseja alterar: '))

        if 1 <= escolha <= len(bd):
            n_titulo = input('Digite o novo título: ')
            n_ano = int(input('Digite o novo ano: '))
            n_categoria = input('Digite a nova categoria: ')

            # Atualiza os dados do filme selecionado
            bd[escolha - 1][0] = n_titulo
            bd[escolha - 1][1] = n_ano
            bd[escolha - 1][2] = n_categoria
        else:
            print('Número inválido.')
    except Exception as e:
        print(f'Erro ao alterar filme: {e}')


#agora vamos fazer o menu, será feito com recurso de loop 'while'.
#while vai ser usado em todo momento, não vai parar, por isso usa-se true.
while True:
    print('Bem-vindo ao CadFilme')
    print('1 - Cadastrar filme')
    print('2 - Alterar filme')
    print('3 - Listar filmes')
    print('0 - Sair')
#criar excepction para o programa não travar caso o usuário insira caracter que não seja número
    try:
        op = int(input('Digite a opção desejada: '))
    except Exception as e:
        print(f'Error: {e}')
        op = -1
    time.sleep(1)

    if op == 1:
        print(f'---- CADASTRO DE FILMES ----')
        titulo = input('Digite o título do novo filme: ')
        ano = int(input('Digite o ano do novo filme: '))
        categoria = input('Informe a categoria do filme: ')
        bd_filmes = cadastrar_filme(
            bd=bd_filmes,
            titulo=titulo,
            ano=ano,
            categoria=categoria
        )
        print(f'---- CADASTRO DE FILMES CONCLUÍDO ----')

    elif op == 2:
        print('---- ALTERAR FILME ----')
        alterar_filme(bd=bd_filmes)


        print('Filme alterado.')
    elif op ==3:
        print(f'---- LISTAGEM DE FILMES, INÍCIO ----')
        listar_filmes(bd=bd_filmes)
        print(f'---- LISTAGEM DE FILMES, FINAL ----')

    elif op==0:
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida! Tente novamente')
    time.sleep(2)