import java.util.*;

public class acc5p3 {
    public static void main( String[] args )
    {
        Scanner in = new Scanner(System.in);

        int n = Integer.parseInt(in.next());
        int k = Integer.parseInt(in.next());

        int[] diff = new int[n];

        long m = 0;
        for (int i = 0; i < n; i++) {
            int p = Integer.parseInt(in.next());
            int d = Integer.parseInt(in.next());
            m += p;
            diff[i] = p-d;
        }

        Arrays.sort(diff);

        for (int i = n-1; i >= n-k; i--) {
            m -= diff[i];
        }

        System.out.println(m);

        in.close();

    }
    
}