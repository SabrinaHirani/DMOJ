import java.util.*;

public class ccc06s1 {

    public static void main(String[] args) {

        int[] gene = new int[5];

        Scanner in = new Scanner(System.in);

        String Alice = in.nextLine();
        String Bob = in.nextLine();

        for (int i = 0; i < 5; i++) {
            if ((Character.isUpperCase(Alice.charAt(i*2)) && Character.isUpperCase(Alice.charAt((i*2)+1))) || (Character.isUpperCase(Bob.charAt(i*2)) && Character.isUpperCase(Bob.charAt((i*2)+1)))) {
                gene[i] = 0;
            } else if (Character.isLowerCase(Alice.charAt(i*2)) && Character.isLowerCase(Bob.charAt(i*2))) {
                gene[i] = 1;
            } else {
                gene[i] = 2;
            }
        }
        int x = Integer.parseInt(in.nextLine());

        for (int i = 0; i < x; i++) {

            String child = in.nextLine();

            for (int j = 0; j < 5; j++) {
                if (((gene[j] == 0) && (Character.isLowerCase(child.charAt(j)))) || ((gene[j] == 1) && (Character.isUpperCase(child.charAt(j))))) {
                    System.out.println("Not their baby!");
                    break;
                }
                if (j == 4) {
                    System.out.println("Possible baby.");
                }
            }

        }

        in.close();
    }
    
}