public class ProxyServer extends Server {
	private String protokoll;
	
	public ProxyServer() {
		this.protokoll = "unbekannt";
	}
	
	public String getProtokoll() { return this.protokoll; }
	public void setProtokoll(String protokoll) { this.protokoll = protokoll; }
}
