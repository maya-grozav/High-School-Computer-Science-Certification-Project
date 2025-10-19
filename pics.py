from numpy import delete
import pygame.image as p

st = [p.load("assets/standingl.png"),p.load("assets/standingr.png")]
wk = [p.load("assets/right1.png"), p.load("assets/right2.png"), p.load("assets/left1.png"), p.load("assets/left2.png")]
jp = [p.load("assets/jumpingr.png"), p.load("assets/jumpingl.png")]
k = [p.load("assets/king-face.png"), p.load("assets/king.png")]
g = p.load("assets/ground.png")
b = p.load("assets/box.png")
y = [p.load("assets/yay-1.png"), p.load("assets/yay-2.png")]
birds = [p.load("assets/birds1.png"), p.load("assets/birds2.png")]
little_prince_flying = p.load("assets/flying.png")
items = []
for i in range(1, 4):
    gold = p.load(f"assets/gold-{i}.png")
    items.append(gold)
bg_images = [],[]
for i in range(2):
    for j in range(1, 4):
        bg_image = p.load(f"assets/bg{j}-{i}.png")
        bg_images[i].append(bg_image)
bg_width = bg_image.get_width()
