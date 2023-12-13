import java.util.*;

public class cco14p4 {

    static class Planet implements Comparable<Planet> {
        int a;
        int b;
    
        Planet(int a, int b) {
            this.a = a;
            this.b = b;
        }
    
        @Override
        public int compareTo(Planet p1) {
            return this.b - p1.b;
        }
    
    }
    
    public static void main( String[] args )
    {
        Scanner in = new Scanner(System.in);

        int n = Integer.parseInt(in.next());
        int p = Integer.parseInt(in.next());

        ArrayList<Planet> planets = new ArrayList<Planet>(n-1);

        long t = 0;
        long f = 0;
        for (int i = 0; i < n; i++) {
            if (p == i+1) {
                t++;
                f += Integer.parseInt(in.next());
                Integer.parseInt(in.next());
            } else {
                planets.add(new Planet(Integer.parseInt(in.next()), Integer.parseInt(in.next())));
            }
        }

        Collections.sort(planets);

        for (int i = 0; i < n-1; i++) {
            if (planets.get(i).a - planets.get(i).b >= 0) {
                if (f >= planets.get(i).b) {
                    t++;
                    f += planets.get(i).a - planets.get(i).b;
                } else {
                    break;
                }
            }
        }

        System.out.println(f);
        System.out.println(t);

        in.close();
    }
    
}