
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Stack<String> stack = new Stack<>();
        for (int i = 0; i < n; i++) {
            String x = br.readLine();
            if (x.split(" ")[0].equals("1")) {
                stack.push(x.split(" ")[1]);
            } else if (x.equals("2")) {
                System.out.println(stack.isEmpty() ? -1 : stack.pop());
            } else if (x.equals("3")) {
                System.out.println(stack.size());
            } else if (x.equals("4")) {
                System.out.println(stack.isEmpty() ? 1 : 0);
            } else if (x.equals("5")) {
                System.out.println(stack.isEmpty() ? -1 : stack.peek());
            }
        }
    }
}
