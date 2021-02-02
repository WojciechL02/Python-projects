import pygame, random
import graphics as g
import map


pygame.init()

clock = pygame.time.Clock()

W_WIDTH = 1024
W_HEIGHT = 1024

win = pygame.display.set_mode((W_WIDTH, W_HEIGHT), 0, 32)
pygame.display.set_caption("Christmas Game")
display = pygame.Surface((1024, 1024))

# music and sounds
music = pygame.mixer.music.load('sounds/music.mp3')
pygame.mixer_music.set_volume(0.05)
pygame.mixer.music.play(-1)

point_score = pygame.mixer.Sound('sounds/score.ogg')
point_score.set_volume(0.25)
lose_hp = pygame.mixer.Sound('sounds/lose_hp.ogg')
lose_hp.set_volume(0.25)


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 8
        self.isJump = False
        self.left = False
        self.right = False
        self.jumpCount = 10
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 13, 29, 50)
    
    def draw(self, display):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if not self.standing:
            if self.left:
                display.blit(g.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                display.blit(g.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.left:
                display.blit(g.walkLeft[0], (self.x, self.y))
            else:
                display.blit(g.walkRight[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 13, 29, 50)


class Projectile(object):
    def __init__(self, img, x, y, facing):
        self.x = x
        self.y = y
        self.img = img
        self.facing = facing
        self.vel = 12 * facing
    
    def draw(self, display):
        display.blit(self.img, (round(self.x), round(self.y)))
    

class Present(object):
    def __init__(self, img, x, vel, h_r, h_d, h_w, h_h):
        self.x = x
        self.y = 0
        self.width = 64
        self.height = 64
        self.vel = vel
        self.img = img
        self.h_r = h_r
        self.h_d = h_d
        self.h_w = h_w
        self.h_h = h_h
        self.hitbox = (self.x + self.h_r, self.y + self.h_d, self.h_w, self.h_h)
        self.visible = True

    def draw(self, display):
        if self.visible:
            display.blit(self.img, (self.x, self.y))
            self.hitbox = (self.x + self.h_r, self.y + self.h_d, self.h_w, self.h_h)
    
    def hit(self):
        self.visible = False


def redrawGameWindow():
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 32)
    label = font.render("Score: " + str(score), 1, (255, 255, 255))
    display.blit(label, (100, 36))
    man.draw(display)
    gift.draw(display)
    for bullet in bullets:
        bullet.draw(display)
    win.blit(pygame.transform.scale(display,(1024,1024)), (0,0))
    pygame.display.update()


def main_menu(display):
    run = True
    while run:
        display.blit(g.bg, (0, 0))
        y = 0
        for row in map.start_map:
            x = 0
            for tile in row:
                if tile == "AA":
                    display.blit(g.A, (x*64, y*64))
                if tile == "EE":
                    display.blit(g.E, (x*64, y*64))
                if tile == "OO":
                    display.blit(g.O, (x*64, y*64))
                if tile == "KK":
                    display.blit(g.K, (x*64, y*64))
                if tile == "NN":
                    display.blit(g.N, (x*64, y*64))
                if tile == "PP":
                    display.blit(g.P, (x*64, y*64))
                if tile == "RR":
                    display.blit(g.R, (x*64, y*64))
                if tile == "SS":
                    display.blit(g.S, (x*64, y*64))
                if tile == "TT":
                    display.blit(g.T, (x*64, y*64))
                if tile == "YY":
                    display.blit(g.Y, (x*64, y*64))
                if tile == "d1":
                    display.blit(g.d1, (x*64, y*64))
                if tile == "e1":
                    display.blit(g.e1, (x*64, y*64))
                if tile == "e2":
                    display.blit(g.e2, (x*64, y*64))
                if tile == "e3":
                    display.blit(g.e3, (x*64, y*64))
                if tile == "e4":
                    display.blit(g.e4, (x*64, y*64))
                x += 1
            y += 1
        win.blit(pygame.transform.scale(display, (1024,1024)), (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()
    pygame.display.quit()


def end_screen(display):
    run = True
    while run:
        display.blit(g.bg, (0, 0))
        y = 0
        for row in map.end_map:
            x = 0
            for tile in row:
                if tile == "AA":
                    display.blit(g.A, (x*64, y*64))
                if tile == "EE":
                    display.blit(g.E, (x*64, y*64))
                if tile == "GG":
                    display.blit(g.G, (x*64, y*64))
                if tile == "MM":
                    display.blit(g.M, (x*64, y*64))
                if tile == "OO":
                    display.blit(g.O, (x*64, y*64))
                if tile == "RR":
                    display.blit(g.R, (x*64, y*64))
                if tile == "VV":
                    display.blit(g.V, (x*64, y*64))
                if tile == "d1":
                    display.blit(g.d1, (x*64, y*64))
                if tile == "d2":
                    display.blit(g.d2, (x*64, y*64))
                if tile == "e3":
                    display.blit(g.e3, (x*64, y*64))
                if tile == "e4":
                    display.blit(g.e4, (x*64, y*64))
                x += 1
            y += 1
        win.blit(pygame.transform.scale(display, (1024,1024)), (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                run = False
            elif keys[pygame.K_SPACE]:
                main_menu(display)
    pygame.display.quit()


def main():
    global score, man, gift, bullets
    man = Player(480, 768, 64, 64)
    gift = Present(g.e1 ,random.randrange(64, W_WIDTH - 128), 5, 0, 0, 40, 64)
    score = 0
    health = 3
    shootLoop = 0
    bullets = []
    run = True
    while run:
        display.blit(g.bg, (0,0))

        if shootLoop > 0:
            shootLoop += 1
        if shootLoop > 7:
            shootLoop = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # missiles handling
        for bullet in bullets:
            if bullet.y - 4 < gift.hitbox[1] + gift.hitbox[3] and bullet.y + 4 > gift.hitbox[1]:
                if bullet.x + 4 > gift.hitbox[0] and bullet.x - 4 < gift.hitbox[0] + gift.hitbox[2]:
                    gift.hit()
                    bullets.pop(bullets.index(bullet))
                    if health > 0:
                        score += 1
                        point_score.play()
            if bullet.x < W_WIDTH - 72 and bullet.x > 64:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            run = False

        # shooting
        if keys[pygame.K_SPACE] and shootLoop == 0:
            if man.left:
                facing = -1
            else:
                facing = 1
            if len(bullets) < 20:
                bullets.append(Projectile(g.sb, round(man.x + man.width // 2), round(man.y + man.height // 2) - 10, facing))
            shootLoop = 1

        # player moving
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and man.x > 48:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.standing = False
        elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and man.x < W_WIDTH - 112:
            man.x += man.vel
            man.left = False
            man.right = True
            man.standing = False
        else:
            man.standing = True
            walkCount = 0
        
        if not man.isJump:
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                man.isJump = True
                man.left = False
                man.right = False
                man.walkCount = 0
        else:
            if man.jumpCount >= -10:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1
                man.y -= (man.jumpCount ** 2) * 0.5 * neg
                man.jumpCount -= 1
            else:
                man.isJump = False
                man.jumpCount = 10
        
        # gift-man collisions
        if gift.hitbox[1] + gift.hitbox[3] + 8 < man.hitbox[1] + man.hitbox[3] and gift.hitbox[1] + gift.hitbox[3] > man.hitbox[1]:
            if man.hitbox[0] in range(gift.x, gift.x + gift.width + 1) or man.hitbox[0] + man.hitbox[3] in range(gift.x, gift.x + gift.width + 1):
                gift.hit()
                health -= 1
                lose_hp.play()
        
        # falling presents
        if gift.visible and gift.y < W_HEIGHT - 192 - 50:
            gift.y += gift.vel
        else:
            if gift.visible:
                health -= 1
                lose_hp.play()
            if health > 0:
                new_x = random.randrange(64, W_WIDTH - 128)
                img = random.randrange(1, 5)
                if score in range(0, 6):
                    vel = 6
                elif score in range(6, 11):
                    vel = 8
                elif score in range(11, 16):
                    vel = 10
                elif score in range(16, 26):
                    vel = 12
                elif score in range(26, 36):
                    vel = 15
                elif score in range(36, 41):
                    vel = 18
                elif score in range(41, 51):
                    vel = 20
                else:
                    vel = 25
                if img == 1:
                    h_w = 40
                    h_h = 64
                    gift = Present(g.e1, new_x, vel, 0, 0, h_w, h_h)
                elif img == 2:
                    h_w = 56
                    h_h = 56
                    gift = Present(g.e2, new_x, vel, 0, 0, h_w, h_h)
                elif img == 3:
                    h_w = 48
                    h_h = 64
                    gift = Present(g.e3, new_x, vel, 0, 0, h_w, h_h)
                elif img == 4:
                    h_w = 52
                    h_h = 52
                    gift = Present(g.e4, new_x, vel, 4, 4, h_w, h_h)
            else:
                end_screen(display)
        
        # health bar
        if health == 3:
            display.blit(g.ss, (W_WIDTH-5*64, 0))
            display.blit(g.ss, (W_WIDTH-4*64, 0))
            display.blit(g.ss, (W_WIDTH-3*64, 0))
        elif health == 2:
            display.blit(g.ss, (W_WIDTH-5*64, 0))
            display.blit(g.ss, (W_WIDTH-4*64, 0))
        elif health == 1:
            display.blit(g.ss, (W_WIDTH-5*64, 0))
            
        # map rendering
        y = 0
        for row in map.game_map:
            x = 0
            for tile in row:
                if tile == "a1":
                    display.blit(g.a1, (x*64, y*64))
                if tile == "a2":
                    display.blit(g.a2, (x*64, y*64))
                if tile == "a3":
                    display.blit(g.a3, (x*64, y*64))
                if tile == "a4":
                    display.blit(g.a4, (x*64, y*64))
                if tile == "b1":
                    display.blit(g.b1, (x*64, y*64))
                if tile == "b2":
                    display.blit(g.b2, (x*64, y*64))
                if tile == "b3":
                    display.blit(g.b3, (x*64, y*64))
                if tile == "b4":
                    display.blit(g.b4, (x*64, y*64))
                if tile == "c1":
                    display.blit(g.c1, (x*64, y*64))
                if tile == "c2":
                    display.blit(g.c2, (x*64, y*64))
                if tile == "c3":
                    display.blit(g.c3, (x*64, y*64))
                if tile == "c4":
                    display.blit(g.c4, (x*64, y*64))
                if tile == "d1":
                    display.blit(g.d1, (x*64, y*64))
                if tile == "d2":
                    display.blit(g.d2, (x*64, y*64))
                if tile == "d3":
                    display.blit(g.d3, (x*64, y*64))
                if tile == "d4":
                    display.blit(g.d4, (x*64, y*64))
                if tile == "e1":
                    display.blit(g.e1, (x*64, y*64))
                if tile == "e2":
                    display.blit(g.e2, (x*64, y*64))
                if tile == "e3":
                    display.blit(g.e3, (x*64, y*64))
                if tile == "e4":
                    display.blit(g.e4, (x*64, y*64))

                if tile == "AA":
                    display.blit(g.A, (x*64, y*64))
                if tile == "CC":
                    display.blit(g.C, (x*64, y*64))
                if tile == "EE":
                    display.blit(g.E, (x*64, y*64))
                if tile == "GG":
                    display.blit(g.G, (x*64, y*64))
                if tile == "HH":
                    display.blit(g.H, (x*64, y*64))
                if tile == "II":
                    display.blit(g.I, (x*64, y*64))
                if tile == "MM":
                    display.blit(g.M, (x*64, y*64))
                if tile == "RR":
                    display.blit(g.R, (x*64, y*64))
                if tile == "SS":
                    display.blit(g.S, (x*64, y*64))
                if tile == "TT":
                    display.blit(g.T, (x*64, y*64))     
                x += 1
            y += 1

        redrawGameWindow()
        clock.tick(75)

    pygame.quit()


# start game
main_menu(display)
