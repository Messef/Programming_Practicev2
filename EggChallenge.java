public class EggChallenge 
{
    public EggChallenge() {
        
}
    public void displayEgg() {
    System.out.println("   __");
    System.out.println(" /    \\");
    System.out.println("|      |");
    System.out.println(" \\ __ /");
    } 
    public void displayHouse() {
    System.out.println("  /\\");
    System.out.println(" /  \\");
    System.out.println("/    \\");
    System.out.println("|    |");
    System.out.println("| || |");
    System.out.println("| || |");
}
    public void displayElephant() {
    System.out.println("          _     _");
    System.out.println("         / \\~~~/ \\");
    System.out.println("   ,----(    ..   )");
    System.out.println("  /      \\__   __/");
    System.out.println(" /|        (\\ |( ");
    System.out.println("^ \\ /__\\    /\\| ");
    System.out.println("  |_|   |__|-\"");
}
    public void displayCat()    {
    System.out.println(" _");
    System.out.println("( \\");
    System.out.println(" ) )");
    System.out.println("( (  .-''''-.  A.-.A");
    System.out.println(" \\ \\/        \\/ , , \\");
    System.out.println("  \\   \\      =;  t  /=");
    System.out.println("   \\   |''''-  ',--'");
    System.out.println("    / //    | ||");
    System.out.println("   /_,))    |_,))");
}
}
class app
{
    public static void main(String[] args) {
    EggChallenge printEgg = new EggChallenge();
    printEgg.displayEgg();
    printEgg.displayHouse();
    printEgg.displayElephant();
    printEgg.displayCat();
}
}