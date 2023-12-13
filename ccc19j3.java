import java.util.*;

public class ccc19j3 {

    public static void main(String[] args) {
        
        Scanner in = new Scanner(System.in);

        int n = Integer.parseInt(in.nextLine());

        for (int i = 0; i < n; i++) {

            String text = in.nextLine() + " ";

            int count = 0;
            char last = text.charAt(0);

            for (int j = 0; j < text.length(); j++) {

                if (text.charAt(j) != last) {

                    System.out.print(count + " " + last + " ");

                    count = 1;
                    last = text.charAt(j);

                } else {

                    count++;

                }
            }
            System.out.print("\n");
        }

        in.close();
    }
    
}