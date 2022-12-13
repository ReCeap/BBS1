import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;


public class MySQLConnection{
 private Connection con = null;
 private Statement sqlStatement = null;
 private String dbHost = "localhost";	     // Hostname
 private String dbPort = "3306";		     // Port -- Standard: 3306
 private String dbName = "Ortverwaltung";	 // Datenbankname
 private String dbUser = "user";		     // Datenbankuser
 private String dbPass = "password";		 // Datenbankpasswort
 
 
 public void create()
 {
		try {
			// Datenbanktreiber für JDBC Schnittstellen laden.
			Class.forName("com.mysql.jdbc.Driver");	
			// Verbindung zur JDBC-Datenbank herstellen.
			con = DriverManager.getConnection("jdbc:mysql://"+dbHost+":"+ dbPort+"/"+dbName+"?"+"user="+dbUser+"&"+"password="+dbPass);
			sqlStatement = con.createStatement();
			System.out.println("Verbindung erfolgreich hergestellt.");
		} catch (ClassNotFoundException e) {
			System.out.println("Verbindung nicht möglich.");
		} catch (SQLException e) {
			System.out.println("Verbindung nicht moglich");
			System.out.println("SQLException: " + e.getMessage());
	        System.out.println("SQLState: " + e.getSQLState());
	        System.out.println("VendorError: " + e.getErrorCode());
		}
 }

public void close() {
	 try {
	   if (sqlStatement != null) { sqlStatement.close(); }
	   if (con != null) { 
		    con.close(); 
		    System.out.println("Datenbankverbindung beendet");
	   }
	   
	 } catch (SQLException e) {
		 System.out.println("SQLException: " + e.getMessage());
	        System.out.println("SQLState: " + e.getSQLState());
	        System.out.println("VendorError: " + e.getErrorCode());
	 }
	 
 }

public void updateDB(String sql) {
	 try {
		   sqlStatement.executeUpdate(sql);
		 } catch (SQLException e) {
			 System.out.println("SQLException: " + e.getMessage());
		        System.out.println("SQLState: " + e.getSQLState());
		        System.out.println("VendorError: " + e.getErrorCode());
		 }
 }
 
public ResultSet getData(String sql) {
	 try {
		   return sqlStatement.executeQuery(sql);
		 } catch (SQLException e) {
			 System.out.println("SQLException: " + e.getMessage());
		        System.out.println("SQLState: " + e.getSQLState());
		        System.out.println("VendorError: " + e.getErrorCode());
		        return null;
		 }
 }
 
 
 
}