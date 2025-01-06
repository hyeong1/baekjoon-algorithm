import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Set<Integer> angles = new HashSet<Integer>();
        int sum = 0;
        for (int i = 0; i < 3; i++) {
            int angle = Integer.parseInt(br.readLine());
            sum += angle;
            angles.add(angle);
        }

        String res = "";
        if (sum != 180) {
            res = "Error";
        } else if (angles.size() == 1) {
            res = "Equilateral";
        } else if (angles.size() == 2) {
            res = "Isosceles";
        } else if (angles.size() == 3) {
            res = "Scalene";
        }
        System.out.println(res);
    }
}
