import java.util.Scanner;

public class Assignment2 {
        private String callsign;
        private int bearing;
        private int altitude;
        private double distance;


        public Assignment2(String callsign, int bearing, int altitude, double distance) {
            this.callsign = callsign;
            this.bearing = bearing;
            this.altitude = altitude;
            this.distance = distance;
            
        }

        public void move(double dist, int dir) {
            this.distance += dist; 
            System.out.println("Airplane moved to " + this.distance + " Nautical miles from control tower");
        }

        public void gainAlt(double alt) {
            this.altitude += alt;
            System.out.println("The airplane gained " + this.altitude + " altitude.");
        }

        public void loseAlt(double alt) {
            this.altitude *= (-1);
            this.altitude += alt;
            System.out.println("The airplane lost " + this.altitude + " altitude.");
        }
        
        

        public void getAlt(int alt) {
            this.altitude = alt;
            System.out.println("The airplane is at " + this.altitude + " altitude.");
        }

        public void DescribeAirplane(){
            System.out.print("Airplane ");
            System.out.println("callsign: " + this.callsign);
            System.out.println("");
            System.out.println("Altitude: "+this.altitude);
            System.out.println("Bearing: "+this.bearing);
            System.out.println("Distance: "+this.distance);
            System.out.println("");
        }

        public double distTo(Assignment2 other){

            double r1 = this.distance;
            double r2 = other.distance;
            double u1 = Math.toRadians(this.bearing);
            double u2 = Math.toRadians(other.bearing);
            double between = Math.sqrt(r1*r1 + r2*r2 - 2*r1*r2*Math.cos(u2-u1));
            return (double)Math.round(100*between)/100;
        }

        public void NewAirplane() {
        Scanner input = new Scanner(System.in);
        System.out.println("What is the callsign: ");
        String call = input.nextLine();
        call = call.toUpperCase();
        this.callsign = call;
        System.out.println("What is the heading direction: ");
        int heading = input.nextInt();
        this.bearing = heading;
        System.out.println("What is the altitude: ");
        int altitude = input.nextInt();
        this.altitude = altitude;
        System.out.println("What is the distance to the airport in nm: ");
        double distance = input.nextDouble();
        this.distance = distance;
        
        input.close();
        }
        
        public void initialize(){
            Assignment2 Airplane1 = new Assignment2("AAA01", 0,0, 1);
            Assignment2 Airplane2 = new Assignment2("AAA03", 128,30000, 15.8);
            Assignment2 Airplane3 = new Assignment2("N461P",0,0,0);
            int tempDist = (int) Airplane2.distTo(Airplane3);


            Airplane3.NewAirplane();

            Airplane1.move(tempDist, 65);

            Airplane2.move(8.0,135);

            Airplane3.move(5.0,55);

            Airplane1.gainAlt(3000);
            Airplane1.DescribeAirplane();

            Airplane2.gainAlt(2000);
            Airplane2.DescribeAirplane();
            
            Airplane3.gainAlt(4000);
            Airplane3.DescribeAirplane();
        }

        public static void main(String[] args){
            Assignment2 a = new Assignment2(null, 0, 0, 0);
        
           a.initialize();
        }
    }
