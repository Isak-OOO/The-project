import pygame as p
import math
import time

#last_called = 0
bullet_speed = 40
"""
def shooting(speedbx, speedby, screen, bx, by, b2x, b2y, b3x, b3y):
    while bx > -10 and bx < 1200 and by > -10 and by < 1000:
        bx += bullet_speed * speedbx
        by += bullet_speed * speedby
        b2x += bullet_speed * speedbx
        b2y += bullet_speed * speedby
        b3x += bullet_speed * speedbx
        b3y += bullet_speed * speedby

        bullet = p.Rect((bx, by, 4, 4))
        bullet2 = p.Rect((b2x, b2y, 4, 4))
        bullet3 = p.Rect((b3x, b3y, 4, 4))
        p.draw.rect(screen, (255, 255, 255), bullet)
        p.draw.rect(screen, (100, 100, 100), bullet2)
        p.draw.rect(screen, (50, 50, 50), bullet3)
"""
def main():
    p.init() # starta programmet

    

                #bullet.move_ip(bx,by)
                #if last_called < time.time() - 1:
                    #last_called = time.time()
                    #break
            
    can_shoot = 0
    # variabler till hastigheten
    change_x = 0
    change_y = 0
    #playerx_vect = 0
    #playery_vect = -1
    speed_factor = 0.2

    # uppsättning av skärmen
    SCREEN_WIDTH = 800 * 1.2
    SCREEN_HEIGHT = 600 * 1.2
    screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Inladdning och position av skeppet
    #p.display.set_caption("Load Image in Pygame")
    original_player = p.image.load("ship.jpg").convert_alpha()
    original_player = p.transform.scale(original_player, (30, 40))
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    #old_direct = 0
    direct = 0
    player = p.transform.rotate(original_player, direct)
    player_rect = player.get_rect(center = (x, y))
    #player_speed = p.math.Vector2(speed_factor * playerx_vect, speed_factor * playery_vect)

    # uppsättning av skotten
    #bullet = p.Rect((x-5, y-5, 10, 10))

    # uppsättning av klockan
    clock = p.time.Clock()

    run = True

    while run:
        keys = p.key.get_pressed()
        for event in p.event.get():
            if event.type == p.QUIT:
                run = False
        if keys[p.K_r]:
            main()
            break
        p.display.update()
        #p.display.flip()
        screen.fill((0, 0, 0))
        screen.blit(player, player_rect)

        if keys[p.K_RIGHT] or keys[p.K_d]:
            direct -= 5
            player = p.transform.rotate(original_player, direct)

            player_rect = player.get_rect(center = (x, y))
        if keys[p.K_LEFT] or keys[p.K_a]:
            direct += 5
            player = p.transform.rotate(original_player, direct)

            player_rect = player.get_rect(center = (x, y))
        if keys[p.K_UP] or keys[p.K_w]:
            speed_factor += 0.05
            change_x -= speed_factor * math.cos(math.radians(direct-90))
            change_y += speed_factor * math.sin(math.radians(direct-90))
        speed_factor = 0.3
        change_x *= 0.99
        change_y *= 0.99
        x += change_x
        y += change_y
        player_rect = player.get_rect(center = (x, y))
        original_player.blit(original_player, player_rect)
        #x, y = player_rect.centerx, player_rect.centery
        if player_rect.centery < 20:
            y += SCREEN_HEIGHT - 40
        if player_rect.centery > SCREEN_HEIGHT - 20:
            y -= SCREEN_HEIGHT - 40
        if player_rect.centerx < 20:
            x += SCREEN_WIDTH - 40
        if player_rect.centerx > SCREEN_WIDTH - 20:
            x -= SCREEN_WIDTH - 40
        
        """if x >= 0.1:
            x -= 0.1
        if x <= -0.1:
            x += 0.1
        if y >= 0.1:
            y -= 0.1
        if y <= -0.1:
            y += 0.1
        """

        if can_shoot - time.time() < 0 and keys[p.K_SPACE]:
            speedbx = (-math.cos(math.radians(direct-90)))
            speedby = math.sin(math.radians(direct-90))
            bx = x - 10 * speedbx
            by = y - 10 * speedby
            b2x = x - 20 * speedbx
            b2y = y - 20 * speedby
            b3x = x - 30 * speedbx
            b3y = y - 30 * speedby
            can_shoot = time.time() + 0.4
            # while bx > -10 and bx < 1200 and by > -10 and by < 1000:
        if can_shoot - time.time() > 0 and not keys[p.K_SPACE]:
            bx += bullet_speed * speedbx
            by += bullet_speed * speedby
            b2x += bullet_speed * speedbx
            b2y += bullet_speed * speedby
            b3x += bullet_speed * speedbx
            b3y += bullet_speed * speedby

            bullet = p.Rect((bx, by, 4, 4))
            bullet2 = p.Rect((b2x, b2y, 4, 4))
            bullet3 = p.Rect((b3x, b3y, 4, 4))
            p.draw.rect(screen, (255, 255, 255), bullet)
            p.draw.rect(screen, (100, 100, 100), bullet2)
            p.draw.rect(screen, (50, 50, 50), bullet3)
            #can_shoot = time.time() + 3
            #can_shoot = False


        clock.tick(60) # programmets hastighet



    p.quit()

main()