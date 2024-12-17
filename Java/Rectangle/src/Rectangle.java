import java.lang.Math;

public class Rectangle {
    private int length;
    private int width;
    public Rectangle(int length, int width) {
        this.length = length;
        this.width = width;
    }
    public boolean isSquare() {
        return this.length == this.width && this.length > 0;
    }
    public int getArea() {
        return this.length * this.width;
    }
    public int getPerimeter() {
        return 2 * (this.length + this.width);
    }
    public int getLength() {
        return this.length;
    }
    public int getWidth() {
        return this.width;
    }
}

/*clas called rectangle that has length and width as instance variables and a 
method that determines if the rectangle is a square based off of the dimentions returns true or false. 
inclue a default constructor a parameter consturctor and an accestor and mutator methods */