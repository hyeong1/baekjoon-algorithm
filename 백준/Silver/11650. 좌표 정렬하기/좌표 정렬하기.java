
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        PriorityQueue<int[]> sortPos = new PriorityQueue<int[]>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0] == o2[0]) return o1[1] - o2[1];
                return o1[0] - o2[0];
            }
        });
        for (int i = 0; i < n; i++) {
            String input = br.readLine();
            int[] pos = new int[2];
            pos[0] = Integer.parseInt(input.split(" ")[0]);
            pos[1] = Integer.parseInt(input.split(" ")[1]);
            sortPos.add(pos);
        }
        for (int i = 0; i < n; i++) {
            int[] curr = sortPos.poll();
            System.out.println(curr[0] + " " + curr[1]);
        }
    }
}
