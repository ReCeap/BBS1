import java.util.*;
public class BeispielEinUndAusgabe {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("Geben Sie bitte ihren Namen ein");
		String name = input.nextLine();
		System.out.println("Geben Sie bitte ihr Alter ein");
		int alter = input.nextInt();
		System.out.println("Geben Sie bitte Ihre K�rpergr��e ein");
		double groesse = input.nextDouble();
		System.out.println("Sie hei�en " + name + ", sind " + alter +
		                   " Jahre alt und sind " + groesse + " gro�.");
		input.close();
	}

}
