
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] inputs = br.readLine().split(" ");

        Set<Integer> sortedSet = new HashSet<Integer>();
        for (int i = 0; i < n; i++) {
            sortedSet.add(Integer.parseInt(inputs[i]));
        }

        List<Integer> sortedList = new ArrayList<>(sortedSet);
        Collections.sort(sortedList);

        Map<Integer, Integer> sorted = new HashMap<Integer, Integer>();
        for (int i = 0; i < sortedList.size(); i++) {
            sorted.put(sortedList.get(i), i);
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            int curr = Integer.parseInt(inputs[i]);
            sb.append(sorted.get(curr)).append(" ");
        }
        System.out.print(sb.toString().trim());
    }
}
