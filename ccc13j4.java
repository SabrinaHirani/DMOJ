import java.util.*;

public class ccc13j4 {
    
    public static void main( String[] args )
    {
        Scanner in = new Scanner(System.in);

        int t = Integer.parseInt(in.next());
        int c = Integer.parseInt(in.next());

        int[] chores = new int[c];
        for (int i = 0; i < c; i++) {
            chores[i] = Integer.parseInt(in.next());
        }

        Arrays.sort(chores);

        for (int i = 0; i < chores.length; i++) {
            if (!(t >= chores[i])) {
                System.out.print(i);
                break;
            }
            t -= chores[i];
        }

        in.close();

    }
    
}