
abstract class Luftfahrzeug {     
   //----------------------------------------------------------------------------------     
   // Attribute der Klasse mit entsprechenden Zugriffsmodifiern    
   //-----------------------------------------------------------------------------------
   private String bezeichnung;
   private double gewicht; 
   private int baujahr; 
   
   //--------------------------------------------------------------------------
   // Konstruktors der Klasse     
   //---------------------------------------------------------------------------     
   public Luftfahrzeug()  { 
      this.bezeichnung = "unbekannt";
      this.gewicht = 0.0;
      this.baujahr = 0;     
   } 
   
   //-----------------------------------------------------------------------------
   // Getter und Setter der Klasse     
   //-----------------------------------------------------------------------------
   public String getBezeichnung() { return this.bezeichnung; }
   public void setBezeichnung(String bezeichnung) { this.bezeichnung = bezeichnung; }
   public double getGewicht() { return this.gewicht; }
   public void setGewicht(double gewicht) { this.gewicht = gewicht; }
   public int getBaujahr() { return this.baujahr; }
   public void setBaujahr(int baujahr) { this.baujahr = baujahr;  } 
   
   //-----------------------------------------------------------------------------
   //   Methoden     
   //-----------------------------------------------------------------------------
   public abstract String getDaten(); // abstrakte Methode    
}
