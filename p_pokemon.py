class Pokemon:
    # class variable
    Pct = 0

    # class document
    '''Pokemon Class'''

    # class method
    def __init__(self, name='Name', lv=0, pro=None, hp=10):
        # instance variable
        self.name = name
        self.lv = lv
        self.pro = pro
        self.hp = hp
        # use class variable in instance
        Pokemon.Pct += 1

    def Info(self):
        print('Name:', self.name)
        print('Lv:', self.lv)
        print('Pro:', self.pro)
        print('Hp:', self.hp)

    def Defense(self, damage):
        if self.hp >= damage:
            self.hp -= damage
        else:
            self.hp = 0
            print(self.name, 'has been defeated !!')

    def Attack(self, target, damage):
        if target.hp <= 0 or self.hp <= 0:
            return
        else:
            print(self.name, 'use %s attack' % self.pro, target.name)
            target.Defense(damage)

# help(Pokemon)
p1 = Pokemon('Pikachu', 10, 'Lightning', 100)
print('P1:', p1.Pct)
p1.Info()
p2 = Pokemon('FireDragon', 15, 'Fire', 150)
print('\nP2:', p2.Pct)
p2.Info()
print('\n%s and %s are starting to fight !!\n' % (p1.name, p2.name))
p1.Attack(p2, 30)
p2.Attack(p1, 30)
p1.Attack(p2, 30)
p2.Attack(p1, 30)
p1.Attack(p2, 30)
p2.Attack(p1, 30)
p1.Attack(p2, 30)
p2.Attack(p1, 30)

print('\nTotal number of Pokemon = ', Pokemon.Pct)
