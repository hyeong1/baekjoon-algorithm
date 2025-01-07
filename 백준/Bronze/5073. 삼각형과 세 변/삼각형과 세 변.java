import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = "";

        while (true) {
            line = br.readLine();
            if (line.equals("0 0 0")) break;
            List<Integer> lines = new ArrayList<Integer>();
            lines.add(Integer.parseInt(line.split(" ")[0]));
            lines.add(Integer.parseInt(line.split(" ")[1]));
            lines.add(Integer.parseInt(line.split(" ")[2]));

            String res = "";
            if (lines.get(0) + lines.get(1) > lines.get(2) &&
                lines.get(1) + lines.get(2) > lines.get(0) &&
                lines.get(0) + lines.get(2) > lines.get(1)) {
                Set<Integer> setLines = new HashSet<>(lines);
                if (setLines.size() == 1) {
                    res = "Equilateral";
                } else if (setLines.size() == 2) {
                    res = "Isosceles";
                } else if (setLines.size() == 3) {
                    res = "Scalene";
                }
            } else {
                res = "Invalid";
            }
            System.out.println(res);
        }
    }
}
