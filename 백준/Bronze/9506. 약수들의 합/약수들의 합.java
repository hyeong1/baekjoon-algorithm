import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        while (n != -1) {
            int sum = 0;
            String res = "";
            for (int i = 1; i < n; i++) {
                if (n % i == 0) {
                    sum += i;
                    res += String.valueOf(i) + " + ";
                    if (sum > n) {
                        break;
                    }
                }
            }
            if (sum == n) {
                System.out.println(n + " = " + res.substring(0, res.length() - 3));
            } else {
                System.out.println(n + " is NOT perfect.");
            }
            n = Integer.parseInt(br.readLine());
        }
    }
}
