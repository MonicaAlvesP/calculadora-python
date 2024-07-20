def soma(a, b):
      print(f"A soma de {a:.0f} + {b:.0f} é igual a {a + b:.0f}")

def subtracao(a, b):
      print(f"A subtração de {a:.0f} - {b:.0f} é igual a {a - b:.0f}")

def multiplicacao(a, b):
      print(f"A multiplicação de {a:.0f} * {b:.0f} é igual a {a * b:.0f}")

def divisao(a, b):
      if b != 0:
        print(f"A divisão de {a:.0f} / {b:.0f} é igual a {a / b:.0f}")
      else:
        print("\033[31mErro: Divisão por zero!\033[m")
    