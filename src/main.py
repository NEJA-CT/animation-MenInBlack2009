import pyxel


SPEED = 0.2
GRAVITY = 0.3
BOUNCE = 0.7
W, H = 160, 120

# initial position and velocity
x, y = W // 2, H // 2
vx, vy = 0, 0

def update():
   global x, y, vx, vy

   # Apply gravity
   vy += GRAVITY
   y += vy
  
   if x < 100 or x > 110:
      vx += SPEED
      x += vx
   else:
       vx -= SPEED
       x += vx

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

def draw():
   pyxel.cls(0)
   pyxel.circ(x, y, 9, 1)



pyxel.init(W,H, title="fun")
pyxel.run(update,draw)