import java.util.*;

public class ccc04j4 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        String key = in.nextLine();
        String text = in.nextLine();

        int count = 0;
        String cipher = "";
        for (int i = 0; i < text.length(); i++) {
            if (Character.isLetter(text.charAt(i))) {
                int ch = ((text.charAt(i)+(key.charAt(count%key.length())-'A')-'A')%26)+'A';
                cipher += (char) ch;
                count++;
            }
        }

        System.out.println(cipher);

        in.close();
        
    }
    
}