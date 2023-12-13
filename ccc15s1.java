import java.util.*;

public class ccc15s1 {

    public static void main( String[] args )
    {

        Scanner in = new Scanner(System.in);

        int k = Integer.parseInt(in.next());
        Stack<Integer> money = new Stack<Integer>();

        for (int i = 0; i < k; i++) {
            int m = Integer.parseInt(in.next());
            if (m == 0) {
                money.pop();
            } else {
                money.push(m);
            }
        }

        int sum = 0;
        while (money.size() > 0) {
            sum += money.pop();
        }

        System.out.print(sum);

        in.close();
    }
}