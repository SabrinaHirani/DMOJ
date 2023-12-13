import java.util.*;

public class ccc19s2 {

    public static boolean isPrime(int p) {
        
        for (int i = 2; i <= Math.sqrt(p)+1; i++) {
            if (p%i == 0) {
                return false;
            }
        }

        return true;

    }

    public static void main(String[] args) {
        
        Scanner in = new Scanner(System.in);

        int t = Integer.parseInt(in.next());

        for (int i = 0; i < t; i++) {

            int n = Integer.parseInt(in.next())*2;

            for (int j = (n-2); j > 1; j--) {

                if (isPrime(j)) {

                    if (isPrime(n-j)) {

                        System.out.println(j + " " + (n-j));
                        break;
                        
                    }
                }

            }
        }

        in.close();


    }

    
}