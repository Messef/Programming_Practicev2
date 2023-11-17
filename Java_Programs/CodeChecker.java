package Java_Programs;

public class CodeChecker   {
    public static void main (String [] args){

        System.out.println("The java charAt( ) method may not be used with");
        System.out.println("any code written in the class this year.");
        System.out.println("No looping or conditional statements may be used with the ");
        System.out.println("non-uber section of the challenge.");
        System.out.println("---------------------------------------------------------\n");

        /** In this section write the code to create an object using the default constructor **/
        /** Call the toString method **/
        /** Call reesesPieces method **/
        /** Call Amazon method **/
        /** Call returnMe method **/
        /** Look at the requirements and the output from your name **/
        /** Does the output look correct? **/
        
        /** Execute the code below **/
        StringChallenge obj = new StringChallenge("Tafbecy ", "Bardchardt");
        
        System.out.println("\n---------------------------------------------------------");
        System.out.println("Testing toString method");
        System.out.println(obj);
        System.out.println("Full Name should = Tafbecy Bardchardt ");
        
        System.out.println("\nOutput should = aabbcc");
        System.out.println("Calling ressesPieces( )");
        System.out.println(obj.reesesPieces());
        
        System.out.println("\nOutput should = 68.0");
        System.out.println("Calling amazon('f', \"ard\")");
       System.out.println(obj.amazon('f', "ard"));
        
        System.out.println("\nOutput should = cy Bar");
        System.out.println("Calling returnMe(5, 10)");
       // System.out.println(obj.returnMe(5,10));
        
        /** If you completed the Uber method, call the method here **/
        /** Run the method with several test cases to verify the code is correct **/
        
        System.out.println("\nEnd of execution");
    }
}
