import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int m = Integer.parseInt(br.readLine());
        int n = Integer.parseInt(br.readLine());
        int sum = 0;
        int min = 0;
        for (int i = m; i <= n; i++) {
            for (int j = 1; j < i; j++) {
                if (j > 1 && i % j == 0) {
                    break;
                }
                if (j == i - 1) {
                    sum += i;
                    if (min == 0) {
                        min = i;
                    }
                }
            }
        }
        if (sum != 0) {
            System.out.println(sum);
            System.out.println(min);
        } else {
            System.out.print(-1);
        }
    }
}
