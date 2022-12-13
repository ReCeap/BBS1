import java.util.*;
public class BeispielZufallszahlen {

	public static void main(String[] args) {
		int anzahlElemente = 20;
		int[] feld = new int[anzahlElemente];
		for(int i = 0; i < anzahlElemente; i++) {
		    feld[i] = (int)(Math.random() * 10); // Erzeugen der Zufallszahlen
		    System.out.println(feld[i]);
		}    
	}

}
