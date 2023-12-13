import java.util.*;

public class ccc21s2 {
    
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        int m = Integer.parseInt(in.next());
        int n = Integer.parseInt(in.next());
        int k = Integer.parseInt(in.next());

        boolean[] canvasV = new boolean[m+1];
        boolean[] canvasH = new boolean[n+1];

        for (int i = 0; i < k; i++) {
            char dir = in.next().charAt(0);
            int which = Integer.parseInt(in.next());

            if (dir == 'R') {
                canvasV[which] = !canvasV[which];
            }
            
            if (dir == 'C') {
                canvasH[which] = !canvasH[which];
            }
        }

        int gold = 0;

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (!canvasV[i] && canvasH[j] || canvasV[i] && !canvasH[j]) {
                    gold++;
                }
            }
        }

        System.out.println(gold);

        in.close();
        
    }
}