
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nm = br.readLine().split(" ");
        Map<String, Integer> nMap = new HashMap<String, Integer>();
        Map<String, Integer> mMap = new HashMap<String, Integer>();
        for (int i = 0; i < Integer.parseInt(nm[0]); i++) {
            nMap.put(br.readLine(), i);
        }
        for (int i = 0; i < Integer.parseInt(nm[1]); i++) {
            mMap.put(br.readLine(), i);
        }

        ArrayList<String> resString = new ArrayList<String>();
        nMap.keySet().forEach(key -> {
            if (mMap.containsKey(key)) {
                resString.add(key);
            }
        });
        System.out.println(resString.size());
        Collections.sort(resString);
        resString.forEach(s -> System.out.println(s));
    }
}
