public class RubbiksCube{

  /** Tableau représentant les couleurs d'un RubbiksCube */
  private static Face[][][] tab;

  public RubbiksCube(){
    this.tab = new Face[6][3][3];
  }
  /** Initialisation d'un tableau avec ses 6 faces et ses 9 couleurs par face
      On construit un RubbiksCube résolu pour être sûr qu'après mélange, il soit
      solvable */
  public void initiTab(){
    for (int i = 0; i < 6; i++){
      for (int j = 0; j < 3; j++){
        for (int k = 0; k < 3; k++){
          tab[i][j][k] = new Face(i);
          if (i == 0)
            tab[i][j][k].setType("Bleu");
          if (i == 1)
            tab[i][j][k].setType("Orange");
          if (i == 2)
            tab[i][j][k].setType("Vert");
          if (i == 3)
            tab[i][j][k].setType("Rouge");
          if (i == 4)
            tab[i][j][k].setType("Blanc");
          if (i == 5)
            tab[i][j][k].setType("Jaune");
        }
      }
    }
  }

  /** Les mouvements sont définis avec la face 0 en face de soi et avec
      des rotations dans le sens horaire (InverseMovement) pour le sens
      antihoraire */
  public void rightMovement(){
    // rotation cote droit
    // sauvegarde cote droit face 0
    Face tmp1 = tab[0][2][0];
    Face tmp2 = tab[0][2][1];
    Face tmp3 = tab[0][2][2];
    // cote droit face 5 sur cote droit face 0
    tab[0][2][0] = tab[5][2][0];
    tab[0][2][1] = tab[5][2][1];
    tab[0][2][2] = tab[5][2][2];
    // cote droit face 2 sur cote droit face 5
    tab[5][2][0] = tab[2][2][0];
    tab[5][2][1] = tab[2][2][1];
    tab[5][2][2] = tab[2][2][2];
    // cote droit face 4 sur cote droit face 2
    tab[2][2][0] = tab[4][2][0];
    tab[2][2][1] = tab[4][2][1];
    tab[2][2][2] = tab[4][2][2];
    // cote droit face 0 sur cote droit face 4
    tab[4][2][0] = tmp1;
    tab[4][2][1] = tmp2;
    tab[4][2][2] = tmp3;
    // rotation de la face 1
    // sauvegarde cote haut face 1
    tmp1 = tab[1][0][0];
    tmp2 = tab[1][1][0];
    tmp3 = tab[1][2][0];
    // cote gauche face 1 sur cote haut face 1
    tab[1][0][0] = tab[1][0][2];
    tab[1][1][0] = tab[1][0][1];
    tab[1][2][0] = tmp1;
    // cote bas face 1 sur cote gauche face 1
    tab[1][0][1] = tab[1][1][2];
    tab[1][0][2] = tab[1][2][2];
    // cote droit face 1 sur cote bas face 1
    tab[1][1][2] = tab[1][2][1];
    tab[1][2][2] = tmp3;
    // cote droit avec la sauvegarde
    tab[1][2][1] = tmp2;
  }
  // fonction qui effectue une rotation avec en parametre l'indice de la face
  // la couleur du carre au milieu definit la couleur de la face
  /**
  public void abstract rightInverseMovement();
  public void abstract leftMovement();
  public void abstract leftInverseMovement();
  public void abstract upMovement();
  public void abstract upInverseMovement();
  public void abstract downMovement();
  public void abstract downInverseMovement();
  public void abstract frontMovement();
  public void abstract frontInverseMovement();
  public void abstract behindMovement();
  public void abstract behindInverseMovement();
  */
  public static void affichage(){
    for (int i = 0; i < 6; i++){
      for (int j = 0; j < 3; j++){
        for (int k = 0; k < 3; k++){
          System.out.println("i= "+i+", j= "+j+", k= "+k+" "+tab[i][k][j]);
        }
      }
    }
  }

  public static void affichage(int i){
    for (int j = 0; j < 3; j++){
      System.out.println("------------");
      for (int k = 0; k < 3; k++){
        System.out.print("|");
        System.out.print(tab[i][k][j]);
      }
      System.out.println("|");
    }
    System.out.println("------------");
  }
}
