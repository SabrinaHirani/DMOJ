import java.util.*;

public class dmopc20c3p1 {

    public static void main( String[] args )
    {
        Scanner in = new Scanner(System.in);

        int n = Integer.parseInt(in.next());
        int[] presents = new int[n+1];

        for (int i = 0; i < n; i++) {
            int l = Integer.parseInt(in.next());
            if (presents[l] > 0) {
                System.out.println("NO");
                System.exit(0);
            } else {
                presents[l]++;
            }
        }
        System.out.println("YES");

        in.close();
    }
    
}