
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Deque<String> queue = new LinkedList<>();
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            String nn = br.readLine();
            switch (nn.split(" ")[0]) {
                case "1":
                    queue.offerFirst(nn.split(" ")[1]);
                    break;
                case "2":
                    queue.offer(nn.split(" ")[1]);
                    break;
                case "3":
                    if (!queue.isEmpty()) {
                        System.out.println(queue.pollFirst());
                    } else {
                        System.out.println(-1);
                    }
                    break;
                case "4":
                    if (!queue.isEmpty()) {
                        System.out.println(queue.pollLast());
                    } else {
                        System.out.println(-1);
                    }
                    break;
                case "5":
                    System.out.println(queue.size());
                    break;
                case "6":
                    if (!queue.isEmpty()) {
                        System.out.println(0);
                    } else {
                        System.out.println(1);
                    }
                    break;
                case "7":
                    if (!queue.isEmpty()) {
                        System.out.println(queue.peekFirst());
                    } else {
                        System.out.println(-1);
                    }
                    break;
                case "8":
                    if (!queue.isEmpty()) {
                        System.out.println(queue.peekLast());
                    } else {
                        System.out.println(-1);
                    }
                    break;
            }
        }
    }
}
