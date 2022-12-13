public class Server {
	protected String name;
	protected double preis;
	protected int hauptspeicher;
	
	public Server() {
		this.name = "unbekannt";
		this.preis = 0.0;
		this.hauptspeicher = 0;
	}
	
	public String getName() { return this.name; }
	public void setName(String name) { this.name = name; }
	public double getPreis() { return this.preis; }
	public void setPreis(double preis) { this.preis = preis; }
	public int getHauptspeicher() { return this.hauptspeicher; }
	public void setHauptspeicher(int hauptspeicher) { this.hauptspeicher = hauptspeicher; }
	
	//----------------------------------------------------------
	// Methoden
	//----------------------------------------------------------
	public String getDaten() {
		String daten = "Name: " + this.name + "\n" +
					   "Preis: " + this.preis + "\n" +
					   "Hauptspeicher: " + this.hauptspeicher;
		return daten;
	}
}
