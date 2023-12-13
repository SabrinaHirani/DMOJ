import java.util.*;

public class ecoo19r1p1 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        for (int repeat = 0; repeat < 10; repeat++) {

            int n = Integer.parseInt(in.next());
            int m = Integer.parseInt(in.next());
            int d = Integer.parseInt(in.next());

            int shirt = n;
            HashMap<Integer, Integer> events= new HashMap<Integer, Integer>();

            for (int i = 0; i < m; i++) {
                int x = Integer.parseInt(in.next());
                if (events.get(x) == null) {
                    events.put(x, 1);
                } else {
                    events.put(x, events.get(x)+1);
                }
            }

            int count = 0;
            for (int i = 1; i <= d; i++) {
                if (n <= 0) {
                    count += 1;
                    n = shirt;
                }
                if (events.get(i) != null) {
                    n += events.get(i);
                    shirt += events.get(i);
                }
                n--;
            }

            System.out.println(count);

        }

        in.close();

    }

    
}