import java.sql.ResultSet;

...

   ResultSet rs = sqlStatement.executeQuery("SECECT O.Name, O.Einwohner, L.Name " +
			                                 "FROM Ort O INNER JOIN Land L ON O.LandID = L.LandID");
	while (rs.next()) {
		String ortsName = rs.getString("Name");
		int anzahlEinwohner = rs.getInt("Einwohner");
		String landName = rs.getString("Name");
		// Ausgabe der Werte
		System.out.format("%s, %s, %s\n", ortsName, anzahlEinwohner, landName);
	}
...
