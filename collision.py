import pygame


class Collide:
    def penetration(self, player, wall):
        cor_x, cor_y = 0, 0
        if player.rect.colliderect(wall.rect):
            if wall.rect.x < player.rect.x < wall.rect.right:
                cor_x = wall.rect.right - player.rect.x
            if wall.rect.y < player.rect.y < wall.rect.bottom:
                cor_y = wall.rect.bottom - player.rect.y
            if wall.rect.y < player.rect.bottom < wall.rect.bottom:
                cor_y = wall.rect.y - player.rect.bottom
            if wall.rect.x < player.rect.right < wall.rect.right:
                cor_x = wall.rect.x - player.rect.right
        return cor_x, cor_y

    def no_scroll(self, sprite, group):
        around = pygame.sprite.spritecollide(sprite, group, False)
        for i in around:
            dx_cor, dy_cor = self.penetration(sprite, i)

            if dx_cor == 0:
                sprite.rect.y += dy_cor
            elif dy_cor == 0:
                sprite.rect.x += dx_cor
            else:
                if abs(dx_cor) < abs(dy_cor):
                    dy_cor = 0
                elif abs(dy_cor) < abs(dx_cor):
                    dx_cor = 0
                if dy_cor != 0:
                    sprite.rect.y += dy_cor
                elif dx_cor != 0:
                    sprite.rect.x += dx_cor

    def scrolled(self, sprite, group):
        around = pygame.sprite.spritecollide(sprite, group, False)
        for i in around:
            dx_cor, dy_cor = self.penetration(sprite, i)

            if dx_cor == 0:
                for j in group:
                    j.rect.y -= dy_cor
            elif dy_cor == 0:
                for j in group:
                    j.rect.x -= dx_cor
            else:
                if abs(dx_cor) < abs(dy_cor):
                    dy_cor = 0
                elif abs(dy_cor) < abs(dx_cor):
                    dx_cor = 0
                if dy_cor != 0:
                    for j in group:
                        j.rect.y -= dy_cor
                elif dx_cor != 0:
                    for j in group:
                        j.rect.x -= dx_cor

    def collision(self, sprite, group):
        self.scrolled(sprite, group)
        # print([*group][-1].rect.bottom)
