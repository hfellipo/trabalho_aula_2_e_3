''''
arq = open('teste2.txt','w')
print (arq)
arq.close()
print ('\nArquivo vazio criado com sucesso')
'''

'''

def gerar_numeros():
    arquivo = open('numeros.txt','w')
    for gerar in range(100):
        gerar += 1
        arquivo.write(str(gerar) + ';')
    arquivo.close()

gerar_numeros()

'''


def relatorio():
    nomes = []
    emails = []
    cursos = []

    while True:
        try:
            op = int(input('1 - cadastrar aluno\n'
                           '2 - listar alunos\n'
                           '3 - buscar um aluno pelo nome\n'
                           '4 - sair\n'
                           'Resposta:'))

            if op == 1:
                nome = input('Digite o nome do aluno: ')
                nomes.append(nome)
                email = input('Digite o e-mail do aluno: ')
                emails.append(email)
                curso = input('Digite o nome do curso: ')
                cursos.append(curso)
            elif op == 2:
                print("Lista de alunos:")
                for i in range(len(nomes)):
                    print(f"Nome: {nomes[i]}, E-mail: {emails[i]}, Curso: {cursos[i]}")
            elif op == 3:
                nome_busca = input("Digite o nome do aluno que deseja buscar: ")
                encontrado = False
                for i in range(len(nomes)):
                    if nomes[i] == nome_busca:
                        print(f"Aluno encontrado:\nNome: {nomes[i]}, E-mail: {emails[i]}, Curso: {cursos[i]}")
                        encontrado = True
                        break
                if not encontrado:
                    print("Aluno não encontrado.")
            elif op == 4:
                break
            else:
                print('Opção inválida')
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

    with open("alunos1.txt", "w") as arquivo:
        for i in range(len(nomes)):
            arquivo.write(f"Nome: {nomes[i]}, E-mail: {emails[i]}, Curso: {cursos[i]}\n")


relatorio()

































