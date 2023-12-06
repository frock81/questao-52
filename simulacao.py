#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import sys
from enum import Enum
from typing import Optional, List

class Cor(Enum):
    BRANCA = 0
    PRETA = 1

class Bola:
    def __init__(self, cor):
        self.cor: Cor = cor

class Urna:
    def __init__(self, bolas: List[Bola]):
        self.bolas: List[Bola] = bolas

    def retirar_bola(self) -> Optional[Bola]:
        if len(self.bolas) > 0:
            bola = random.choice(self.bolas)
            self.bolas.remove(bola)
            return bola
        return None

class Contador:
    def __init__(self):
        self.total = 0
        self.total_pretas = 0

    def incrementar_total(self):
        self.total += 1

    def get_total(self):
        return self.total

    def incrementar_total_pretas(self):
        self.total_pretas += 1

    def get_total_pretas(self):
        return self.total_pretas

def criar_bola(cor: Cor) -> Bola:
    return Bola(cor)

def criar_urna(bolas) -> Urna:
    return Urna(bolas)

def criar_bola_preta() -> Bola:
    return criar_bola(Cor.PRETA)

def criar_bola_branca() -> Bola:
    return criar_bola(Cor.BRANCA)

def escolher_urna_aleatoria(urnas: List[Urna]) -> Urna:
    return random.choice(urnas)

def criar_contador() -> Contador:
    return Contador()

def criar_urnas() -> List[Urna]:
    # Criação das bolas
    urna1_bola_branca1 = criar_bola_branca()
    urna1_bola_branca2 = criar_bola_branca()
    urna2_bola_branca = criar_bola_branca()
    urna2_bola_preta = criar_bola_preta()
    # Separar as bolas
    bolas_urna1 = [urna1_bola_branca1, urna1_bola_branca2]
    bolas_urna2 = [urna2_bola_branca, urna2_bola_preta]
    # Cria a urna um com duas bolas brancas
    urna1 = criar_urna(bolas_urna1)
    # Cria a urna dois com uma bola branca e uma preta
    urna2 = criar_urna(bolas_urna2)
    return [urna1, urna2]

def simular_evento1(urnas: List[Urna]) -> Bola:
    # Escolhe aleatoriamente uma urna
    primeira_urna_escolhida = escolher_urna_aleatoria(urnas)
    # Retira uma bola da urna escolhida
    return primeira_urna_escolhida.retirar_bola()

def embaralhar_urnas(urnas: List[Urna]) -> List[Urna]:
    # Não é claro o que isso quer dizer, mas pode ser implementado
    # de diversas formas:
    #   1. Uma escolha aleatória das urnas
    # Entretanto, perceba que isso independe no nosso evento,
    # visto que as urnas funcionam apenas como um container.
    # Embaralha as urnas
    return escolher_urna_aleatoria(random.shuffle(urnas))

def simular_evento2(urnas: List[Urna]) -> Bola:
    # O próximo passo do evento é embaralhar as urnas.
    segunda_urna_escolhida = escolher_urna_aleatoria(urnas)
    # Retira uma bola da urna escolhida
    return segunda_urna_escolhida.retirar_bola()

def simular_eventos(contador: Contador) -> None:
    urnas = criar_urnas()
    primeira_bola_retirada = simular_evento1(urnas)
    # A primeira bola retirada é branca, conforme enunciado.
    # Portanto, dado que a primeira bola é branca, se a bola
    # retirada for preta, ela não deve ser considerada.
    if primeira_bola_retirada.cor == Cor.PRETA:
        return
    segunda_bola_retirada = simular_evento2(urnas)
    # Incrementa o contador
    contador.incrementar_total()
    # Verifica se a bola retirada é preta
    if segunda_bola_retirada.cor == Cor.PRETA:
        contador.incrementar_total_pretas()

def simular(numero_iteracoes: int) -> None:
    contador = criar_contador()
    for _ in range(numero_iteracoes):
        simular_eventos(contador)
    print(f"Probabilidade de a segunda bola ser preta: {contador.get_total_pretas() / contador.get_total()}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Por favor, forneça o número de iterações como um argumento.")
        sys.exit(1)
    try:
        num_iterations = int(sys.argv[1])
        simular(num_iterations)
    except ValueError:
        print("Por favor, forneça um número inteiro válido para o número de iterações.")
        sys.exit(1)
