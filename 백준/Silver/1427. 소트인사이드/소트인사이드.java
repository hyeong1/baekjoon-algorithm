
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String num = br.readLine();
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
        for (int i = 0; i < num.length(); i++) {
            int n = Integer.parseInt(String.valueOf(num.charAt(i)));
            maxHeap.add(n);
        }
        while (maxHeap.size() != 0) {
            System.out.print(maxHeap.poll());
        }
    }
}
