import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String read = br.readLine();
        int n = Integer.parseInt(read.split(" ")[0]);
        int k = Integer.parseInt(read.split(" ")[1]);
        int seq = 0;
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                seq++;
            }
            if (seq == k) {
                System.out.println(i);
                break;
            }
        }
        if (seq < k) System.out.println(0);
    }
}