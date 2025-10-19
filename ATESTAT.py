import pygame, sys, constants as c, functions as f, pics as p
pygame.init()
screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
pygame.display.set_caption("The little game")

clock = pygame.time.Clock()
CHANGE500 = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE500, 500)
CHANGE1000 = pygame.USEREVENT + 2
pygame.time.set_timer(CHANGE1000, 1000)
TALKING = pygame.USEREVENT + 3
pygame.time.set_timer(TALKING, 50)
display_find_npc = pygame.USEREVENT + 4
FLY = pygame.USEREVENT + 5
pygame.time.set_timer(FLY, 20)
ANIMATION = pygame.USEREVENT + 6

font20 = pygame.font.Font("assets/kongtext.ttf", 20)
font = pygame.font.Font("assets/kongtext.ttf", 30)
title_font = pygame.font.Font("assets/kongtext.ttf", 50)

level = 0

ground_image = p.g.convert_alpha()
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()

bg_i = 0

initialized = False

while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    if level == 0:
        if not initialized:
            font = title_font.render(c.title, True, c.title_color)
            title_rect = font.get_rect(center = (c.WIDTH // 2, c.HEIGHT // 4))
            little_princes_planet = pygame.image.load("assets/planet.png")
            the_little_princes_planet = little_princes_planet.get_rect(center = (c.WIDTH, c.HEIGHT))
            text_font = font20.render(c.instructions[0], True, (255, 255, 255))
            text_rect = text_font.get_rect(center = (c.WIDTH // 2, c.HEIGHT // 2 + 80))
            flying_rect = p.little_prince_flying.get_rect(x=-100, y=-70)
            fly_pic = p.little_prince_flying
            k = 0
            rot = 0
            rot_speed = 0.2
            is_the_animation_on = False
            initialized = True
            bird_pic = p.birds[0]
            birds_rect = p.birds[0].get_rect(x=-100, y=-220)

        screen.fill(c.bg_color)
        f.draw_bg(screen, p.bg_images, bg_i, p.bg_width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == CHANGE1000:
                bg_i = (bg_i + 1) % 2
            if event.type == CHANGE500:
                k = (k + 1) % 2
                title_rect.y += 5*pow(-1,k)
                bird_pic = p.birds[k]
            if event.type == FLY:
                if is_the_animation_on:
                    if flying_rect.x == 449:
                        fly_pic = p.st[1]
                    flying_rect, birds_rect = f.change_animation_coords(flying_rect, birds_rect)
            if event.type == pygame.KEYDOWN:
                is_the_animation_on = True
            if is_the_animation_on and birds_rect.x >=800:
                is_the_animation_on = False
                level += 1
                initialized = False

        if is_the_animation_on:
            f.draw_ground(screen, p.g,1)
            screen.blit(fly_pic, flying_rect)
            screen.blit(bird_pic, birds_rect)
        else:
            screen.blit(font, title_rect)
            screen.blit(text_font, text_rect)
            old_center = the_little_princes_planet.center  
            rot = (rot + rot_speed) % 360  
            new_image = pygame.transform.rotate(little_princes_planet , rot)  
            the_little_princes_planet = new_image.get_rect(center = old_center)
            screen.blit(new_image , the_little_princes_planet)  

    if level == 1:
        if not initialized:
            pygame.time.set_timer(display_find_npc, 5000)
            do_i_display_find_king = 1
            is_the_king_speaking = 0
            walking = 0
            rows = []
            letters = []
            main_lines_done = [0,0]
            items = f.initialize_items()
            standing, walkingr, walkingl, jumping = [p.st[0].convert_alpha(),p.st[1].convert_alpha()], [p.wk[0].convert_alpha(), p.wk[1].convert_alpha()], [p.wk[2].convert_alpha(), p.wk[3].convert_alpha()], [p.jp[0].convert_alpha(), p.jp[1].convert_alpha()]
            player = walkingr[1].get_rect(center = (c.WIDTH // 2, c.HEIGHT - ground_image.get_height() + 20))
            king_face = p.k[0].convert_alpha()
            king = p.k[1].convert_alpha()
            box = p.b.convert_alpha()
            speed = 0
            jump_height = -12
            gravity = 0.6
            on_ground = False
            dis = 2
            isit = 0
            max_k = 0
            main_k = 0
            chars_on_row = []
            run = 1
            inventory = 0
            king_inventory = 0
            char_image = 0
            direction = 0
            NPC = king.get_rect()
            NPC.x = c.WIDTH // 6 + c.starting_point 
            NPC.y = c.HEIGHT - ground_image.get_height() - p.k[1].get_height() + 20
            initialized = True
        
        walking = 0
        screen.fill(c.bg_color)
        f.draw_bg(screen, p.bg_images, bg_i, p.bg_width)
        f.draw_ground(screen, ground_image, run)
        f.invent(screen, inventory)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == CHANGE500:
                char_image = (char_image + 1) % 2
            elif event.type == CHANGE1000:
                bg_i = (bg_i + 1) % 2
            elif event.type == display_find_npc:
                do_i_display_find_king = 0
            elif event.type == TALKING and is_the_king_speaking and not isit:
                    letters, isit = f.what_letters_do_i_display(main_k,chars_on_row,rows, max_k)
                    main_k += 1
            elif event.type == pygame.KEYDOWN and not is_the_animation_on:
                if (event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w) and not is_the_king_speaking and on_ground:
                    speed = jump_height
                    on_ground = False
                if event.key == pygame.K_g and inventory:
                    inventory, king_inventory = f.give(inventory, king_inventory, c.how_much_does_a_king_need)
                    if king_inventory < c.how_much_does_a_king_need:
                        rows, chars_on_row, max_k = f.convert_into_rows(f"Only {king_inventory}? A king needs more gold than that!",c.max_rows)
                        is_the_king_speaking = 1
                        letters, isit = f.what_letters_do_i_display(main_k,chars_on_row,rows, max_k)
                        main_k += 1
                    else:
                        rows, chars_on_row, max_k = f.convert_into_rows("Good! I order you to be proud of yourself!",c.max_rows)
                        is_the_king_speaking = 1
                        letters, isit = f.what_letters_do_i_display(main_k,chars_on_row,rows, max_k)
                        main_k += 1
                if event.key == pygame.K_RETURN and NPC.centerx > 0:
                    if king_inventory >= c.how_much_does_a_king_need and not is_the_king_speaking:
                        rows, chars_on_row, max_k = f.convert_into_rows("Now, you can leave for the next planet! Farewell!",c.max_rows)
                        is_the_king_speaking = 1
                        letters, isit = f.what_letters_do_i_display(main_k,chars_on_row,rows, max_k)
                    if isit:
                        for i in range(len(main_lines_done)):
                            if not main_lines_done[i]:
                                main_lines_done[i] = 1
                                main_k = 0
                                break
                        isit = 0
                    if not (main_lines_done[0] and main_lines_done[1]):
                        is_the_king_speaking = 1
                        for i in range(len(main_lines_done)):
                            if not main_lines_done[i]:
                                rows, chars_on_row, max_k = f.convert_into_rows(c.main_lines_1[i],c.max_rows)
                                break
                    else:
                        is_the_king_speaking = 0
                        main_k = 0
                if event.key == pygame.K_p:
                    item_to_pick = f.find_x(c.hm_items, items, c.WIDTH)
                    if item_to_pick != -1:
                        items, inventory = f.pick_up(item_to_pick, items, inventory)
        if do_i_display_find_king:
            f.display_text(screen, c.start_text[1])
        if NPC.centerx > 0 and not main_lines_done[0] and not is_the_king_speaking:
            f.display_text(screen, c.instructions[3])
        if is_the_king_speaking:
            f.talk(screen, letters, king_face)
        if not king_inventory and inventory and NPC.centerx > 0:
            f.display_text(screen, c.instructions[2])
        if main_lines_done[1]:
            f.manage_items(screen, items, ground_height)
        if king_inventory >= c.how_much_does_a_king_need and not is_the_king_speaking and not is_the_animation_on:
            is_the_animation_on = True
            pygame.time.set_timer(ANIMATION, 2000)
            initialized = False
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and not is_the_king_speaking and NPC.centerx < 171 and not is_the_animation_on:
            c.scroll -= 5
            direction = 1
            walking = 1
            for x in range(c.hm_items + 1):
                items[0][x] = items[0][x] + 5 * run
            NPC.centerx = NPC.centerx + 5 * run
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not is_the_king_speaking and NPC.centerx > -2000 and not is_the_animation_on:
            c.scroll += 5
            direction = 0
            walking = 1
            for x in range(c.hm_items + 1):
                items[0][x] = items[0][x] - 5 * run
            NPC.centerx = NPC.centerx - 5 * run
        speed += gravity
        player.y += speed
        if player.bottom >= c.HEIGHT - ground_image.get_height() + 10:
            player.bottom = c.HEIGHT - ground_image.get_height() + 10
            speed = 0
            on_ground = True
        if not is_the_animation_on:
            screen.blit(
                walkingr[char_image]
                if on_ground and walking and not direction 
                else walkingl[char_image]
                if on_ground and direction and walking
                else standing[0]
                if on_ground and direction and not walking
                else standing[1]
                if on_ground and not direction and not walking
                else jumping[1]
                if not on_ground and direction
                else jumping[0],
                player
            )
        screen.blit(king, NPC)

        if is_the_animation_on:
            if not initialized:
                char_image = 0
                yay = [p.y[0].convert_alpha(), p.y[1].convert_alpha()]
                player = yay[0].get_rect(center = (c.WIDTH / 2, c.HEIGHT - ground_image.get_height() + 175))
                initialized = True
            if event.type == CHANGE500:
                    char_image = (char_image + 1) % 2
            elif event.type == ANIMATION:
                level = 1.5
                initialized = False
                is_the_animation_on = False
            screen.blit(yay[char_image], player)
    if level == 1.5:
        if not initialized:
            home_button = f.create_button("HOME", 1)
            quit_button = f.create_button("QUIT", 2)
            initialized = True
            rect_surface = pygame.Surface((c.WIDTH, c.HEIGHT), pygame.SRCALPHA)
            pygame.draw.rect(rect_surface, (10, 0, 100, 130), rect_surface.get_rect())
            screen.blit(rect_surface, (0, 0))
        
        f.draw_button(screen, home_button)
        f.draw_button(screen, quit_button)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
                pos = pygame.mouse.get_pos()
                if f.button_click(pos[0], pos[1],home_button[1]):
                    level = 0
                    is_the_animation_on = False
                    initialized = False
                if f.button_click(pos[0], pos[1],quit_button[1]):
                    pygame.quit()
                    sys.exit()

    pygame.display.update()
    clock.tick(c.FPS)