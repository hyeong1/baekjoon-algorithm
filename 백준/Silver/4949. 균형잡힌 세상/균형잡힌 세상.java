import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Stack<Character> stack = new Stack<>();
        String n = br.readLine();
        while (!n.equals(".")) {
            String[] nn = n.split(" ");
            for (int i = 0; i < nn.length; i++) {
                for (int j = 0; j < nn[i].length(); j++) {
                    if (nn[i].charAt(j) == '(' || nn[i].charAt(j) == '[') {
                        stack.push(nn[i].charAt(j));
                    } else if (nn[i].charAt(j) == ')') {
                        if (!stack.isEmpty() && stack.peek() == '(') {
                            stack.pop();
                        } else if (stack.isEmpty() || stack.peek() == '[') {
                            stack.push(nn[i].charAt(j));
                        }
                    } else if (nn[i].charAt(j) == ']') {
                        if (!stack.isEmpty() && stack.peek() == '[') {
                            stack.pop();
                        } else if (stack.isEmpty() || stack.peek() == '(') {
                            stack.push(nn[i].charAt(j));
                        }
                    }
                }
            }
            if (stack.isEmpty()) {
                System.out.println("yes");
            } else {
                System.out.println("no");
            }
            stack.clear();
            n = br.readLine();
        }

    }
}
