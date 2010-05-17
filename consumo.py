#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

## pega o valor da kilometragem inicial do carro
km_inicial = float(raw_input("Digite a kilometragem inicial: "))

## pega o valor da kilometragem final do carro
km_final = float(raw_input("Digite a kilometragem Final: "))

## pega o valor do combustível
valor = float(raw_input("Digite o valor do combustível: "))

## pega a quantidade em litros de combustível
litros = float(raw_input("Digite a quantidade de litros: "))

# calcula a kilometragem rodada
km_rodados = km_final - km_inicial

# valor pago pelo combustível
valor_pago = valor * litros

#calcula o consumo do carro
consumo = km_rodados / litros

print("Informações:")
print("Quilometragem inicial: {0} km\nQuilometragem final: {1} km".format(km_inicial, km_final))
print("Valor do combustível: R$ {0}\nLitros de combustível: {1} l".format(valor, litros))

print("Resultados:")
print('Valor do Combustível: R$', valor_pago)
print('O carro rodou: ', km_rodados, 'km')
print('O carro está fazendo: ', consumo, 'Km/lt')
