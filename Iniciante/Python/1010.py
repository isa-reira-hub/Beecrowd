vendedor = input()
salario_fixo = float(input())
total_de_vendas = float(input())
total_receber = salario_fixo + 0.15 * total_de_vendas
print(f'TOTAL = R$ {total_receber:.2f}')
