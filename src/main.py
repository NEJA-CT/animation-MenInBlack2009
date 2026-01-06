import pyxel

W, H = 160, 120


# initial position and velocity
x, y = W // 10, 15
vx, vy = 0, 0


SPEED = 0.2
GRAVITY = 0.3
BOUNCE = 0.5


def update():
   global x, y, vx, vy

   vy += GRAVITY

   x += vx

   y += vy

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
      vy = vy - 5
      y += vy

   if pyxel.btnp(pyxel.KEY_S):
      vy = vy + 5
      y += vy

   if pyxel.btnp(pyxel.KEY_A):
      vx = vx - 5
      x += vx
   if pyxel.btnp(pyxel.KEY_D):
      vx = vx + 5
      x += vx

   if pyxel.btnp(pyxel.KEY_UP):
      vy = vy - 5
      y += vy

   if pyxel.btnp(pyxel.KEY_DOWN):
      vy = vy + 5
      y += vy

   if pyxel.btnp(pyxel.KEY_LEFT):
      vx = vx - 5
      x += vx
   if pyxel.btnp(pyxel.KEY_RIGHT):
      vx = vx + 5
      x += vx




def draw():
   pyxel.cls(0)
   pyxel.circ(x, y, 9, 1)

pyxel.init(W,H, title="fun")
pyxel.run(update,draw)