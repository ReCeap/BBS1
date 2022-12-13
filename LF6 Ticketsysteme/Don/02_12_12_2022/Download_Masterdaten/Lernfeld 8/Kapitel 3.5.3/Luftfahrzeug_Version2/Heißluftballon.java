public class Hei�luftballon extends Luftfahrzeug {
	private double ballonVolumen;
	private double korbh�he;
	
	public Hei�luftballon() {
		this. ballonVolumen = 0.0;
		this. korbh�he = 0.0;
	}
	
	public double getBallonVolumen() { return this.ballonVolumen; }
	public void setBallonVolumen(int ballonVolumen) { this.ballonVolumen = ballonVolumen; }
	public double getKorbh�he() { return this.korbh�he; }
	public void setKorbh�he(double korbh�he) { this.korbh�he = korbh�he; }
	
	public String getDaten() {
		String daten = "Bezeichnung: " + this.bezeichnung + "\n" +
		"Gewicht: " + this.gewicht + " kg \n" +
		"Baujahr: " + this.baujahr + "\n" +
		"Volumen des Ballons: " + this.ballonVolumen + " m3\n" +
		"Korbh�he: " + this.korbh�he + " m";
		return daten;
	}
}
