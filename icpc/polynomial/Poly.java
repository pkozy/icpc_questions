import java.util.Scanner;

public class Poly {
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);

        int numTest = in.nextInt();
        for (int i = 0; i < numTest; i++) {
            int deg1 = in.nextInt();
            PolyNoMeal polynomial1 = new PolyNoMeal(deg1);
            for (int j = 0; j < deg1; j++) {
                polynomial1.addTerm(deg1, in.nextInt());
            }

            int deg2 = in.nextInt();
            PolyNoMeal polynomial2 = new PolyNoMeal(deg2);
            for (int j = 0; j < deg2+1; j++) {
                polynomial2.addTerm(deg2, in.nextInt());
            }

            System.out.println("" + polynomial1 + "\n" + polynomial2);
             
        }
        
    }
}


