public class Main {
    public static void main(String[] args) {
        Rectangle rect = new Rectangle(5, 5);

        System.out.println("is it a Square? : " + rect.isSquare());
        System.out.println("Area: " + rect.getArea());
        System.out.println("Perimeter: " + rect.getPerimeter());
    }
}
