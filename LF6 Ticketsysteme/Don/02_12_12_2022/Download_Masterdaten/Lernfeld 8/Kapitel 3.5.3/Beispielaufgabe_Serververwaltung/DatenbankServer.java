public class DatenbankServer extends Server {
	private String dbms;
	
	public DatenbankServer() {
		this.dbms = "unbekannt";
	}
	public String getDBMS() { return this.dbms; }
	public void setDBMS(String dbms) { this.dbms = dbms; }
}
