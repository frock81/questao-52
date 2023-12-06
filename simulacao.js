const NUMERO_ITERACOES = 100000;

class Cor {
    static BRANCA = 0;
    static PRETA = 1;
}

class Bola {
    constructor(cor) {
        this.cor = cor;
    }
}

class Urna {
    constructor(bolas) {
        this.bolas = bolas;
    }

    retirarBola() {
        if (this.bolas.length > 0) {
            const index = Math.floor(Math.random() * this.bolas.length);
            return this.bolas.splice(index, 1)[0];
        }
        return null;
    }

    inserirBola(bola) {
        this.bolas.push(bola);
    }

    isEmpty() {
        return this.bolas.length === 0;
    }
}

class Contador {
    constructor() {
        this.total = 0;
        this.totalPretas = 0;
    }

    incrementarTotal() {
        this.total++;
    }

    getTotal() {
        return this.total;
    }

    incrementarTotalPretas() {
        this.totalPretas++;
    }

    getTotalPretas() {
        return this.totalPretas;
    }
}

function criarBola(cor) {
    return new Bola(cor);
}

function criarUrna(bolas) {
    return new Urna(bolas);
}

function criarBolaPreta() {
    return criarBola(Cor.PRETA);
}

function criarBolaBranca() {
    return criarBola(Cor.BRANCA);
}

function escolherUrnaAleatoria(urnas) {
    const index = Math.floor(Math.random() * urnas.length);
    return urnas[index];
}

function criarContador() {
    return new Contador();
}

function criarUrna1e2() {
    const urna1BolaBranca1 = criarBolaBranca();
    const urna1BolaBranca2 = criarBolaBranca();
    const urna2BolaBranca = criarBolaBranca();
    const urna2BolaPreta = criarBolaPreta();

    const bolasUrna1 = [urna1BolaBranca1, urna1BolaBranca2];
    const bolasUrna2 = [urna2BolaBranca, urna2BolaPreta];

    const urna1 = criarUrna(bolasUrna1);
    const urna2 = criarUrna(bolasUrna2);

    return [urna1, urna2];
}

function filtrarUrnaSemBolas(urnas) {
    return urnas.filter(urna => !urna.isEmpty());
}

function escolherUrnaAleatoriaComBola(urnas) {
    const urnasComBolas = filtrarUrnaSemBolas(urnas);
    return escolherUrnaAleatoria(urnasComBolas);
}

function simularRetiradaBola(urnas) {
    const urnaEscolhida = escolherUrnaAleatoriaComBola(urnas);
    const bolaEscolhida = urnaEscolhida.retirarBola();
    return [bolaEscolhida, urnaEscolhida];
}

function embaralhamentoAleatorio(urnas) {
    urnas.sort(() => Math.random() - 0.5);
    return urnas;
}

function embaralhamentoRedistribuido(urnas) {
    let bolas = [];
    urnas.forEach(urna => {
        let bola;
        while ((bola = urna.retirarBola()) !== null) {
            bolas.push(bola);
        }
    });

    bolas.sort(() => Math.random() - 0.5);

    bolas.forEach(bola => {
        const urna = escolherUrnaAleatoria(urnas);
        urna.inserirBola(bola);
    });

    return urnas;
}

function simularEventos(contador, funcaoEmbaralhamento, reposicao = false) {
    const urnas = criarUrna1e2();
    const [primeiraBolaRetirada, primeiraUrnaEscolhida] = simularRetiradaBola(urnas);
    if (primeiraBolaRetirada.cor === Cor.PRETA) {
        return;
    }

    if (reposicao) {
        primeiraUrnaEscolhida.inserirBola(primeiraBolaRetirada);
    }

    const urnasEmbaralhadas = funcaoEmbaralhamento(urnas);
    const [segundaBolaRetirada, _] = simularRetiradaBola(urnasEmbaralhadas);
    contador.incrementarTotal();

    if (segundaBolaRetirada.cor === Cor.PRETA) {
        contador.incrementarTotalPretas();
    }
}

function simular(numeroIteracoes, funcaoEmbaralhamento, reposicao = false) {
    const startTime = Date.now();
    const contador = criarContador();

    for (let i = 0; i < numeroIteracoes; i++) {
        simularEventos(contador, funcaoEmbaralhamento, reposicao);
    }

    console.log(`Probabilidade de a segunda bola ser preta: ${contador.getTotalPretas() / contador.getTotal()}`);
    const endTime = Date.now();
    console.log(`Tempo de execução: ${(endTime - startTime) / 1000} seconds`);
}

console.log("Simulação com embaralhamento aleatório sem reposição");
simular(NUMERO_ITERACOES, embaralhamentoAleatorio);

console.log("\nSimulação com embaralhamento redistribuído sem reposição");
simular(NUMERO_ITERACOES, embaralhamentoRedistribuido);

console.log("\nSimulação com embaralhamento aleatório com reposição");
simular(NUMERO_ITERACOES, embaralhamentoAleatorio, true);

console.log("\nSimulação com embaralhamento redistribuído com reposição");
simular(NUMERO_ITERACOES, embaralhamentoRedistribuido, true);
