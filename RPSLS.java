import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom;

public class RPSLP {

    private static int name_to_number(String name) {
        if (name.equals("rock")) {
            return (0);
        } else if (name.equals("spock")) {
            return (1);
        } else if (name.equals("paper")) {
            return (2);
        } else if (name.equals("lizard")) {
            return (3);
        } else if (name.equals("scissors")) {
            return (4);
        }else{
            return (0000000);
        }
    }

    public static String number_to_name(int number) {
        if (number == 0) {
            return ("rock");
        } else if (number == 1) {
            return ("spock");
        } else if (number == 2) {
            return ("paper");
        } else if (number == 3) {
            return ("lizard");
        } else if (number == 4) {
            return ("scissors");
        } else {
            return("error");
        }
    }

    public static void main(String [] args) {

        Scanner reader = new Scanner(System.in);

        String player_name = reader.nextLine();

        int player_number = name_to_number(player_name);

        int comp_number = ThreadLocalRandom.current().nextInt(0, 5);

        System.out.println("Computer chooses " + number_to_name(comp_number));

        System.out.println("Player Chooses " + player_name);


        if ((comp_number - player_number) % 5 == 1 || (comp_number - player_number) % 5 == -1) {
            System.out.println("Computer Wins!");
        } else if (((comp_number - player_number) % 5 == 2) || ((comp_number - player_number) % 5 == -2)) {
            System.out.println("Computer Wins!");
        } else if (((comp_number - player_number) % 5 == 3) || ((comp_number - player_number) % 5  == -3)) {
            System.out.println("Player Wins!");
        } else if (((comp_number - player_number) % 5 == 4) || ((comp_number - player_number) % 5 == -4)) {
            System.out.println("Player Wins!");
        } else {
            System.out.println("Computer and Player tie!");
        }
    }
}
