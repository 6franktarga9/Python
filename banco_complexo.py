def criar_usuario():
    lista_usuarios = []
    while True:
        print('Criar usuário? 1 - Sim | 2 - Não')
        op = int(input("Opção: "))
        if op == 1:
            usuario = dict()
            usuario['nome'] = input('Nome: ')
            usuario['email'] = input('Email: ')
            usuario['senha'] = input('Senha: ')
            usuario['conta'] = None  # Inicializa sem conta
            lista_usuarios.append(usuario)
        elif op == 2:
            break
        else:
            print("Opção inválida!")
    return lista_usuarios

def criar_conta(lista_usuarios):
    while True:
        print('Criar conta? 1 - Sim | 2 - Não')
        op = int(input("Opção: "))
        if op == 1:
            login = input("Email: ")
            senha = input("Senha: ")
            for usuario in lista_usuarios:
                if usuario['email'] == login and usuario['senha'] == senha:
                    if usuario["conta"] is None:
                        usuario['conta'] = {
                            'saldo': 800,
                            'debito': 0,
                            'historico': []
                        }
                        print("Conta criada com sucesso!")
                    else:
                        print("Usuário já possui conta.")
                    break
            else:
                print("Login ou senha incorretos!")
        elif op == 2:
            break
        else:
            print("Opção inválida!")

def operacoes_conta(lista_usuarios):
    while True:
        login = input("Email: ")
        senha = input("Senha: ")
        for usuario in lista_usuarios:
            if usuario['email'] == login and usuario['senha'] == senha:
                if usuario['conta'] is None:
                    print("Usuário ainda não possui conta!")
                    return
                while True:
                    print('\n1 - Depósito | 2 - Saque | 3 - Extrato | 4 - Sair')
                    op = int(input("Opção: "))
                    if op == 1:
                        deposito = float(input("Valor do depósito R$: "))
                        usuario['conta']['saldo'] += deposito
                        usuario['conta']['historico'].append(f"Depósito de R$ {deposito:.2f}")
                    elif op == 2:
                        saque = float(input("Valor do saque R$: "))
                        if saque > usuario['conta']['saldo']:
                            print("Saldo insuficiente!")
                        else:
                            usuario['conta']['saldo'] -= saque
                            usuario['conta']['historico'].append(f"Saque de R$ {saque:.2f}")
                    elif op == 3:
                        print(f"\nSaldo atual: R$ {usuario['conta']['saldo']:.2f}")
                        print("Histórico de transações:")
                        for i, transacao in enumerate(usuario['conta']['historico']):
                            print(f"{i} - {transacao}")
                    elif op == 4:
                        return
                    else:
                        print("Opção inválida!")
                break
        else:
            print("Login ou senha incorretos!")

def main():
    while True:
        print('\n1 - Criar usuário | 2 - Criar conta | 3 - Operações da conta | 4 - Sair')
        op = int(input("Opção: "))
        if op == 1:
            lista_usuarios = criar_usuario()
        elif op == 2:
            criar_conta(lista_usuarios)
        elif op == 3:
            operacoes_conta(lista_usuarios)
        elif op == 4:
            break
        else:
            print("Opção inválida!")

main()