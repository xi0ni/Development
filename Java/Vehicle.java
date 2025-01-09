public class Vehicle {
    private int location;

   
    public Vehicle() {
        this.location = 0;
    }

    
    public void moveForward(int blocks) {
        location += blocks;
        if (location > 20) {
            location = 20; 
        }
    }


    public void moveBackward(int blocks) {
        location -= blocks;
        if (location < -20) {
            location = -20; 
        }
    }

  
    public int getLocation() {
        return location;
    }

    
    public static void main(String[] args) {
        Vehicle car = new Vehicle();

        System.out.println("Initial location: " + car.getLocation());

        car.moveForward(10);
        System.out.println("Location after moving forward 10 blocks: " + car.getLocation());

        car.moveForward(15);
        System.out.println("Location after moving forward 15 blocks: " + car.getLocation());

        car.moveBackward(5);
        System.out.println("Location after moving backward 5 blocks: " + car.getLocation());

        car.moveBackward(25);
        System.out.println("Location after moving backward 25 blocks: " + car.getLocation());
    }
}
