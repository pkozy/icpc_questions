import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Dreki {
    public static void main(String[] args) {
       getInput(); 
     }

    public static void getInput() throws FileNotFoundException {
	 Scanner sc = new Scanner(new File("input"));
        int[] input = new int[3];
        while (sc.hasNextInt()) {
            long aLong = sc.nextLong();
        }    
    }
}

