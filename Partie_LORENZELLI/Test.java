public class Test{
  public static void main(String[] args){
    RubbiksCube r = new RubbiksCube();
    r.initiTab();
    r.affichage();
    r.rightMovement();
    for (int i = 0; i < 6; i++){
      r.affichage(i);
    }
  }
}
