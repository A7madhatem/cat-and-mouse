# -------- Main Program Loop -----------
while not done:
    if way == 0:
        time.sleep(0.5)
        movement()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:       # If user clicked close
            done = True           # Flag that we are done so we exit this loop
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and way == 1:      # Control mouse by keys
            mouse_posx = mouse_posx-66
            current_pos = (mouse_posx, mouse_posy)
            LEFT_presses += 1
        if key[pygame.K_RIGHT] and way == 1:
            mouse_posx = mouse_posx+66
            current_pos = (mouse_posx, mouse_posy)
            right_presses += 1
        if key[pygame.K_UP] and way == 1:
            mouse_posy = mouse_posy-66
            current_pos = (mouse_posx, mouse_posy)
            UP_presses += 1
        if key[pygame.K_DOWN] and way == 1:
            mouse_posy = mouse_posy+66
            current_pos = (mouse_posx, mouse_posy)
            DOWN_presses += 1
    KEY_PRESSES = LEFT_presses + right_presses + UP_presses + DOWN_presses
    if KEY_PRESSES == 21:           # 4 conditions of mouse
        starve()
        time.sleep(2)
        exit()
    if current_pos == (467, 269):       # When escaped
        escape()
        time.sleep(2)
        exit()
    if (mouse_posy == 71 or mouse_posy == 467) and (mouse_posx in bl_mouse):   # When drowned
        water()
        time.sleep(2)
        exit()
    if (mouse_posx == 71 or mouse_posx == 467) and (mouse_posy in bl_mouse):    # // // // //
        water()
        time.sleep(2)
        exit()
    if current_pos == random_catv:    # When touching the cat
        dead()
        time.sleep(1)
        exit()
    surface.blit(cat, (random_catx, random_caty))    # Displaying cat and mouse
    surface.blit(mouse, current_pos)
    win.update()
    pygame.display.update()
    screen.fill(BLACK)
    for row in range(1):               # Draw the grid
        for column in range(7):
            color = BLUE
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN+66,
                              (MARGIN + HEIGHT) * row + MARGIN+66,
                              WIDTH,
                              HEIGHT])
    for row in range(7):
        for column in range(1):
            color = BLUE
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN+66,
                              (MARGIN + HEIGHT) * row + MARGIN+66,
                              WIDTH,
                              HEIGHT])
    for row in range(7):
        for column in range(1):
            color = BLUE
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN + 468,
                              (MARGIN + HEIGHT) * row + MARGIN + 66,
                              WIDTH,
                              HEIGHT])
    for row in range(1):
        for column in range(7):
            color = BLUE
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN+66,
                              (MARGIN + HEIGHT) * row + MARGIN+468,
                              WIDTH,
                              HEIGHT])
    for row in range(5):
        for column in range(5):
            color = WHITE
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN+133,
                              (MARGIN + HEIGHT) * row + MARGIN+133,
                              WIDTH,
                              HEIGHT])
    for row in range(1):
        for column in range(1):
            color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN+468,
                              (MARGIN + HEIGHT) * row + MARGIN+266,
                              WIDTH,
                              HEIGHT])
    clock.tick(200)
pygame.quit()