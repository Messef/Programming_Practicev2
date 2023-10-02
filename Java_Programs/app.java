package Java_Programs;
import java.util.Scanner;
public class app {
    static Scanner myScan = new Scanner(System.in);
    public static void main(String[] args) {
        System.out.println("four digit real number 10.10<x<99.9: ");
        double firstInt = myScan.nextDouble();
        int rightSide = (int) firstInt;
        System.out.println(firstInt);
        firstInt+=.0001;
        firstInt*=100;
        System.out.println(firstInt);
        firstInt-= (rightSide*100);
        System.out.println(firstInt);
        int leftSide = (int)firstInt;
        System.out.println("Right of decimal place: " + rightSide + "");
        System.out.println("Left of decimal place: " + leftSide ); 
        System.out.println("goodbye!");
    
    }
}
