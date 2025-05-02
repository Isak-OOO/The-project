import pygame as p
import math
import random

#p.init()
# funktionen där programmet körs
def main():
    p.init()
    class rocks(p.sprite.Sprite):
        def __init__(self, side, version, x, y, x_speed, y_speed):
            p.sprite.Sprite.__init__(self)
            self.image = p.image.load("Edvin_20241213.jpg").convert_alpha()
            self.image = p.transform.scale(self.image, (200/(2**version), 200/(2**version)))
            self.rect = self.image.get_rect()
            self.version = version
            if version == 0:
                if side == 0:
                    self.rect.center = [random.randint(0, SCREEN_WIDTH), 0]
                elif side == 1:
                    self.rect.center = [random.randint(0, SCREEN_WIDTH), SCREEN_HEIGHT]
                elif side == 2:
                    self.rect.center = [0, random.randint(0, SCREEN_HEIGHT)]
                elif side == 3:
                    self.rect.center = [SCREEN_WIDTH, random.randint(0, SCREEN_HEIGHT)]
                if random.randint(0,1) == 0:
                    self.speedx = random.uniform(float(low_speed), float(high_speed))
                else:
                    self.speedx = random.uniform(float(-low_speed), float(-high_speed))
                if random.randint(0,1) == 0:
                    self.speedy = random.uniform(float(low_speed), float(high_speed))
                else:
                    self.speedy = random.uniform(float(-low_speed), float(-3.0))
            if version >= 1:
                self.rect.center = [x, y]
                self.speedx = x_speed
                self.speedy = y_speed


        def update(self):
            self.rect.centerx += self.speedx
            self.rect.centery += self.speedy
            if self.rect.centerx < 0:
                self.rect.move_ip(SCREEN_WIDTH, 0)
            if self.rect.centerx > SCREEN_WIDTH:
                self.rect.move_ip(-SCREEN_WIDTH, 0)
            if self.rect.centery < 0:
                self.rect.move_ip(0, SCREEN_HEIGHT)
            if self.rect.centery > SCREEN_HEIGHT:
                self.rect.move_ip(0, -SCREEN_HEIGHT)
            for bullet in bullet_list:
                if self.version <= 1 and self.rect.colliderect(bullet):
                    if (self.speedx > 0 and self.speedy > 0) or (self.speedx < 0 and self.speedy < 0):
                        rock = rocks(0, self.version + 1, self.rect.centerx, self.rect.centery, self.speedx+1, self.speedy-1)
                        rock_group.add(rock)
                        rock = rocks(0, self.version + 1, self.rect.centerx, self.rect.centery, self.speedx-1, self.speedy+1)
                        rock_group.add(rock)
                        bullet.hit()
                        self.kill()
                    elif (self.speedx > 0 and self.speedy < 0) or (self.speedx < 0 and self.speedy > 0):
                        rock = rocks(0, self.version + 1, self.rect.centerx, self.rect.centery, self.speedx+1, self.speedy+1)
                        rock_group.add(rock)
                        rock = rocks(0, self.version + 1, self.rect.centerx, self.rect.centery, self.speedx-1, self.speedy-1)
                        rock_group.add(rock)
                        bullet.hit()
                        self.kill()
                if self.version == 2 and self.rect.colliderect(bullet):
                    bullet.hit()
                    self.kill()

    # skott renderingssystemet
    class bullets(p.sprite.Sprite):
        def __init__(self, x, y):
            p.sprite.Sprite.__init__(self)
            self.image = p.image.load("bullet.png").convert_alpha()
            self.image = p.transform.scale(self.image, (4, 4))
            self.rect = self.image.get_rect()
            self.rect.center = [x + 10 * (-math.cos(math.radians(direct-90))), y + 10 * (math.sin(math.radians(direct-90)))]
            self.numberx = (-math.cos(math.radians(direct-90))) 
            self.numbery = (math.sin(math.radians(direct-90)))
            self.speedx = change_x
            self.speedy = change_y
            self.dist = 0
            
        def update(self):
            if self.dist < 40:
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
                
                #if count1 < 4:
                    #if self.rect.colliderect(rock):
                        #self.kill()
            else:
                #flyttar kulan så att positionen inte stör astroiderna
                self.rect.move_ip(2*SCREEN_WIDTH, 2*SCREEN_HEIGHT)
                self.kill()
        def hit(self):
            self.rect.move_ip(2*SCREEN_WIDTH, 2*SCREEN_HEIGHT)
            self.kill()

    # uppsättning av skärmen
    SCREEN_WIDTH = int(800 * 1.2)
    SCREEN_HEIGHT = int(600 * 1.2)
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
    bullet_speed = 10
    bullet_group = p.sprite.Group()
    rock_group = p.sprite.Group()
    last_shot = 0
    clock = p.time.Clock()
    fps = 60
    low_speed = 0.5
    high_speed = 2.0
    bullet = bullets(-1000*SCREEN_WIDTH, -1000*SCREEN_WIDTH)
    bullet_group.add(bullet)
    count1 = 4
    bullet_list = []

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
        #player.blit(original_player, player_rect)
        bullet_group.draw(screen)
        bullet_group.update()
        rock_group.draw(screen)
        rock_group.update()

        # knappar för att änra skeppets egenskaper
        if keys[p.K_RIGHT] or keys[p.K_d] or keys[p.K_l]:
            direct -= 5
            #player = p.transform.rotate(original_player, direct)
            #aplayer_rect = player.get_rect(center = (x, y))
            
        if keys[p.K_LEFT] or keys[p.K_a] or keys[p.K_j]:
            direct += 5
            #player = p.transform.rotate(original_player, direct)
            #player_rect = player.get_rect(center = (x, y))
        
        if keys[p.K_SPACE] and hasshot == False and p.time.get_ticks() - last_shot > 200:
            bullet = bullets(x, y)
            bullet_list.append(bullet)
            bullet_group.add(bullet)
            last_shot = p.time.get_ticks()
            hasshot = True
        if not keys[p.K_SPACE]:
            hasshot = False

        if keys[p.K_UP] or keys[p.K_w] or keys[p.K_i]:
            change_x -= speed_factor * math.cos(math.radians(direct-90))
            change_y += speed_factor * math.sin(math.radians(direct-90))
        """if keys[p.K_s] or keys[p.K_DOWN]:
            change_x *= 0.95
            change_y *= 0.95"""
        player = p.transform.rotate(original_player, direct)
        
        #speed_factor = 0.2
        change_x *= 0.99
        change_y *= 0.99
        x += change_x
        y += change_y
        player_rect = player.get_rect(center = (x, y))
        #print(p.time.get_ticks() - last_shot > 300)
        
        # oändlig värld
        if player_rect.centery < 0:
            y += SCREEN_HEIGHT
        if player_rect.centery > SCREEN_HEIGHT:
            y -= SCREEN_HEIGHT
        if player_rect.centerx < 0:
            x += SCREEN_WIDTH
        if player_rect.centerx > SCREEN_WIDTH:
            x -= SCREEN_WIDTH

        if count1 > 1:
            rock = rocks(random.randint(0, 3), 0, 0, 0, 0, 0)
            rock_group.add(rock)
            count1 -= 1
        # programmets hastighet
        clock.tick(fps)

    p.quit()

main()