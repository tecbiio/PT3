import RubiksCube
import Movement

# Test constructeur
cube = RubiksCube()
print(cube.tab)

# Test getter
tab2 = cube.get_tab()
print(tab2)

# Test Attribution des valeurs par coordonnées en local
cube.tab[0,2,1] = 5
print(cube.tab)

# Test setter
tab3 = np.zeros((6,3,3))
cube.set_tab(tab3)
print(cube.tab)

# Test movement
move = Movement()
