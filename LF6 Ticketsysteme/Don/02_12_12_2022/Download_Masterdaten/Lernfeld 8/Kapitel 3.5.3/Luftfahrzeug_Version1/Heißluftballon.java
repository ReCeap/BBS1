public class Heißluftballon extends Luftfahrzeug {
	private double ballonVolumen;
	private double korbhöhe;
	
	public Heißluftballon() {
		this. ballonVolumen = 0.0;
		this. korbhöhe = 0.0;
	}
	
	public double getBallonVolumen() { return this.ballonVolumen; }
	public void setBallonVolumen(int ballonVolumen) { this.ballonVolumen = ballonVolumen; }
	public double getKorbhöhe() { return this.korbhöhe; }
	public void setKorbhöhe(double korbhöhe) { this.korbhöhe = korbhöhe; }

}
