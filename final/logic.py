

class Player:
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
    
    def move(self, direction):
        if(direction == 'w'):
            self.y = max(0, self.y-1)
        elif(direction == 'a'):
            self.x = max(0, self.x-1)
        elif(direction == 's'):
            self.y = min(4, self.y+1)
        elif(direction == 'd'):
            self.x = min(4, self.x+1)

def print_map(player, treasure):
    for y in range(5):
        row = ""
        for x in range(5):
            if player.x == x and player.y == y:
                row += " P "
            elif treasure[0] == x and treasure[1] == y:
                row += " T "
            else:
                row += " . "
        print(row)
    print()

def main():
    player = Player("You")
    treasure = (3,3)

    while True:
        print_map(player, treasure)
        move = input().lower()
        if move in ["w","a","s","d"]:
            player.move(move)