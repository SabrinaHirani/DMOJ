import java.util.*;

public class ccc17s2 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        int n = Integer.parseInt(in.nextLine());

        int[] measurement = new int[n];

        for (int i = 0; i < n; i++) {
            measurement[i] = Integer.parseInt(in.next());
        }
        Arrays.sort(measurement);

        int mid = (int)(Math.ceil(n/2)) + (n%2);

        for (int i = 0; i < n/2; i++) {

                System.out.print(measurement[mid-1-i] + " ");
                System.out.print(measurement[mid+i] + " ");

        }
        if (n%2 != 0) {
            System.out.print(measurement[0] + " ");
        }

        in.close();
        
    }
    
}