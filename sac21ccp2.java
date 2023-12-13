import java.util.*;

public class sac21ccp2 {

    public static void main( String[] args )
    {
        Scanner in = new Scanner(System.in);

        int n = Integer.parseInt(in.next());
        int k = Integer.parseInt(in.next());

        int[] garbage = new int[n+1];
        for (int i = 1; i < n+1; i++) {
            garbage[i] = Integer.parseInt(in.next());
        }

        Arrays.sort(garbage);

        long f = 0;
        for (int i = 0; i < k; i++) {
            f += garbage[n-i];
        }

        System.out.print(f);

        in.close();
    }
    
}