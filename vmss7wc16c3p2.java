import java.util.*;

public class vmss7wc16c3p2 {

    static ArrayList<Integer>[] neighbourhood = null;
    static boolean[] checked = null;

    public static void dfs(int node) {

        checked[node] = true;
        for (int i = 0; i < neighbourhood[node].size(); i++) {
            if (!(checked[neighbourhood[node].get(i)])) {
                dfs(neighbourhood[node].get(i));
            }
        }

    }

    public static void main( String[] args )
    {
        Scanner in = new Scanner(System.in);

        int n = Integer.parseInt(in.next());
        int m = Integer.parseInt(in.next());
        int a = Integer.parseInt(in.next());
        int b = Integer.parseInt(in.next());

        neighbourhood = new ArrayList[n+1];

        for (int i = 1; i < n+1; i++) {
            neighbourhood[i] = new ArrayList<Integer>(n);
        }

        for (int i = 0; i < m; i++) {
            int x = Integer.parseInt(in.next());
            int y = Integer.parseInt(in.next());
            neighbourhood[x].add(y);
            neighbourhood[y].add(x);
        }

        checked = new boolean[n+1];

        dfs(a);

        if (checked[b] == true) {
            System.out.print("GO SHAHIR!");
        } else {
            System.out.print("NO SHAHIR!");
        }

        in.close();

    }
    
}