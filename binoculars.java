import java.util.*;

public class binoculars {

    public static void main( String[] args )
    {

        Scanner in = new Scanner(System.in);

        int n = Integer.parseInt(in.next());
        int k = Integer.parseInt(in.next());

        long[] houses = new long[n+1];
        long[] add = new long[n+1];

        long p = 0;
        for (int i = 0; i < k; i++) {
            int a = Integer.parseInt(in.next());
            int b = Integer.parseInt(in.next());
            long x = Integer.parseInt(in.next());
            if (houses[a] < x) {
                p += x-houses[a];
                add[a] += -(houses[a]-x);
                houses[b] += x;
                houses[a] = 0;
            } else {
                houses[a] -= x;
                houses[b] += x;
            }
        }

        System.out.println(p);
        for (int i = 1; i <= n; i++) {
            System.out.print(add[i] + " ");
        }

        in.close();

    }
    
}