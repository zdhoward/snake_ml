from random import randrange
from getch import getch

def main():
    
    s = Snake(20,20)
    while True:
        #print (s.tail)
        #print(s.sense())
        s.sense()
        s.print()
        direction = getch()
        if direction == 'A':
            direction="up"
        elif direction == 'C':
            direction="right"
        elif direction == 'B':
            direction="down"
        elif direction == 'D':
            direction="left"
        if direction == "up" or direction == "right" or direction == "down" or direction == "left":
            s.move(direction)


class Snake:
    def __init__(self, _height, _width):
        self.height = _height
        self.width = _width

        self.tail = [(round(_width/2), round(_height/2))]
        self.length = 1

        self.food = []

        self.__generate_food()

    def __generate_food(self):
        generating = True
        (x, y) = (0,0)
        while generating:
            x = randrange(0,self.width)
            y = randrange(0, self.height)
            generating = False
                    
            if (x, y) in self.food or (x,y) in self.tail:
                generating = True


        self.food.append((x,y))

    def __grow(self):
        self.length += 1
        return True

    def __in_bounds(self, x, y):
        if x > self.width - 1 or x < 0 or y > self.height - 1 or y < 0:
            return False
        return True

    def sense(self):
        data = {}
        
        x, y = self.tail[0]
        if (x, y - 1) in self.tail or not self.__in_bounds(x, y - 1):
            data['up'] = False
        else:
            data['up'] = True
        if (x + 1, y) in self.tail or not self.__in_bounds(x + 1, y):
            data['right'] = False
        else:
            data['right'] = True
        if (x, y + 1) in self.tail or not self.__in_bounds(x, y + 1):
            data['down'] = False
        else:
            data['down'] = True
        if (x - 1, y) in self.tail or not self.__in_bounds(x - 1, y):
            data['left'] = False
        else:
            data['left'] = True

        print("DATA:")
        print(data)

        return data

    def print(self):
        print("= "*self.width)
        for y in range(self.height):
            for x in range(self.width):
                symbol = "  "
                if (x, y) in self.food:
                    symbol = "F "
                if (x, y) in self.tail:
                    symbol = "X "
                print(symbol, end='')
            print()
        print("= "*self.width)


    def die(self):
        print ("YOU HAVE DIED")
        #self.__init__(self.height, self.width)
        exit(1)
        return True

    def move(self, direction):
        x, y = self.tail[0]

        if direction == "up":
            y -= 1
        elif direction == "right":
            x += 1
        elif direction == "down":
            y += 1
        elif direction == "left":
            x -= 1
        
        ## if the move is illegal, game over
        if not self.__in_bounds(x,y):
            self.die()
        if (x, y) in self.tail:
            self.die()
        ## if the move lands on food, grow
        if (x,y) in self.food:
            self.__grow()
            self.food.remove((x,y))
            self.__generate_food()

        self.tail.insert(0, (x, y))
        if len(self.tail) > self.length:
            self.tail.pop() 

        return True

    def takeTurn(self):
        return True

if __name__ == "__main__":
    main()