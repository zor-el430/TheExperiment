import os
import random


# Entity is a neato thing
class Entity:
    def __init__(self, x_position, y_position, name, display):
        self.x_position = x_position
        self.y_position = y_position
        self.name = name
        self.display = display

    def info(self):
        info = [self.x_position, self.y_position, self.name, self.display]
        return info

    def new_instance(self):
        pass

    x_position = 0
    y_position = 0
    name = ""
    display = ""

    def move(self, direction, entities, x_position, y_position):
        pass


class MoveableEntity(Entity):
    def __init__(self, x_position, y_position, name, display):
        super().__init__(x_position, y_position, name, display)

    def move(self, direction, entities, board_x, board_y):
        target_dest = [self.x_position, self.y_position]
        if direction == "up":
            target_dest[1] -= 1
        elif direction == "down":
            target_dest[1] += 1
        elif direction == "left":
            target_dest[0] -= 1
        elif direction == "right":
            target_dest[0] += 1
        else:
            return False, "Please type a direction"
        for e in range(0, len(entities)):
            if target_dest[0] == -1 or target_dest[0] == board_x or target_dest[1] == -1 or target_dest[1] == board_y:
                return False, "You can't go that way!"
            if target_dest[0] == entities[e].x_position and target_dest[1] == entities[e].y_position:
                print(entities[e].info()[2])
                return False, "There's a " + entities[e].info()[2] + " in the way!"
            elif e == len(entities) - 1:
                self.x_position = target_dest[0]
                self.y_position = target_dest[1]
                return True, ""


class Dog(MoveableEntity):
    def __init__(self, x_position, y_position, name, display):
        super().__init__(x_position, y_position, name, display)

    def move(self, direction, entities, board_x, board_y):
        direction_list = ["up", "down", "right", "left"]
        end_loop = False
        while not end_loop:
            direction = random.choice(direction_list)
            end_loop, response = super().move(direction, entities, board_x, board_y)
            if not end_loop:
                direction_list.remove(direction)
        return end_loop, response




def startup(board_x, board_y):
    entities = [MoveableEntity(0, 0, "PC", "O")]
    dog_spawn_check = True
    while dog_spawn_check:
        x_position = random.randint(0, board_x - 1)
        y_position = random.randint(0, board_y - 1)
        if x_position == 0 and y_position == 0:
            pass
        else:
            entities.append(Dog(x_position, y_position, "dog", "D"))
            dog_spawn_check = False
    entity_count = random.randint(3, 5)
    loop_count = 0
    while loop_count <= entity_count:
        x_position = random.randint(0, board_x - 1)
        y_position = random.randint(0, board_y - 1)
        for i in range(0, len(entities)):
            if entities[i].x_position == x_position and entities[i].y_position == y_position:
                break
            elif i == len(entities) - 1:
                type_list = ["log", "rock"]
                object_name = random.choice(type_list)
                if object_name == "log":
                    entities.append(Entity(x_position, y_position, object_name, "L"))
                    loop_count += 1
                elif object_name == "rock":
                    entities.append(Entity(x_position, y_position, object_name, "R"))
                    loop_count += 1
    return entities


def main(board_x, board_y):
    entities = startup(board_x, board_y)
    for i in range(0, len(entities)):
        print(entities[i].info())
    os.system('cls')
    message = ""
    direction = ""
    while direction != "stop":
        os.system('cls')
        board(board_x, board_y, entities)
        print(message)
        direction = input("Move: ")
        direction = direction.lower()
        end_loop, message = entities[0].move(direction, entities, board_x, board_y)
        entities[1].move(direction, entities, board_x, board_y)
        # dog_move()


def board(board_x, board_y, entities):
    lines = []
    for x in range(0, board_x):
        # Goes across the collums from 0 to board_x
        lines.append([])
        for y in range(0, board_y):
            for e in range(0, len(entities)):
                if entities[e].y_position == y and entities[e].x_position == x:
                    print(entities[e].info())
                    lines[x].append(entities[e].info()[3] + " ")
                    break
                elif e == len(entities) - 1:
                    lines[x].append("' ")
            # print(lines[x])

    output = ""
    for y in range(0, board_y):
        for x in range(0, board_x):
            output = output + lines[x][y]
        output = output + "\n"
    print(output)


if __name__ == "__main__":
    main(10, 8)
