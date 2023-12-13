import java.util.*;

public class ccc21s3 {

    public static int n = 0;
    public static int[][] friends = null;

    public static long cost(long p) {
        long cost = 0;
        for (int i = 0; i < n; i++) {
            cost += Math.max(0, friends[i][1]*(Math.abs(p-friends[i][0])-friends[i][2]));
        }
        return cost;
    }
    
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        n = Integer.parseInt(in.next());

        friends = new int[n][3];

        long left = Long.MAX_VALUE;
        long right = Long.MIN_VALUE;

        for (int i = 0; i < n; i++) {

            friends[i][0] = Integer.parseInt(in.next());
            friends[i][1] = Integer.parseInt(in.next());
            friends[i][2] = Integer.parseInt(in.next());

            left = Math.min(left, friends[i][0]);
            right = Math.max(right, friends[i][0]);
        }

        while (left < right) {

            long middle = (left + right)/2;

            if (cost(middle) < cost(middle+1)) {
                right = middle;
            } else {
                left = middle+1;
            }

        }

        System.out.println(cost(left));

        in.close();
        
    }
}