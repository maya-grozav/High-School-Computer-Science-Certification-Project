import pygame, constants as c, pics as p, math

def find_x(hmi, items, W):
    for i in range(hmi + 1):
        if W / 2 - 50 <= items[0][i] <= W / 2 + 50 and items[2][i]:
            return i
    return -1

def pick_up(x,it,inv):
    it[2][x] = 0
    inv += 1
    return it, inv

def give(to_give, to_get, max):
    while to_give and (to_get < max):
        to_get += 1
        to_give -= 1
    return to_give, to_get

def convert_into_rows_beta(x,k,text):
    isit = 0
    if x > len(text) - k - 1:
        x = len(text) - k - 1
    q = k + x 
    for i in range(k+1, k + x + 1):
        if text[i] == " " or i == len(text) - 1:
            q = i
    if q == len(text) - 1:
        isit = 1
    if k:
        k += 1
    if isit:
        return q, text[k:q+1], isit
    else:
        return q, text[k:q], isit

def convert_into_rows(text, max):
    x =[]
    hm = 0
    k = 0
    isit = 0
    while not isit:
        hm += 1
        k, t1, isit = convert_into_rows_beta(max,k,text)
        x.append(t1)
    hm_on_row, maxk = hm_chars_on_row(x)
    return x, hm_on_row, maxk

def hm_chars_on_row(rows):
    x = []
    max = 0
    for i in rows:
        x.append(len(i) - 1)
        max += len(i) - 1
    return x, max
def what_letters_do_i_display(main_k,chars_on_row, rows, max):
    x= []
    k = 0
    isit = 0
    poz = 0
    while k < main_k and poz < len(rows):
        if  k + chars_on_row[poz] >= main_k:
            x.append(rows[poz][:main_k - k+1])
        else:
            x.append(rows[poz][:chars_on_row[poz]+1])
        k += chars_on_row[poz]
        poz += 1
    if main_k == max:
        isit = 1
    return x, isit

def talk(screen, letters, face):
    pygame.draw.rect(screen, (0, 0, 0), (c.bubble_x - 5, c.bubble_y - 5, c.bubble_w + 10, c.bubble_h + 10))
    pygame.draw.rect(screen, (255, 255, 255), (c.bubble_x, c.bubble_y, c.bubble_w, c.bubble_h))
    rect = face.get_rect(center=(c.facey, c.facex))
    font = pygame.font.Font("assets/kongtext.ttf", 30)
    screen.blit(face, rect)
    for i in range(len(letters)):
        len_row = len(letters[i])
        line_1 = font.render(letters[i], True, (0, 0, 0))
        rect_1 = line_1.get_rect(center = (240 + c.king_padding + len_row*15, i*50 + 125))
        screen.blit(line_1, rect_1)
def display_text(screen, text):
    font = pygame.font.Font("assets/kongtext.ttf", 30)
    text_font = font.render(text, True, (255, 255, 255))
    text_rect = text_font.get_rect(center = (c.WIDTH // 2, c.HEIGHT // 2 + 80))
    screen.blit(text_font, text_rect)
def initialize_items():
    import random
    items = [], [], [] #0 - coords; 1 - pic; 2 - valid
    pics = []
    for i in p.items:
        pics.append(i.convert_alpha())
    item_height = pics[0].get_height()
    item_width = pics[0].get_width()
    for i in range(c.hm_items + 1):
        random_number = random.randint(1, 300)
        items[0].append(c.item_starting_point + c.starting_point + c.distance * i + random_number)
        r = i % len(p.items)
        items[1].append(p.items[r])
        items[2].append(1)
        
    return items
def manage_items(screen, items, ground_height):
    item_height = items[1][0].get_height()
    for i in range(len(items[1])):
        if items[2][i]:
            screen.blit(items[1][i], (items[0][i], c.HEIGHT - ground_height - item_height + 10))
            if c.WIDTH / 2 - 50 <= items[0][i] <= c.WIDTH / 2 + 50 and i < 2:
                    display_text(screen, c.instructions[1])

def draw_bg(screen, bg_images, bg_i, bg_width):
    for i in range(30):
        speed = 0.1
        for j in bg_images[bg_i]:
            screen.blit(j, ((i * bg_width) + c.starting_point - c.scroll * speed, 0))
            speed += 0.1

def inventory(screen, inventory):
    font = pygame.font.Font("assets/kongtext.ttf", 20)
    text = "Inventory"
    title_font = font.render(text, True, c.title_color)
    title_rect = title_font.get_rect(x = c.inventory_x, y = c.inventory_y)
    screen.blit(title_font, title_rect)
    for i in len(inventory):
        if not inventory[i][1]:
            inventory.remove(inventory[i])
    for i in len(inventory):
        rect = inventory[i][0].get_rect(x = c.inventory_padding * (i + 1) + i * p.b.get_width, y = c.inventory_padding * 2 + title_font.get_height)

def invent(screen, inventory):
    font20 = pygame.font.Font("assets/kongtext.ttf", 20)
    text = "Inventory"
    text_font = font20.render(text, True, (255, 255, 255))
    text_rect = text_font.get_rect(x = c.padding_x, y = c.padding_y)
    screen.blit(text_font, text_rect)
    inv_box = p.b.get_rect(x = c.padding_x * 2, y = c.padding_y * 2 + text_font.get_height())
    screen.blit(p.b, inv_box)
    if inventory > 0:
        rect = p.items[1].get_rect(x = c.padding_x * 2 + c.box_border, y = c.padding_y * 2 + c.box_border + text_font.get_height())
        screen.blit(p.items[1], rect)
        how_many = str(inventory)
        how_many_font = font20.render(how_many, True, (255, 255, 255))
        text_rect = how_many_font.get_rect(x = c.padding_x + p.b.get_width(), y = c.padding_y * 2 + p.b.get_height() + text_font.get_height())
        screen.blit(how_many_font, text_rect)

def draw_ground(screen, ground_image, run):
    ground_width = ground_image.get_width()
    ground_height = ground_image.get_height()
    for i in range(50):
        screen.blit(ground_image,((i * ground_width) + c.starting_point - 700 - c.scroll * run, c.HEIGHT - ground_height))

def change_animation_coords(rect1, rect2):
    if rect1.x < c.WIDTH / 2 + 10 and rect1.y < c.HEIGHT - p.g.get_height() - p.little_prince_flying.get_height() + 10:
        rect1.x += 1
        rect1.y = rect1.x+100*math.sin(rect1.x/72)
        rect2.x = rect1.x +85
        rect2.y = rect1.y -150
    else:
        rect2.x += 1
        rect2.y -= 2
    return rect1, rect2

def create_button(text, y):
    font20 = pygame.font.Font("assets/kongtext.ttf", 20)

    rect1 = pygame.Rect(c.button_x - 5, y * c.button_y - 5, c.button_w + 10, c.button_h + 10)
    rect2 = pygame.Rect(c.button_x, y * (c.button_y), c.button_w, c.button_h)
    text_font = font20.render(text, True, c.bg_color)
    text_rect = text_font.get_rect(x = c.button_x + c.button_w / 2 - text_font.get_width() / 2, y = y * c.button_y + c.button_h / 2 - text_font.get_height() / 2)
    button = [(0, 0, 0), rect1, (255, 255, 255), rect2, text_font, text_rect]
    return button

def draw_button(screen, button):
    pygame.draw.rect(screen, button[0], button[1])
    pygame.draw.rect(screen, button[2], button[3])
    screen.blit(button[4],button[5])

def button_click(x, y, rect):
    rx, ry, rw, rh = rect
    return rx <= x <= rx + rw and ry <= y <= ry + rh
