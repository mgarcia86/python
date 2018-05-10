'''
6. Faça um Programa que pergunte quanto você ganha por hora e o número de
horas trabalhadas no mês. Calcule e mostre o total do seu salário no
referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário
bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o salário
líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule
os descontos e o salário líquido, conforme a tabela abaixo:

a. + Salário Bruto : R$
b. - IR (11%) : R$
c. - INSS (8%) : R$
d. - Sindicato ( 5%) : R$
e. = Salário Liquido : R$
'''

sal = float(input('valor salário por hora: R$ '))
hora = int(input('horas trabalhadas no mês: '))
bruto = sal * hora

ir = bruto * 0.11
inss = bruto * 0.08
sind = bruto * 0.05
desc = ir + inss + sind

liq = bruto - desc

print('\nIR \t\t\tR$ %.2f\nINSS \t\t\tR$ %.2f\nSindicado \t\tR$ %.2f' % (ir, inss, sind))
print('total de descontos \tR$ %.2f \nsalário líquido \tR$ %.2f' % (desc, liq))
