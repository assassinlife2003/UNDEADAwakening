
from gamelib import *

game = Game(866,487, "UNDEAD Awakening")

#Player2 Graphics
p2 = Image("p2.png",game)
p2.y = game.height - 100

#PLayer2 FirstPerson Graphics
fp = Image("fp.png",game)
fp.resizeBy(-60)

#Graphics
heal = []
for index in range(5):
    heal.append(Image("medkit.png",game,False))
    heal[index].resizeBy(-60)
for index in range(5):
    heal[index].move()
    x = randint(400,800)
    y = randint(350,400)
    heal[index].moveTo(game.width + x,y)
    heal[index].setSpeed(3,90)
    
ammo = []
for index in range(5):
    ammo.append(Image("ammo.png",game,False))
    ammo[index].resizeBy(-30)
for index in range(5):
    ammo[index].move()
    x = randint(400,800)
    y = randint(350,400)
    ammo[index].moveTo(game.width + x,y)
    ammo[index].setSpeed(3,90)

#Startup Graphics
title = Image("logo.png",game)
title.resizeBy(-20)
title.y -= 153

howtoplay = Image("howtoplay.png",game)
howtoplay.resizeBy(-30)
howtoplay.y += 180

play = Image("play.png",game)
play.resizeBy(-40)
play.y += 89

bg = Image("wave 4.png",game, False)
bg1 = Image("wave 1.png",game, False)
bg1.resizeTo(866,487)
bg2 = Image("bg1.png",game, False)
controls = Image("instructions.png",game)
controls.resizeTo(866,487)

game.setBackground(bg)

#Sounds
gun = Sound("Gun.wav", 1)

#Zombie Wave 1(Level 1)
zombie = []
for index in range(15):
    zombie.append(Image("zombie2.png",game))
    zombie[index].y = game.height - 110
    zombie[index].resizeBy(50)
    
for index in range(15):
    x = randint(200,1000)
    y = randint(350,400)
    zombie[index].moveTo(game.width + x,y)
    zombie[index].resizeBy(-60)
    zombie[index].setSpeed(2.5,90)

#Zombie Wave 2(Level 1)
zombie2 = []

for index in range(25):
    zombie2.append(Image("zombie2.png",game))
    zombie2[index].y = game.height - 110
    zombie2[index].resizeBy(50)
    
for index in range(25):
    x = randint(200,1000)
    y = randint(350,400)
    zombie2[index].moveTo(game.width + x,y)
    zombie2[index].resizeBy(-60)
    zombie2[index].setSpeed(3.5,90)

#Zombie Level 2
    
#zombie3 = Image("zombie.png",game)
#zombie3.resizeBy(-100)
zombie3 = []

for index in range(25):
    zombie3.append(Image("zombie.png",game))
    zombie3[index].y = game.height - 250
    zombie3[index].resizeBy(-60)
    
#bullets
bullet = Image("bullet.jpg",game,False)
bullet.resizeBy(-88)
bullet.rotateBy(90)
bullet.visible = False

#Startup Screen
game.over = False
while not game.over:
    game.processInput()

    game.scrollBackground("down",2)
    bg.draw()
    title.draw()
    howtoplay.draw()
    play.draw()
    
    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over = True

    if howtoplay.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
        
    game.update(30)
    
game.over = False
while not game.over:
    game.processInput()
    controls.draw()
    if mouse.LeftClick:
        game.over = True

    game.update(30)
    
#Level 1
game.over = False
zombiewave1complete = 0
zombiewave2complete = 0
ammocount = 30
while not game.over:
    game.processInput()
    bg2.draw()
    p2.draw()
    bullet.move()
    
    #Player2 Control
    if keys.Pressed[K_w]:
        p2.y -= 8
    if keys.Pressed[K_s]:
        p2.y += 8
    if keys.Pressed[K_d] and p2.right < game.width:
        p2.x += 10
    if keys.Pressed[K_a]and p2.left > 0:
        p2.x -= 10
        
    if mouse.LeftClick:
        bullet.moveTo(p2.x + 90, p2.y + 24)
        bullet.setSpeed(43,-90)
        bullet.visible = True
        ammocount -= 1


#Ammo
    for index in range(5):
        ammo[index].move()
        if ammo[index].collidedWith(p2):
            ammocount += 25
            ammo[index].visible = False

#Med Kit
    for index in range(5):
        heal[index].move()
        if heal[index].collidedWith(p2):
            p2.health += 20
            heal[index].visible = False
    
   
#ZombiesWave1
    for index in range(15):
        zombie[index].move()
        if p2.collidedWith(zombie[index]):
            p2.health -= 10
            zombiewave1complete += 1
        if bullet.collidedWith(zombie[index]):
            zombie[index].visible = False
            bullet.visible = False
            zombiewave1complete += 1

#ZombiesWave2                
    if zombiewave1complete == 15:
        for index in range(25):
            zombie2[index].move()
            if bullet.collidedWith(zombie2[index]):
                zombie2[index].visible = False
                bullet.visible = False
                zombiewave2complete += 1
            if p2.collidedWith(zombie2[index]):
                p2.health -= 20
                zombie2[index].visible = False
                zombiewave2complete += 1
                
    if zombiewave2complete == 25:
        game.over = True
       
    if p2.health < 1:
        game.over = True
        
    game.drawText("Health: " + str(p2.health),p2.x - 20,p2.y - 100,Font(white,24,black))
    game.drawText("Ammo: " + str(ammocount),p2.x - 10,p2.y + 80,Font(white,24,black))

    game.update(30)
#Level 2
game.over = False
zombielevel2complete = 0
ammocount = 30
bullet.rotateBy(270)
while not game.over:
    game.processInput()
    bg1.draw()
    bullet.move()

#zombie Level 2
    for index in range(25):
        zombie3[index].move()
        zombie3[index].resizeBy(1.5)
  
#Player2 FirstPerson Graphics
    fp.moveTo(mouse.x,390)

    if mouse.LeftClick:
        bullet.moveTo(fp.x,fp.y)
        bullet.setSpeed(43,360)
        bullet.visible = True
        ammocount -= 1

    if bullet.collidedWith(zombie3[index]):
        zombie3[index].visible = False
        zombielevel2complete += 1

    if zombielevel2complete == 25:
        game.over = True
        
    if p2.health < 1:
        game.over = True
        
    #game.drawText("Health: " + str(p2.health),p2.x - 20,p2.y - 100,Font(white,24,black))
    #game.drawText("Ammo: " + str(ammocount),p2.x - 10,p2.y + 80,Font(white,24,black))
    game.update(30)
