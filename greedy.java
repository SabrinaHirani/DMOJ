import java.util.*;

public class greedy {

    static class Factory implements Comparable<Factory> {
        int price;
        int amount;
    
        Factory(int p, int a) {
            this.price = p;
            this.amount = a;
        }
    
        @Override
        public int compareTo(Factory f1) {
            return this.price - f1.price;
        }
    
    }

    public static void main( String[] args )
    {
        Scanner in = new Scanner(System.in);

        int n = Integer.parseInt(in.next());
        int m = Integer.parseInt(in.next());

        ArrayList<Factory> factories = new ArrayList<Factory>(n);

        for (int i = 0; i < n; i++) {
            factories.add(new Factory(Integer.parseInt(in.next()), Integer.parseInt(in.next())));
        }

        Collections.sort(factories);

        long p = 0;
        int idx = 0;
        while (true) {
            if (factories.get(idx).amount < m) {
                p += (factories.get(idx).price*factories.get(idx).amount);
                m -= factories.get(idx).amount;
            } else {
                p += (factories.get(idx).price*m);
                break;
            }
            idx++;
        }

        System.out.println(p);
        
        in.close();
    }
    
}