import java.util.*;

public class set {

    public static void main( String[] args )
    {
        Scanner in = new Scanner(System.in);

        int n = Integer.parseInt(in.next());
        HashSet<Integer> elements = new HashSet<Integer>(n);

        for (int i = 0; i < n; i++) {
            elements.add(Integer.parseInt(in.next()));
        }

        System.out.println(elements.size());

        in.close();
    }
    
}