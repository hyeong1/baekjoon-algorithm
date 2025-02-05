
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] num1 = br.readLine().split(" ");
        String[] num2 = br.readLine().split(" ");
        int lcm = (Integer.parseInt(num1[1]) * Integer.parseInt(num2[1])) / gcd(Integer.parseInt(num1[1]), Integer.parseInt(num2[1]));
        int[] sum = new int[2];
        sum[0] = Integer.parseInt(num1[0]) * (lcm / Integer.parseInt(num1[1])) + Integer.parseInt(num2[0]) * (lcm / Integer.parseInt(num2[1]));
        sum[1] = lcm;

        int gcd = gcd(sum[0], sum[1]);
        if (gcd > 1) {
            sum[0] /= gcd;
            sum[1] /= gcd;
        }
        System.out.println(sum[0] + " " + sum[1]);
    }

    private static int gcd(int a, int b) {
        if (a % b == 0) {
            return b;
        }
        return gcd(b, a%b);
    }
}
