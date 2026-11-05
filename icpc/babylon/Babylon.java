import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;

public class Babylon{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int testnum = sc.nextInt();
        int[][] tests = new int[testnum][];
    }
    
    public static void init(Scanner sc, int[][] tests, int testnum) {
        for(int i = 0; i < testnum; i++) {
            int blocknum = sc.nextInt();
	    tests[i] = new int[blocknum];
            for (int j = 0; j < blocknum; j++) {
                Block block = new Block(sc.nextInt(), sc.nextInt());
                blocklist.add(block);
            }
        }
    }
}
