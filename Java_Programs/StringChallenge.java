package Java_Programs;
/**
 * Write a description of class StringChallenge here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class StringChallenge
{
    // instance variables - replace the example below with your own
    private String firstName;
    private String lastName;
    private String fullName;
    public StringChallenge()
    {
        // initialise instance variables
        firstName = "Akshat";
        lastName = "Tewari";
        fullName = firstName.concat(lastName);
    }
    public StringChallenge(String firstName, String lastName)
    {
        // initialise instance variables
        /* 
        this.firstName = firstName;
        this.lastName = lastName;
        fullName += this.firstName;
        fullName+=this.lastName;*/
        this.firstName = firstName;
        this.lastName = lastName;
        fullName = concat();

    }
    public String reesesPieces() {
        return returner(fullName.substring(1, 2), fullName.substring(3, 4), fullName.substring(5, 6));
    }
    public String concat() {
        return this.firstName + " " + this.lastName;
    }
    public int letterFir(char a) {
      return this.fullName.indexOf(a);
    }
    public int stringLas(String a) {
    int find = fullName.indexOf(a);

    String result =  fullName.substring(find+1);
    System.out.println("String las: " + a + "\nString las: " + find + "\nString las: " + result);
    return result.indexOf(a) + find;
    }
    public double returner(int a, int b) {
        int store_a = a;
        a*=a;
        a*=store_a;
        return a + (b-store_a);
    }
    public String returner(String a, String b, String c) {
        return a + a + b + b + c +c;
    }
    public double amazon(char a, String b) {
       int var = letterFir(a);
       int varTwo = stringLas(b);
       System.out.println(var + " " + varTwo + " " + b + " " + this.fullName);
       return returner(var, varTwo);
    } 

}
