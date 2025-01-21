
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] sang = br.readLine().split(" ");
        Map<String, Integer> sangMap = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int sum = 1;
            if (sangMap.get(sang[i]) != null) {
                sum = sangMap.get(sang[i]) + 1;
            }
            sangMap.put(sang[i], sum);
        }
        int m = Integer.parseInt(br.readLine());
        String[] cards = br.readLine().split(" ");
        StringBuilder stringBuilder = new StringBuilder();
        for (int i = 0; i < m; i++) {
            Integer nn = sangMap.get(cards[i]);
            if (nn != null) {
                stringBuilder.append(nn + " ");
            } else {
                stringBuilder.append("0 ");
            }
        }
        System.out.println(stringBuilder.toString());
    }
}
