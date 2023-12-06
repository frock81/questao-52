# Questão 52

Questão número 52 da disciplina de Matemática da prova de conhecimentos gerais para o cargo de Analista Legislativo ‒ Informática Legislativa do concurso da Câmara dos Deputados.

## Introdução

A Questão Propriamente Dita:

> 52
>
> Uma urna contém duas bolas brancas. Uma segunda urna contém
> uma bola branca e outra preta. Retira-se uma bola branca,
> desconhecendo-se de qual urna ela saiu. A seguir, as urnas são
> embaralhadas e uma segunda bola é retirada.
>
> A probabilidade de que a segunda bola seja preta é igual a
>
> (A) 3/8.
>
> (B) 2/3.
>
> (C) 1/6
>
> (D) 1/3.
> 
> (E) 1/4.

O gabarito preliminar da questão foi a letra "(A) 3/8". Como será demonstrado


## Espaço amostral

| bola-1             | bola-2             |
|--------------------|--------------------|
| branca_urna1_bola1 | branca_urna1_bola2 |
| branca_urna1_bola1 | branca_urna2_bola1 |
| branca_urna1_bola1 | preta              |
| branca_urna1_bola2 | branca_urna1_bola1 |
| branca_urna1_bola2 | branca_urna2_bola1 |
| branca_urna1_bola2 | preta              |
| branca_urna2_bola1 | branca_urna1_bola1 |
| branca_urna2_bola1 | branca_urna1_bola2 |
| branca_urna2_bola1 | preta              |

É fácil perceber que existem somente 9 possibilidades e que 3 delas correspondem a bolas pretas. Portanto a probabilidade é de 3/9, equivalente a 1/3.

## Resultados da Simulação

Cem mil (100.000) iterações foram suficientes para o script em Python convergir:

```
$ time python simulacao.py
Simulação com embaralhamento aleatório
Probabilidade de a segunda bola ser preta: 0.333032751021802
Tempo de execução: 7.2517607800109545 seconds

Simulação com embaralhamento redistribuído
Probabilidade de a segunda bola ser preta: 0.3335082994811873
Tempo de execução: 10.43669317101012 seconds

real    0m17,753s
user    0m17,719s
sys     0m0,034s
```

Percebe-se que o valor converge para 0.33, equivalente a 1/3.


## Sobre o Embaralhamento das Urnas

A etapa de "embaralhar as urnas" no problema apresentado pode ter múltiplas interpretações, dependendo de como se entende o ato de embaralhar no contexto.

Cada uma dessas interpretações leva a uma maneira diferente de abordar o problema e calcular as probabilidades resultantes. A escolha da interpretação correta dependeria do contexto específico ou de esclarecimentos adicionais na formulação do problema.

As seções a seguir abordam algumas possíveis interpretações.


### Aleatoriedade na Escolha da Urna

"Embaralhar as urnas" pode significar que a escolha da urna para a próxima retirada da bola é feita de forma completamente aleatória, sem qualquer viés ou padrão. Isso implicaria que não há como saber de qual urna a próxima bola será retirada, independentemente de qual urna foi usada anteriormente. Essa parece ser a interpretação mais razoável e será uma das consideradas nas simulações.


### Redistribuição (Permutação) das Bolas entre as Urnas

Uma interpretação mais complexa poderia ser a de que as bolas são redistribuídas entre as urnas de alguma forma antes da segunda retirada. No entanto, esta interpretação não altera as probabilidades envolvidas no problema, porquanto as urnas servem apenas como container. Essa interpretação será considerada e o resultado da simulação confirmará essa tese.


### Restauração das Condições Iniciais (Reposição)

Pode ser entendido que após a retirada da primeira bola, as urnas são reconfiguradas para seu estado inicial (por exemplo, se a primeira bola veio da Urna 2, uma nova bola branca é colocada de volta nela), garantindo que a segunda retirada seja feita sob as mesmas condições iniciais.

A questão não menciona reposição. A interpretação mais razoável é a de entender que não há reposição, pois se houvesse reposição o segundo evento seria independente do primeiro, não impactando a retirada da primeira bola ou qualquer embaralhamento.


### Troca Física das Posições das Urnas

Pode-se interpretar que as urnas são fisicamente movidas ou rearranjadas. Isso não altera o conteúdo das urnas, mas poderia afetar a escolha se a decisão de qual urna usar é baseada na posição física (por exemplo, sempre escolhendo a urna à esquerda). Isso não ocorre no enunciado do problema, portanto não deve ser considerado.


### Simbólico, Sem Efeito Prático

"Embaralhar as urnas" pode ser simplesmente uma frase para indicar uma pausa ou separação entre os eventos de retirada das bolas, sem ter um efeito prático ou literal no problema. Isso não altera as probabilidades.
