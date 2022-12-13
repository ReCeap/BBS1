	
public class Program {
	public static void main(String[] args) {
		Luftfahrzeug beispielLuftfahrzeug = new Luftfahrzeug();
		beispielLuftfahrzeug.setBezeichnung("A310");
		beispielLuftfahrzeug.setGewicht(71840);
		beispielLuftfahrzeug.setBaujahr(1995);		
		System.out.print(beispielLuftfahrzeug.getDaten());
	}
}
