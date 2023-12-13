import java.util.*;

public class ccc11j2 {

    public static double altitude(int t, int h) {

        double a = 0;

        a += Math.pow(t, 4) * -6;
        a += Math.pow(t, 3) * h;
        a += Math.pow(t, 2) * 2;
        a += t;

        return a;
        
    }

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        int h = Integer.parseInt(in.next());
        int m = Integer.parseInt(in.next());

        int count = -1;
        for (int i = 1; i <= m; i++) {
            if (altitude(i, h) <= 0) {
                count = i;
                break;
            }
        }

        if (count >= 0) {
            System.out.printf("The balloon first touches ground at hour: %n%d", count);
        } else {
            System.out.println("The balloon does not touch ground in the given time.");
        }

        in.close();
        
    }
    
}