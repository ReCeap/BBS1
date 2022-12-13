public class Flugzeug extends Luftfahrzeug {
	private double spannweite;
	private int motorenAnzahl;
	
	public Flugzeug() {
		this.spannweite = 0.0;
		this.motorenAnzahl = 0;
	}
	
	public double getSpannweite() { return this.spannweite; }
	public void setSpannweite(double spannweite) { this.spannweite = spannweite; }
	public int getAnzahlMotoren() { return this.motorenAnzahl; }
	public void setAnzahlMotoren(int motorenAnzahl) { this.motorenAnzahl = motorenAnzahl; }

}
