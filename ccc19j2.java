import java.util.*;

public class ccc19j2 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        int l = Integer.parseInt(in.next());

        for (int i = 0; i < l; i++) {

            int n = Integer.parseInt(in.next());
            char x = in.next().charAt(0);

            for (int j = 0; j < n; j++) {
                System.out.print(x);
            }
            System.out.print("\n");
            
        }

        in.close();
        
    }
    
}