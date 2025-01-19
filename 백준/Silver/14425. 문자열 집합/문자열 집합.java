
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        int n = Integer.parseInt(inputs[0]);
        int m = Integer.parseInt(inputs[1]);
        Map<Integer, String> mapS = new HashMap<Integer, String>();
        for (int i = 0; i < n; i++) {
            mapS.put(i, br.readLine());
        }
        Map<Integer, String> target = new HashMap<Integer, String>();
        for (int i = 0; i < m; i++) {
            target.put(i, br.readLine());
        }
        int res = 0;
        for (int i = 0; i < n; i++) {
            String curr = mapS.get(i);
            for (int j = 0; j < m; j++) {
                if (curr.equals(target.get(j))) {
                    res++;
                }
            }
        }
        System.out.println(res);
    }
}
