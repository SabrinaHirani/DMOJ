import java.util.*;

public class ccc08s1 {

    static class City implements Comparable<City> {

        String name = "";
        int temperature = 0;

        City(String n, int t) {
            this.name = n;
            this.temperature = t;
        }

        @Override
        public int compareTo(ccc08s1.City o) {
            return this.temperature - ((City) o).temperature;
        }

    }

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        ArrayList<City> city = new ArrayList<City>();

        String name = "";
        while (!(name.equals("Waterloo"))) {
            name = in.next();
            city.add(new City(name, Integer.parseInt(in.next())));
        }

        city.sort(null);

        System.out.println(city.get(0).name);

        in.close();
        
    }
    
}