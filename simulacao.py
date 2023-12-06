#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random, time
from enum import Enum
from typing import Optional, List, Callable

NUMERO_ITERACOES = 100_000

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

    def inserir_bola(self, bola: Bola) -> None:
        self.bolas.append(bola)

    def is_empty(self) -> bool:
        return len(self.bolas) == 0

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


def filtrar_urnas_sem_bolas(urnas: List[Urna]) -> List[Urna]:
    return list(filter(lambda urna: not urna.is_empty(), urnas))


def escolher_urna_aleatoria_com_bola(urnas: List[Urna]) -> Urna:
    urnas_com_bolas = filtrar_urnas_sem_bolas(urnas)
    urna_escolhida = escolher_urna_aleatoria(urnas)
    return urna_escolhida


def simular_retirada_bola(urnas: List[Urna]) -> Bola:
    # A depender do método de embaralhamento, pode ser que
    # uma urna não tenha bolas. Portanto, é necessário
    # garantir que a urna escolhida tenha bolas.
    urna_escolhida = escolher_urna_aleatoria_com_bola(urnas)
    return urna_escolhida.retirar_bola()


def embaralhamento_aleatorio(urnas: List[Urna]) -> List[Urna]:
    random.shuffle(urnas)
    return urnas


def embaralhamento_redistribuido(urnas: List[Urna]) -> List[Urna]:
    bolas = []
    for urna in urnas:
        bola = urna.retirar_bola()
        while(bola is not None):
            bolas.append(bola)
            bola = urna.retirar_bola()
    random.shuffle(bolas)
    for bola in bolas:
        urna = random.choice(urnas)
        urna.inserir_bola(bola)
    return urnas


def embaralhar_urnas(
    urnas: List[Urna],
    funcao_embaralhamento) -> List[Urna]:
    return funcao_embaralhamento(urnas)


def simular_eventos(contador: Contador, funcao_embaralhamento) -> None:
    urnas = criar_urnas()
    primeira_bola_retirada = simular_retirada_bola(urnas)
    # A primeira bola retirada é branca conforme enunciado.
    # Portanto, dado que a primeira bola é branca, se a bola
    # retirada for preta, ela não deve ser considerada, pois
    # não faz parte do nosso espaço amostral.
    if primeira_bola_retirada.cor == Cor.PRETA:
        return
    # O próximo passo do evento é embaralhar as urnas, o qual
    # pode ter diferentes interpretações.
    urnas: List[Urna] = embaralhar_urnas(urnas, funcao_embaralhamento)
    segunda_bola_retirada = simular_retirada_bola(urnas)
    if segunda_bola_retirada is not None:
        # Incrementa o contador
        contador.incrementar_total()
        # Verifica se a bola retirada é preta
        if segunda_bola_retirada.cor == Cor.PRETA:
            contador.incrementar_total_pretas()

def simular(numero_iteracoes: int,
            funcao_embaralhamento: Callable[[List[Urna]], Urna]) -> None:
    start_time = time.perf_counter()
    contador = criar_contador()
    for _ in range(numero_iteracoes):
        simular_eventos(contador, funcao_embaralhamento)
    print(f"Probabilidade de a segunda bola ser preta: {contador.get_total_pretas() / contador.get_total()}")
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"Tempo de execução: {total_time} seconds")


if __name__ == "__main__":
    print("Simulação com embaralhamento aleatório")
    simular(numero_iteracoes=NUMERO_ITERACOES,
            funcao_embaralhamento=embaralhamento_aleatorio)
    print("\nSimulação com embaralhamento redistribuído")
    simular(numero_iteracoes=NUMERO_ITERACOES,
            funcao_embaralhamento=embaralhamento_redistribuido)
