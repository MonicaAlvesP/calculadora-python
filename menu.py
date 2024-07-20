import calculadora

print("\033[35mBem-vindo à calculadora que calcula!!\033[m")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
opcao = 0

while opcao != 5:
  print(' ' * 10)
  print("""
  \033[32mEscolha uma das opções abaixo:
  [1] Somar
  [2] Subtrair
  [3] Multiplicar
  [4] Dividir
  [5] Sair do programa \033[m""")
  print(' ' * 10)
  opcao = int(input("\033[33m>>>>Digite a opção desejada: \033[m"))
  print(' ' * 10)

  match opcao:
    case 1:
      calculadora.soma(num1, num2)
    case 2:
      calculadora.subtracao(num1, num2)
    case 3:
      calculadora.multiplicacao(num1, num2)
    case 4:
      calculadora.divisao(num1, num2)
    case 5:
      print("Saindo do programa...")
    case _:
      print("Opção inválida! Tente novamente.")
  
  print(' ' * 10)
  continuar = input("Deseja continuar? (s/n): ")
  print(' ' * 10)
  if continuar.lower() != 's':
    break
  
  mesma_operacao = input("Deseja escolher novos numeros? (s/n): ")
  print(' ' * 10)
  if mesma_operacao.lower() != 's':
    continue
  else:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print(' ' * 10)
    continue

print("\033[35mPrograma encerrado.\033[m")
