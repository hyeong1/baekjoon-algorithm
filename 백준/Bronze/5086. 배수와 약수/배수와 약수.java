import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int a = -1, b = -1;
        while (true) {
            String num = br.readLine();
            if (num == null) { break; }
            a = Integer.parseInt(num.split(" ")[0]);
            b = Integer.parseInt(num.split(" ")[1]);

            if (a == 0 && b == 0) { break; }
            if (a != 0 && b != 0) {
                if (a % b == 0) {
                    System.out.println("multiple");
                } else if (b % a == 0) {
                    System.out.println("factor");
                } else {
                    System.out.println("neither");
                }
            }   
        }
    }
}
