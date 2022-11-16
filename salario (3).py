
import time

hrs=float(input('Quantos voce ganha por hora ?'))
hrspordia=float(input('Quantas horas trabalhado por mês ?'))

salarioSemHrsExtras = hrs * hrspordia
print(f'salario sem hrs extras: {salarioSemHrsExtras:,.2f}')


hrsExtras = float(input('Quantas horas extras fez por mês sem adicional noturno ?'))

comHrsExtras = hrsExtras + (hrsExtras*25/100)
salarioComHrsExtras = salarioSemHrsExtras + (hrs * comHrsExtras)
print(f'salario bruto com horas extras: {salarioComHrsExtras:,.2f}')

adicionalNoturno = input('teve adicional noturno sim/nao: ')
if adicionalNoturno == 'sim' and 'Sim':
    hrsExtrasAdicionalNoturno = float(input('Quantas hrs adicional noturno fez por mes ?'))
    ComAdicionalNoturno =  hrsExtrasAdicionalNoturno + (hrsExtrasAdicionalNoturno*25/100)
    salarioComAdicionalNoturno = ComAdicionalNoturno + (ComAdicionalNoturno * hrs)
    salarioComAdicionalNoturno = salarioComAdicionalNoturno + salarioComHrsExtras
    print(f'Salario bruto com adicional noturno: {salarioComAdicionalNoturno:,.2f}')
else:
    print('fim')
time.sleep(10)