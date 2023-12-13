import java.util.*;

public class ccc05s2 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        int x = 0;
        int y = 0;

        int c = Integer.parseInt(in.next());
        int r = Integer.parseInt(in.next());

        int chx = Integer.parseInt(in.next());
        int chy = Integer.parseInt(in.next());

        while ((chx != 0) || (chy != 0)) {

            x = Math.min(Math.max(0, x+chx), c);
            y = Math.min(Math.max(0, y+chy), r);

            System.out.println(x +" "+y);

            chx = Integer.parseInt(in.next());
            chy = Integer.parseInt(in.next());
        } 

        in.close();
        
    }
    
}