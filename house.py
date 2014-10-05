import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z + 10.
b = block.WOOD_PLANKS

def wall(x, y, z, width, height, facing, blk):
    for w in xrange(int(width)):
        for h in xrange(int(height)):
	    if facing=='X':
                mc.setBlock(x+w, y+h, z, blk)
            elif facing=='Z':
                mc.setBlock(x, y+h, z+w, blk)

def floor(x, y, z, width, blk):
    for w in xrange(int(width)):
        for ww in xrange(int(width)):
            mc.setBlock(x+w, y, z+ww, blk)

def fourwalls(x, y, z, width, height, blk):
    wall(x, y, z, width, height, 'X', blk)
    wall(x+width, y, z, width, height, 'Z', blk)
    wall(x+width, y+height/2., z+width/8.,
        width/4., height/3., 'Z', block.GLASS) 
    wall(x+width, y+height/2., z+width/2 + width/8.,
        width/4., height/3., 'Z', block.GLASS)
    wall(x, y, z+width, width, height, 'X', blk)
    wall(x, y, z, width, height, 'Z', blk)
    wall(x, y+height/2., z+width/8.,
        width/4., height/3., 'Z', block.GLASS)
    wall(x, y+height/2., z+width/2 +width/8.,
        width/4., height/3., 'Z', block.GLASS)
    wall(x+width/3.,y,z, width/3., height/1.5, 'X', block.AIR)
 
def house(x, y, z, width, height):
    floor(x, y, z, width, block.STONE)
    fourwalls(x, y, z, width, height, b)
    floor(x, y+height, z, width, block.WOOD_PLANKS)   

house(x, y, z, 14, 6)
