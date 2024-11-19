import java.util.Scanner;

public class Main {
    public static boolean[] sitoEratostenesa(int n) {
        boolean[] pierwsze = new boolean[n + 1];
        for (int i = 0; i <= n; i++) {
            pierwsze[i] = true;
        }
        pierwsze[0] = false;
        pierwsze[1] = false;

        for (int i = 2; i*i <= n+1; i++) {
            if (pierwsze[i]) {
                for (int j = i * i; j <= n; j += i) {
                    pierwsze[j] = false;
                }
            }
        }

        return pierwsze;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Podaj n: ");
        int n = scanner.nextInt();

        // Wywołanie funkcji sitoEratostenesa i wypisanie wyniku
        System.out.println("Liczby pierwsze z przedziału <2, " + n + ">:");
        boolean[] tablica = sitoEratostenesa(n);

        for (int i = 2; i <= n; i++) {
            if (tablica[i]) {
                System.out.println(i);
            }
        }
    }
}
