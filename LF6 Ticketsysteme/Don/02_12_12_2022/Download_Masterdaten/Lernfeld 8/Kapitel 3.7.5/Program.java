public class Program {
	public static void main(String[] args) {
		MySQLConnection mySqlConnection = null;
		try {
		   mySqlConnection = new MySQLConnection();
		   mySqlConnection.create();
		   String sqlStatement = "CREATE TABLE Kontinent " +
                                 "(KontinentID INTEGER not NULL, " +
                                 " Bezeichnung VARCHAR(100), " + 
                                 " PRIMARY KEY ( KontinentID ))"; 
		   mySqlConnection.updateDB(sqlStatement);
  	       System.out.println("SQL-Anweisung erfogreich ausgeführt");
		} catch(Exception e){
		      e.printStackTrace();
		}finally {
		    if (mySqlConnection != null) { mySqlConnection.close();	}
        }
	}
}

	