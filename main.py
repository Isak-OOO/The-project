import pygame as p
import math

# funktionen där programmet körs
def main():
    p.init()

    # skott renderingssystemet
    class bullets(p.sprite.Sprite):
        def __init__(self, x, y, reach):
            p.sprite.Sprite.__init__(self)
            self.image = p.image.load("bullet.png").convert_alpha()
            self.image = p.transform.scale(self.image, (4, 4))
            self.rect = self.image.get_rect()
            self.rect.center = [x + 10 * (-math.cos(math.radians(direct-90))), y + 10 * (math.sin(math.radians(direct-90)))]
            self.numberx = (-math.cos(math.radians(direct-90)))
            self.numbery = (math.sin(math.radians(direct-90)))
            self.speedx = change_x
            self.speedy = change_y
            self.dist = reach
            
        def update(self):
            if self.dist < 50:
                self.rect.move_ip(self.numberx * bullet_speed + self.speedx, self.numbery * bullet_speed + self.speedy)
                self.dist += 1

                if self.rect.centerx < 0:
                    self.rect.move_ip(SCREEN_WIDTH, 0)
                if self.rect.centerx > SCREEN_WIDTH:
                    self.rect.move_ip(-SCREEN_WIDTH, 0)
                if self.rect.centery < 0:
                    self.rect.move_ip(0, SCREEN_HEIGHT)
                if self.rect.centery > SCREEN_HEIGHT:
                    self.rect.move_ip(0, -SCREEN_HEIGHT)
            else:
                self.remove()
    # uppsättning av skärmen
    SCREEN_WIDTH = 800 * 1.2
    SCREEN_HEIGHT = 600 * 1.2
    screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Inladdning och position av det mesta
    original_player = p.image.load("ship.jpg").convert_alpha()
    original_player = p.transform.scale(original_player, (25, 40))
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    direct = 0
    player = p.transform.rotate(original_player, direct)
    player_rect = player.get_rect(center = (x, y))
    change_x, change_y = 0, 0
    speed_factor = 0.2
    bullet_speed = 14
    bullet_group = p.sprite.Group()
    last_shot = 0
    reach = 0
    clock = p.time.Clock()

    run = True
    while run:
        
        # så jag kan stänga ner och starta om programet
        keys = p.key.get_pressed()
        for event in p.event.get():
            if event.type == p.QUIT:
                run = False
        if keys[p.K_r]:
            main()
            break

        # spelet spelar
        p.display.update()
        screen.fill((0, 0, 0))
        screen.blit(player, player_rect)
        original_player.blit(original_player, player_rect)
        bullet_group.draw(screen)
        bullet_group.update()

        # knappar för att änra skeppets egenskaper
        if keys[p.K_RIGHT] or keys[p.K_d]:
            direct -= 5
            player = p.transform.rotate(original_player, direct)
            player_rect = player.get_rect(center = (x, y))
            
        if keys[p.K_LEFT] or keys[p.K_a]:
            direct += 5
            player = p.transform.rotate(original_player, direct)
            player_rect = player.get_rect(center = (x, y))

        if keys[p.K_UP] or keys[p.K_w]:
            speed_factor += 0.01
            change_x -= speed_factor * math.cos(math.radians(direct-90))
            change_y += speed_factor * math.sin(math.radians(direct-90))
        """if keys[p.K_s] or keys[p.K_DOWN]:
            change_x *= 0.95
            change_y *= 0.95"""
        speed_factor = 0.2
        change_x *= 0.99
        change_y *= 0.99
        x += change_x
        y += change_y
        player_rect = player.get_rect(center = (x, y))
        if keys[p.K_SPACE]:# and p.time.get_ticks() - last_shot > 200:
            bullet = bullets(x, y, reach)
            bullet_group.add(bullet)
            #last_shot = p.time.get_ticks()

        # oändlig värld
        if player_rect.centery < 0:
            y += SCREEN_HEIGHT
        if player_rect.centery > SCREEN_HEIGHT:
            y -= SCREEN_HEIGHT
        if player_rect.centerx < 0:
            x += SCREEN_WIDTH
        if player_rect.centerx > SCREEN_WIDTH:
            x -= SCREEN_WIDTH
        
        # programmets hastighet
        clock.tick(60)

    p.quit()

main()