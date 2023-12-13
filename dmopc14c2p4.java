import java.util.*;

public class dmopc14c2p4 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        int[] forest = new int[1000000];

        int n = Integer.parseInt(in.next());
        
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += Integer.parseInt(in.next());
            forest[i] = sum;
        }

        int q = Integer.parseInt(in.next());

        for (int i = 0; i < q; i++) {
            int a = Integer.parseInt(in.next());
            int b = Integer.parseInt(in.next());
            if (a == 0) {
                System.out.println(forest[b]);
            } else {
                System.out.println(forest[b] - forest[a-1]);
            }
        }

        in.close();
        
    }
    
}