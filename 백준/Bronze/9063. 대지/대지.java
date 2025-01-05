import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.TreeSet;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        TreeSet<Integer> posX = new TreeSet<>();
        TreeSet<Integer> posY = new TreeSet<>();
        for (int i = 0; i < n; i++) {
            String read = br.readLine();
            posX.add(Integer.parseInt(read.split(" ")[0]));
            posY.add(Integer.parseInt(read.split(" ")[1]));
        }
        List<Integer> listX = new ArrayList<>(posX);
        List<Integer> listY = new ArrayList<>(posY);
        System.out.println((listX.get(listX.size()-1) - listX.get(0)) * (listY.get(listY.size()-1) - listY.get(0)));
    }
}
