from Entities.Bullet import Bullet

class Weapon:
    def __init__(self, bullet_group):
        self.bullet_group = bullet_group

    def shoot(self, x, y, direction):
        pass


class Pistol(Weapon):
    def __init__(self, bullet_group):
        super().__init__(bullet_group)
        self.bullet_speed = 10
        self.damage = 10

    def shoot(self, x, y, direction):
        bullet = Bullet(x, y, self.bullet_speed, direction, self.damage)
        self.bullet_group.add(bullet)


class Shotgun(Weapon):
    def __init__(self, bullet_group):
        super().__init__(bullet_group)
        self.bullet_speed = 8
        self.damage = 20

    def shoot(self, x, y, direction):
        spread = [-2, 0, 2]
        for s in spread:
            bullet = Bullet(x, y, self.bullet_speed, direction, self.damage)
            bullet.rect.y += s
            self.bullet_group.add(bullet)
