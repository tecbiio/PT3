public class Face{

  /** Entier permettant le swap entre deux valeur sans utiliser de tmp */
  private int color;
  /** String représentant une couleur */
  private String type;

  public Face(int color){
    this.color = color;
  }

  public int getColor(){
    return color;
  }

  public void setColor(int color){
    this.color = color;
  }

  public String getType(){
    return type;
  }

  public void setType(String type){
    this.type = type;
  }

  public String toString(){
    return ""+color+":"+type;
  }
}
