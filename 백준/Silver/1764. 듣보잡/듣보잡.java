
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nm = br.readLine().split(" ");
        Map<String, Integer> nMap = new HashMap<String, Integer>();
        ArrayList<String> resString = new ArrayList<String>();
        for (int i = 0; i < Integer.parseInt(nm[0]); i++) {
            nMap.put(br.readLine(), i);
        }
        for (int i = 0; i < Integer.parseInt(nm[1]); i++) {
            String m = br.readLine();
            if (nMap.containsKey(m)) {
                resString.add(m);
            }
        }

        System.out.println(resString.size());
        Collections.sort(resString);
        resString.forEach(s -> System.out.println(s));
    }
}
