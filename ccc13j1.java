import java.util.*;

public class ccc13j1 {
    
    public static void main( String[] args )
    {
        Scanner in = new Scanner(System.in);

        int y = Integer.parseInt(in.next());
        int m = Integer.parseInt(in.next());
        int o = m+(m-y);

        System.out.print(o);

        in.close();
    }
    
}