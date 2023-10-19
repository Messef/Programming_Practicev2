package Java_Programs;
class SecondClass
{
   public SecondClass() {

   }
   public void doSomething() {
      System.out.println("Inside Second Class");
   }
   public static void main(String[] args) {
      SecondClass myClass = new SecondClass();
      myClass.doSomething();
   }

}
