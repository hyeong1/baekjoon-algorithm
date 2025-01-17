import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        PriorityQueue<String> sortPos = new PriorityQueue<String>(new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                int chk = Integer.parseInt(o1.split(" ")[0]) - Integer.parseInt(o2.split(" ")[0]);
                if (chk == 0) {
                    chk = Integer.parseInt(o1.split(" ")[2]) - Integer.parseInt(o2.split(" ")[2]);
                }
                return chk;
            }
        });
        for (int i = 0; i < n; i++) {
            String input = br.readLine();
            input += " " + i;
            sortPos.add(input);
        }
        for (int i = 0; i < n; i++) {
            String curr = sortPos.poll();
            System.out.println(curr.split(" ")[0] + " " + curr.split(" ")[1]);
        }
    }
}
