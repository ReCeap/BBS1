	
public class Program {
	public static void main(String[] args) {
		System.out.println("Beispielflugzeug");
		Flugzeug f = new Flugzeug();
		f.setBezeichnung("A310");
		f.setGewicht(71840);
		f.setBaujahr(1995);
		f.setSpannweite(43.90);
		f.setAnzahlMotoren(2);
		System.out.print(f.getDaten());
		System.out.println("\n");
		System.out.println("Beispielheiﬂluftballon");
		Heiﬂluftballon b = new Heiﬂluftballon();
		b.setBezeichnung("Ultra Magic");
		b.setGewicht(478.5);
		b.setBaujahr(2018);
		b.setBallonVolumen(4000);
		b.setKorbhˆhe(1.10);
		System.out.print(b.getDaten());
	}
}
