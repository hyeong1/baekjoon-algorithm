
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Deque<String> queue = new ArrayDeque<>();
        int n = Integer.parseInt(br.readLine());
        StringTokenizer types = new StringTokenizer(br.readLine());
        StringTokenizer nums = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(br.readLine());
        StringTokenizer inputs = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            if (types.nextToken().equals("0")) {
                queue.addLast(nums.nextToken());
            } else {
                nums.nextToken();
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            String x = inputs.nextToken();
            if (queue.isEmpty()) {
                sb.append(x).append(" ");
            } else {
                queue.addFirst(x);
                sb.append(queue.pollLast()).append(" ");
            }
        }
        System.out.println(sb);
    }
}
