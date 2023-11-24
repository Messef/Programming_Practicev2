package Java_Programs;

public class CodeChecker   {
    public static void main (String [] args){
        int max = -5;
        int min = -7;
        for (int i = 0; i < 30; i++) {
            double rn = Math.random();
            int num = (int)(rn * (max - min+1)) + min;
            System.out.println(num);
        }
        
    }
}
