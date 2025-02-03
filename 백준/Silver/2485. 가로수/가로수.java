
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] trees = new int[n];

        for (int i = 0; i < n; i++) {
            trees[i] = Integer.parseInt(br.readLine());
        }

        int minGap = trees[1] - trees[0];
        for (int i = 2; i < n; i++) {
            minGap = gcd(minGap, trees[i] - trees[i-1]);
        }

        int total = ((trees[n-1] - trees[0]) / minGap) + 1;
        System.out.println(total - n);
    }

    private static int gcd(int a, int b) {
        while (b != 0) {
            int tmp = a % b;
            a = b;
            b = tmp;
        }
        return a;
    }
}
