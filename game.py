# Fill me in!
app.background = gradient('midnightBlue', 'navy', 'black', start='bottom')
#Backround Of Space
Star(20, 50, 5, 8, fill='gold', roundness=40)
Star(280, 30, 5, 5, fill='gold')
Oval(175,80,20,10, fill=None, border='gold',borderWidth=3, rotateAngle = -35)
Star(340, 150, 5, 5, fill='gold')
Star(50, 350, 5, 8, fill='white', roundness=40)
Star(250, 220, 5, 5, fill='white')
Star(380, 380, 5, 5, fill='white')
Star(75, 100, 5, 8, fill='gold', roundness=40)
Star(80, 210, 5, 8, fill='white', roundness=40)
Circle(175, 80, 5, fill=gradient('red','white',start='bottom'))
Oval(168,300,25,18, fill=None, border='gold',borderWidth=3, rotateAngle = +35)
Circle(170, 298, 8, fill=gradient('blue','white', start='top'))
#Spaceship
Ship = Group (Polygon(110,200,135,215,110,215, fill=gradient('deepSkyBlue','lightBlue')),
Polygon(110,215,110,230,135,215,fill=gradient('whiteSmoke','darkGrey')),
Polygon(85,195,110,200,110,230,85,230,fill=gradient('whiteSmoke','darkGrey')),
Rect(0,195,85,35,fill=gradient('whiteSmoke','darkGrey')),
Polygon(30,215,65,215,5,245,fill='darkGrey')


)
#Define "Finishgame"
def finishGame(message):
    Label(message, 200, 200, fill='darkRed', size=40, bold=True)
    app.stop()
def WinGame(message):
    Label(message, 200, 200, fill='darkGreen', size=40, bold=True)
    app.stop()
#Obstacles
Asteroid = Circle(400,200,20,fill=gradient('black','grey', start='right'))
Star = Star(400,100,10,5,fill='yellow')
Debris = Polygon(382,239,400,250,383,261,365,257, fill='grey')

#Make the Obstacles In motion
Star.dx=14
Asteroid.dx=10
Debris.dx=16
def onStep():
    Asteroid.centerX-=Asteroid.dx
    if (Asteroid.right<0):
        Asteroid.left=400
        Asteroid.centerY=randrange(0,400)
        
    Star.centerX-=Star.dx
    if (Star.right<0):
        Star.left=400
        Star.centerY=randrange(0,400)
        
    Debris.centerX-=Debris.dx
    if (Debris.right<0):
        Debris.left=400
        Debris.centerY=randrange(0,400)
        
    
       #Make the counter go up
    if(Asteroid.hitsShape(Score) == True):
        label.value += 1
        #Make the game stop when the obstacles hit the ship
    if(Asteroid.hitsShape(Ship) == True):
        finishGame('(>_<) Game over')
        
    if(Star.hitsShape(Ship) == True):
        finishGame('(>_<) Game over')
        
    if(Debris.hitsShape(Ship) == True):
        finishGame('(>_<) Game over')
        
   
        
    
    
        
        
#Make The counter go up 
label = Label(0,200,25, font='arial',size=20, fill='white')
Score = Rect(-39,-39,1,400)

#Make the Ship move 
def onKeyHold(keys):
    if ('up' in keys):
        Ship.centerY -= 10
    elif ('down' in keys):
        Ship.centerY += 10
        

#Dont let the Ship touch the border  #(Ship.centerY <= 0): 
    if (Ship.centerY <=0):
        Ship.centerY +=20
        
    if (Ship.centerY >= 400):
        Ship.centerY -=20
         
#Make the game win
    if (label.value >= 20):
        WinGame('^_^ You Win')
        
