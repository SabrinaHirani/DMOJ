import java.util.*;

public class ccc21s1 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        int n = Integer.parseInt(in.next());

        double[][] dimensions = new double[n][3];

        for (int i = 0; i < n; i++) {
            dimensions[i][0] = Integer.parseInt(in.next());
            if (i > 0) {
                dimensions[i-1][1] = dimensions[i][0];
            }
        }
        dimensions[n-1][1] = Integer.parseInt(in.next());

        for (int i = 0; i < n; i++) {
            dimensions[i][2] = Integer.parseInt(in.next());
        }

        double total = 0;

        for (int i = 0; i < n; i++) {
            total += dimensions[i][2]*((dimensions[i][0]+dimensions[i][1])/2);
        }

        if ((int)(total) == total) {
            System.out.println((int)(total));
        } else {
            System.out.println(total);
        }
    
        in.close();
        
    }
    
}