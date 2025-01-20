
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Map<String, String> logs = new HashMap<String, String>();
        for (int i = 0; i < n; i++) {
            String[] log = br.readLine().split(" ");
            logs.put(log[0], log[1]);
        }
        ArrayList<String> res = new ArrayList<String>();
        for (String key : logs.keySet()) {
            if (logs.get(key).equals("enter")) {
                res.add(key);
            }
        }
        Collections.sort(res, Collections.reverseOrder());
        res.forEach(System.out::println);
    }
}
