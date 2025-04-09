saldo = 1000
usuario = input("Digite seu nome: ")
usuario = usuario.capitalize()

extrato = []

while True:
    deposito = input(f"{usuario}, quanto deseja depositar? (ou digite 'sair'): R$ ")
    
    if deposito.lower() == "sair":
        break

    if deposito.replace('.', '', 1).isdigit():
        deposito = float(deposito)
        if deposito > 0:
            saldo += deposito
            extrato.append(deposito)
        else:
            print("Por favor, digite um valor positivo.")
    else:
        print("Entrada inválida. Tente novamente.")

print(f"\nDepósitos realizados por {usuario}:")
for valor in extrato:
    print(f"R$ {valor:.2f}")

print(f"\nSaldo final: R$ {saldo:.2f}")
