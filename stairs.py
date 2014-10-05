import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z + 1.

def step(x, y, z, width, height, facing):
    half_step = int(width/2)
    for n in xrange(width):
	if facing=='X':
            mc.setBlock(x+n-half_step, y, z, block.BRICK_BLOCK)
        elif facing=='Z':
            mc.setBlock(x, y, z+n-half_step, block.BRICK_BLOCK)
        for m in xrange(int(height)):
            if facing=='X':
                mc.setBlock(x+n-half_step, y+m+1, z, block.AIR)
            elif facing=='Z':
                mc.setBlock(x, y+m+1, z+n-half_step, block.AIR)
        
def stairs(x, y, z, width, height, facing, forward):
    for n in xrange(int(height)):
	if facing=='X':
            step(x, y+n, z+n*forward, width, height, facing)
            step(x, y+n, z+(n+1)*forward, width, height, facing)
        elif facing=='Z':
            step(x+n*forward, y+n, z, width, height, facing)
            step(x+(n+1)*forward, y+n, z, width, height, facing)

def landing(x, y, z, width, height, depth, facing, forward):
    for n in xrange(int(depth)):
        if facing=='X':
            step(x, y, z+n*forward, width, height, facing)
        else:
            step(x+n*forward, y, z, width, height, facing)

def staircase(x, y, z, width, floorheight, floors, facing):
    forward = 1
    for f in xrange(0, int(floors)):
        if facing=='X':
            stairs(x, y+f*floorheight, z, width, floorheight, facing, forward)
            landing(x, y+(f+1)*floorheight, z+floorheight*forward, width, floorheight, width, facing, forward)
            facing='Z'
            z += (floorheight+width/2)*forward
        else:
            stairs(x, y+f*floorheight, z, width, floorheight, facing, forward)
            landing(x+floorheight*forward, y+(f+1)*floorheight, z, width, floorheight, width, facing, forward)
            facing='X'
            x += (floorheight+width/2)*forward
            forward=-1*forward

staircase(x, y, z, 4, 8, 5, 'X')

