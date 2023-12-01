package Java_Programs;

public class CodeChecker   {
    private double x;
    public CodeChecker(double avacadoWeight) {
        x = avacadoWeight;
    }
    public double avacadoWeight() {
        return x;
    }
    public int getBox(double weightBox, double tolerance) {
        double max = weightBox - tolerance;
        return (int)Math.floor(max /  avacadoWeight());
        
    }
}
