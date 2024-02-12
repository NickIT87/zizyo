from mcpi.minecraft import Minecraft

# Specify the Minecraft server address and port
# mc = Minecraft.create(address='localhost', port=4711)
mc = Minecraft.create(address='localhost', port=4711)

mc.postToChat("Привет, Minecraft!")

# player_pos = mc.player.getTilePos()
# mc.postToChat(f"Позиция игрока: {player_pos}")

# for i in range(10):
#     print(player_pos)


# from mcpi.minecraft import Minecraft
# from time import sleep

# mc = Minecraft.create(address="localhost", port=4711)

# # Constantly grab the player's position and create
# # a new stone block underneath him/her
# while True:
#     x,y,z = mc.player.getPos()

#     # Debug
#     print("x: {}, y: {}, z: {}".format(x,y,z))
    
#     mc.setBlock(x,y-1,z,1)
#     sleep
