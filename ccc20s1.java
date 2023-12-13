import java.util.*;

public class ccc20s1 {

    static class Observation implements Comparable<Observation> {

        int t;
        int d;

        Observation(int t, int d) {
            this.t = t;
            this.d = d;
        }

        @Override
        public int compareTo(Observation o) {
            return this.t - o.t;
        }

    }

    public static void main(String[] args) {

        ArrayList<Observation> observations = new ArrayList<Observation>();
        ArrayList<Double> speeds = new ArrayList<Double>();
        
        Scanner in = new Scanner(System.in);

        int n = Integer.parseInt(in.next());

        for (int i = 0; i < n; i++) {
            observations.add(new Observation(Integer.parseInt(in.next()), Integer.parseInt(in.next())));
        }

        Collections.sort(observations);

        for (int i = 0; i < n-1; i++) {
            speeds.add(((double)(Math.abs(observations.get(i+1).d - observations.get(i).d))/(observations.get(i+1).t - observations.get(i).t)));
        }

        Collections.sort(speeds, Collections.reverseOrder());

        System.out.println(speeds.get(0));

        in.close();
    }
    
}