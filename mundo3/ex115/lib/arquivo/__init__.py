from lib.interface import cabecalho 

def arquivoExiste(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {arq} criado com sucesso.')


def lerarquivo(arq):
    try:
        a = open(arq,'rt')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado1 = dado[1].replace('\n','')
            print(f'{dado[0]:<30} {dado1:>3}')
            # print(f'{dado[0]:<30}{dado[1]:>3}')
    finally:
        a.close()


def cadastrar(arq,nome='desconhecido', idade=0):
    # cabecalho('Opção 2')
    try:
        a = open(arq,'at')
    except:
        print('Houve um ERRO na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Não foi possivel gravar no arquivo.')
        else:
            print(f'Novo cadastro de {nome} adicionado.')
            a.close()