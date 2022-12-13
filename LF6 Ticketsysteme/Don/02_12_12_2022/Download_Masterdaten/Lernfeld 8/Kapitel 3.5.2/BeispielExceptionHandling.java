import java.util.*;
public class BeispielExceptionHandling {

	public static void main(String[] args) {
		try {
			Scanner input = new Scanner(System.in);
			System.out.println("Geben Sie bitte eine ganze Zahl ein");
			int zahl = input.nextInt();
			System.out.println("Sie haben eine " + zahl + " eingegeben");
		} catch (Exception ex) {
			System.out.println("Es ist ein Fehler aufgetreten " + ex);
		} finally {
			System.out.println("Das Programm wird beendet");
		}

	}

}
