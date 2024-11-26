// please implement Shape and Color here
abstract class Shape {
    protected String color;
    protected double x; 
    protected double y; 

    public void setCoordinates(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public String getCoordinates() {
        return "(" + x + ", " + y + ")";
    }

    public abstract double calculateArea();

    public abstract double calculatePerimeter();

    public abstract boolean isOverlapping(Shape other);
}

interface Color {
    void setColor(String color);

    String getColor();
}

class Square extends Shape implements Color {
    public double sideLength;

    public Square(double sideLength) {
        this.sideLength = sideLength;
    }

    @Override
    public double calculateArea() {
        return sideLength * sideLength;
    }

    @Override
    public double calculatePerimeter() {
        return 4 * sideLength;
    }

    @Override
    public boolean isOverlapping(Shape other) {
        if (other instanceof Square) {
            Square square = (Square) other;
            return !(x + sideLength <= square.x || square.x + square.sideLength <= x ||
                     y + sideLength <= square.y || square.y + square.sideLength <= y);
        } else if (other instanceof Rectangle) {
            Rectangle rectangle = (Rectangle) other;
            return !(x + sideLength <= rectangle.x || rectangle.x + rectangle.width <= x ||
                     y + sideLength <= rectangle.y || rectangle.y + rectangle.length <= y);
        }
        return false;
    }

    @Override
    public void setColor(String color) {
        this.color = color;
    }

    @Override
    public String getColor() {
        return color;
    }
}


class Rectangle extends Shape implements Color {
    public double width;
    public double length;

    public Rectangle(double width, double length) {
        this.width = width;
        this.length = length;
    }

    @Override
    public double calculateArea() {
        return width * length;
    }

    @Override
    public double calculatePerimeter() {
        return 2 * (width + length);
    }

    @Override
    public boolean isOverlapping(Shape other) {
        if (other instanceof Square) {
            Square square = (Square) other;
            return !(x + width <= square.x || square.x + square.sideLength <= x ||
                     y + length <= square.y || square.y + square.sideLength <= y);
        } else if (other instanceof Rectangle) {
            Rectangle rectangle = (Rectangle) other;
            return !(x + width <= rectangle.x || rectangle.x + rectangle.width <= x ||
                     y + length <= rectangle.y || rectangle.y + rectangle.length <= y);
        }
        return false;
    }

    @Override
    public void setColor(String color) {
        this.color = color;
    }

    @Override
    public String getColor() {
        return color;
    }
}


// please don't modify the testcases below

public class Main {
    public static void main(String[] args) {
        Square square = new Square(6);
        square.setColor("Red");
        square.setCoordinates(10, 15);
        System.out.println("square Area: " + square.calculateArea());
        System.out.println("square Perimeter: " + square.calculatePerimeter());
        System.out.println("square Color: " + square.getColor());
        System.out.println("square Coordinates: " + square.getCoordinates());

        Rectangle rectangle = new Rectangle(11, 25);
        rectangle.setColor("Blue");
        rectangle.setCoordinates(-5, -8);
        System.out.println("rectangle Area: " + rectangle.calculateArea());
        System.out.println("rectangle Perimeter: " + rectangle.calculatePerimeter());
        System.out.println("rectangle Color: " + rectangle.getColor());
        System.out.println("rectangle Coordinates: " + rectangle.getCoordinates());

        Shape anotherRectangle = new Rectangle(3, 4);
        anotherRectangle.setCoordinates(0, 0);
        System.out.println("anotherRectangle Area: " + anotherRectangle.calculateArea());
        System.out.println("anotherRectangle Perimeter: " + anotherRectangle.calculatePerimeter());
        System.out.println("anotherRectangle Coordinates: " + anotherRectangle.getCoordinates());

        Color color = new Square(12);
        color.setColor("Green");
        System.out.println("Color: " + color.getColor());

        System.out.println("square and rectangle overlap: " + square.isOverlapping(rectangle));
        System.out.println("rectangle and anotherRectangle overlap: " + rectangle.isOverlapping(anotherRectangle));
        System.out.println("anotherRectangle and square overlap: " + anotherRectangle.isOverlapping(square));
    }
}
/*
output:
square Area: 36.0
square Perimeter: 24.0
square Color: Red
square Coordinates: (10.0, 15.0)
rectangle Area: 275.0
rectangle Perimeter: 72.0
rectangle Color: Blue
rectangle Coordinates: (-5.0, -8.0)
anotherRectangle Area: 12.0
anotherRectangle Perimeter: 14.0
anotherRectangle Coordinates: (0.0, 0.0)
Color: Green
square and rectangle overlap: false
rectangle and anotherRectangle overlap: true
anotherRectangle and square overlap: false
*/