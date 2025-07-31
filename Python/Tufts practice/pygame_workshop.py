import pygame

SCREEN_W = 500
SCREEN_H = 500

def main():
    pygame.init()
    clock = pygame.time.Clock()
    bg = pygame.display.set_mode(
        (SCREEN_W, SCREEN_H),
        pygame.SRCALPHA,
        32
    )

    show_counter = 0
    font = pygame.font.Font(None, 72)
    bg_color = (0,0,0)
    curr_button = ''
    curr_x = None
    curr_y = None


    while True:
        clock.tick(60)  # 24 FPS
        
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    exit()
                case pygame.MOUSEBUTTONDOWN:
                    curr_button = str(event.button)
                case pygame.MOUSEBUTTONUP:
                    curr_button = ''
                case pygame.MOUSEMOTION:
                    curr_x, curr_y = event.pos # (255, 13)
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_w:
                            bg_color = (55,0,0)
                        case pygame.K_a:
                            bg_color = (0,55,0)
                        case pygame.K_s:
                            bg_color = (0,0,55)
                        case pygame.K_d:
                            bg_color = (55,0,55)
            
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                print('space was pressed')


            bg.fill(bg_color) # RGB 0-255 color

            button_render = font.render(f"button: {curr_button}",
                                        True,
                                        (210, 210, 210))
            bg.blit(button_render, (100, 50))

            pos_surf = font.render(f"({curr_x}, {curr_y})", 
                                   True, 
                                   (210, 210, 210))
            bg.blit(pos_surf, (100, 200))        

        # if (show_counter < 30):
        #     font = pygame.font.Font(None, 120)  # font size 2nd
        #     text_color = (210, 0, 210)
        #     text = font.render("Surprise!",1,text_color)
        #     text2 = font.render("Wow!",1,(255,0,30))
        #     text_loc = (5,5)
        #     bg.blit(text, text_loc)
        #     bg.blit(text2, (0,300))

        # show_counter += 1
        # show_counter = show_counter % 60

        # img = pygame.image.load('toothless_dancing.png')

        # pixel_loc = (20,20)
        # pixel_color = (0,255,255)
        # for i in range(30):
        #     img.set_at((i,20), pixel_color)
        # # img.set_at(pixel_loc, pixel_color)
        # bg.blit(img,(50,50))

        # new_w = img.get_width() * 0.5
        # new_h = img.get_height() * 0.5
        # img = pygame.transform.scale(img, (new_w, new_h))
        # bg.blit(img,(50,50))
        
        # img2 = pygame.image.load('toothless_dancing.png')
        # img3 = pygame.image.load('toothless_dancing.png')

        # # img_rot = -45
        # img2 = pygame.transform.rotate(img2, -45)
        # bg.blit(img2, (50,50))
        # img3 = pygame.transform.rotate(img2, -45)
        # bg.blit(img3, (150,50))

        # orig_center = img.get_rect().center  # center location of original image
        # img_rot = i # rotation amount in DEGREES, goes COUNTER-CLOCKWISE
        # i += 1  # makes rotation slightly larger every time
        # s = pygame.transform.rotate(img, img_rot) # updates image as version rotated by img_rot amount
        # rot_w = s.get_width()  # stores width of rotated img
        # rot_h = s.get_height()  # stores height of rotated img
        # bg.blit(s, (orig_center[0] - rot_w / 2, orig_center[1] - rot_h / 2))



        # img = pygame.image.load('ex_image.jpg')
        # img_loc = (50,50)
        # bg.blit(img, img_loc)

        # circle_color = (251, 171, 96)
        # circle_loc = (100,100)
        # circle_rad = 25
        # pygame.draw.circle(bg, circle_color, circle_loc, circle_rad)

        # line_color = (25, 120, 70)
        # line_start_pos = (250, 250)
        # line_end_pos = (400, 200)
        # line_w = 10
        # pygame.draw.line(bg, line_color, line_start_pos,
        #                  line_end_pos, line_w)

        pygame.display.update()


if __name__ == '__main__':
    main()