import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String position = "";
        ArrayList<Integer> xs = new ArrayList<Integer>();
        ArrayList<Integer> ys = new ArrayList<Integer>();
        for (int i = 0; i < 3; i++) {
            position = br.readLine();
            xs.add(Integer.parseInt(position.split(" ")[0]));
            ys.add(Integer.parseInt(position.split(" ")[1]));
        }
        xs.sort(Comparator.naturalOrder());
        ys.sort(Comparator.naturalOrder());
        int x = xs.get(0), y = ys.get(0);
        for (int i = 1; i < 3;i ++) {
            if (x == -1) {
                x = xs.get(i);
            } else if (x == xs.get(i)) {
                x = -1;
            }
            if (y == -1) {
                y = ys.get(i);
            } else if (y == ys.get(i)) {
                y = -1;
            }
        }
        System.out.println(x + " " + y);
    }
}
