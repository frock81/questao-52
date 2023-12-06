import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public class Simulacao {

    enum Cor {
        BRANCA, PRETA
    }

    static class Bola {
        Cor cor;

        public Bola(Cor cor) {
            this.cor = cor;
        }
    }

    static class Urna {
        List<Bola> bolas;

        public Urna(List<Bola> bolas) {
            this.bolas = bolas;
        }

        public Bola retirarBola() {
            if (!bolas.isEmpty()) {
                return bolas.remove(new Random().nextInt(bolas.size()));
            }
            return null;
        }

        public void inserirBola(Bola bola) {
            bolas.add(bola);
        }

        public boolean isEmpty() {
            return bolas.isEmpty();
        }
    }

    static class Contador {
        int total = 0;
        int totalPretas = 0;

        public void incrementarTotal() {
            total++;
        }

        public int getTotal() {
            return total;
        }

        public void incrementarTotalPretas() {
            totalPretas++;
        }

        public int getTotalPretas() {
            return totalPretas;
        }
    }

    public static void main(String[] args) {
        final int NUMERO_ITERACOES = 100000;
        long startTime = System.currentTimeMillis();

        Contador contador = new Contador();
        for (int i = 0; i < NUMERO_ITERACOES; i++) {
            simularEvento(contador);
        }

        double probabilidade = (double) contador.getTotalPretas() / contador.getTotal();
        System.out.println("Probabilidade de a segunda bola ser preta: " + probabilidade);

        long endTime = System.currentTimeMillis();
        System.out.println("Tempo de execução: " + (endTime - startTime) / 1000.0 + " seconds");
    }

    public static List<Urna> criarUrna1e2() {
        List<Bola> bolasUrna1 = new ArrayList<>();
        bolasUrna1.add(new Bola(Cor.BRANCA));
        bolasUrna1.add(new Bola(Cor.BRANCA));

        List<Bola> bolasUrna2 = new ArrayList<>();
        bolasUrna2.add(new Bola(Cor.BRANCA));
        bolasUrna2.add(new Bola(Cor.PRETA));

        List<Urna> urnas = new ArrayList<>();
        urnas.add(new Urna(bolasUrna1));
        urnas.add(new Urna(bolasUrna2));

        return urnas;
    }

    public static void simularEvento(Contador contador) {
        List<Urna> urnas = criarUrna1e2();
        Bola primeiraBola = retirarBolaAleatoria(urnas);

        if (primeiraBola != null && primeiraBola.cor == Cor.BRANCA) {
            embaralharUrna(urnas);
            Bola segundaBola = retirarBolaAleatoria(urnas);

            contador.incrementarTotal();
            if (segundaBola != null && segundaBola.cor == Cor.PRETA) {
                contador.incrementarTotalPretas();
            }
        }
    }

    public static Bola retirarBolaAleatoria(List<Urna> urnas) {
        Urna urnaEscolhida = urnas.get(new Random().nextInt(urnas.size()));
        return urnaEscolhida.retirarBola();
    }

    public static void embaralharUrna(List<Urna> urnas) {
        Collections.shuffle(urnas);
    }
}
