import java.util.*;

public class wac1p1 {

    public static void main( String[] args )
    {
        Scanner in = new Scanner(System.in);

        int t = Integer.parseInt(in.next());

        for (int i = 0; i < t; i++) {

            long m = Long.parseLong(in.next())*2;
            long n = (int) (Math.sqrt(m));

            if ((n-1)*((n-1)-1) >= m) {
                System.out.print((n-1)+"\n");
            } else if (n*(n-1) >= m) {
                System.out.print(n+"\n");
            } else if ((n+1)*((n+1)-1) >= m) {
                System.out.print((n+1)+"\n");
            } else {
                System.out.print((n+2)+"\n");
            }
        }

        in.close();

    }
    
}