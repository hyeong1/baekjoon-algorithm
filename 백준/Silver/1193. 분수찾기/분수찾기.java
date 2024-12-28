import java.util.*;

public class Main {
    public static void main(String[] args) {
        int X;
        Scanner sc = new Scanner(System.in);
        X = sc.nextInt();

        int digit = 0;
        int sum = 0;
        while (sum < X) {
            sum += digit++ + 1;
        }

        if (digit % 2 == 0) {
            System.out.print(digit - (sum-X));
            System.out.print("/");
            System.out.print(sum-X+1);
        } else {
            System.out.print(sum-X+1);
            System.out.print("/");
            System.out.print(digit - (sum-X));
        }
    }
}