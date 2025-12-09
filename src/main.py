import pyxel

W, H = 160, 120


# initial position and velocity
x, y = W // 10, 15
vx, vy = 0, 0


SPEED = 0.2
GRAVITY = 0.3
BOUNCE = vx/2


def update():
   global x, y, vx, vy

   # Apply gravity
   vy += GRAVITY
   y += vy
  
   if x <= 60:
      vx += SPEED
      x += vx
   else:
       vx += SPEED
       x -= vx 

   if y >= 60:
       vy += SPEED
       y += vy
   else:
       vy += SPEED
       y -= vy

   # Bounce when hitting the ground
   ground = H - 5
   if y > ground:
       y = ground
       vy = -vy * BOUNCE  # reverse and lose some energy

   walls = W - 5
   if x > walls:
         x = walls
         vx = -vx * BOUNCE

   if x < 3:
      x = 3
      vx = -vx * BOUNCE

   ceiling = 5
   if y < ceiling:
       y = ceiling
       vy = -vy * BOUNCE



   if pyxel.btnp(pyxel.KEY_W):
      vy = -vy - 1
   
   if pyxel.btnp(pyxel.KEY_S):
      vy = vy + 1

   if pyxel.btnp(pyxel.KEY_A):
      vx = -vx - 50
      x += vx
   if pyxel.btnp(pyxel.KEY_D):
      vx = vx + 1
      x += vx






def draw():
   pyxel.cls(0)
   pyxel.circ(x, y, 9, 1)

pyxel.init(W,H, title="fun")
pyxel.run(update,draw)