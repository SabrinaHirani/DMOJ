import java.util.*;

public class ccc05j3 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        ArrayList<String> dir = new ArrayList<String>();
        ArrayList<String> street = new ArrayList<String>();

        int i = 0;
        String next = in.nextLine();
        while (!(next.equals("SCHOOL"))) {
            if (i%2 == 0) {
                if (next.charAt(0) == 'L') {
                    dir.add("RIGHT");
                } else {
                    dir.add("LEFT");
                }
            } else {
                street.add(next);
            }
            next = in.nextLine();
            i++;
        }

        for (int j = dir.size()-1; j >= 0 ; j--) {
            if (j != 0) {
                System.out.printf("Turn %S onto %S street.%n", dir.get(j), street.get(j-1));
            } else {
                System.out.printf("Turn %S into your HOME.%n", dir.get(j));
            }
        }

        in.close();
        
    }
    
}