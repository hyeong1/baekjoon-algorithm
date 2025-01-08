
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        PriorityQueue<Integer> lines = new PriorityQueue<Integer>();
        lines.add(Integer.parseInt(input.split(" ")[0]));
        lines.add(Integer.parseInt(input.split(" ")[1]));
        lines.add(Integer.parseInt(input.split(" ")[2]));

        int i = lines.poll();
        int j = lines.poll();
        int k = lines.poll();
        if (i + j > k) {
            System.out.println(i + j + k);
        } else {
            System.out.println((i + j) * 2 - 1);
        }

    }
}
