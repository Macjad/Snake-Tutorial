import pygame
import random

# A bunch of colours in tuple format
forestGreen = (34, 139, 34)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)


class Snake:
    """
    The snake class is our class that holds all data about the snake. This class provides the direction that the snake
    is travelling in, and acts as an interface for the 'body' of the snake (which is implemented using a linked list).
    """

    def __init__(self):
        """
        Create the snake, by randomly choosing a direction the snake will be pointing and randomly placing it in
        within the grid.
        """
        self.direction = random.choice(["left", "right", "up", "down"])
        node = BodyNode(random.randint(2, 17), random.randint(2, 17))
        self.body = LinkedBody(node)

    def location(self):
        """
        Gives the location of where the head of head of the snake is by calling the instance object of the linked list.

        Returns:
            tuple: In the format (x, y) co-ordinates of where the head of the snake is located.
        """
        return self.body.head_location()

    def move(self):
        """
        This function moves the snake by taking what the direction attribute of the snake currently is. Using the
        direction value, it will check to see if it is a valid move (the snake will not hit the wall), and if valid
        will call the linked list class to move all the nodes based on the snakes direction.

        Returns:
            bool: True if the snake will not hit a wall (it will stay alive), false if the snake will hit a wall.
        """
        coords = self.body.head_location()
        x, y = coords[0], coords[1]

        dx, dy = 0, 0
        if self.direction == "left":
            dx = -1
        elif self.direction == "right":
            dx = 1
        elif self.direction == "up":
            dy = -1
        elif self.direction == "down":
            dy = 1

        if 0 <= x + dx <= 19 and 0 <= y + dy <= 19:
            self.body.move(x + dx, y + dy)
            return True
        return False

    def collided(self):
        """
        Checks to see whether the snake has collided with itself or not.

        Returns:
            bool: False if snake has not collided with itself, true if the snake has collided.
        """
        return len(self.body.occupation()) != len(set(self.body.occupation()))

    def occupation(self):
        """
        Gives a list of the grid co-ordinates of where the snake is by calling the occupation method on the linked list.

        Returns:
            list: A list of all the grid co-ordinates that the snake currently is at.
        """
        return self.body.occupation()

    def draw(self, screen):
        """
        Draws the snake by calling the draw method part of the linked list object instance, passing through the
        direction that the snake is travelling in as a argument.

        Args:
            screen: The screen object used to draw polygons onto.
        """
        self.body.draw(screen, self.direction)

    def __str__(self):
        """
        Allows you to debug the location of the snake by including print(snake) in the main while loop.

        Returns:
            str: String of where the head of the snake is and which direction it is traveling.
        """
        coords = self.body.head_location()
        return "<Snake location:({},{}) direction: {}>".format(coords[0], coords[1], self.direction)


class LinkedBody:
    """
    The LinkedBody class acts as a linked list, and will be used to represent the body parts of the snake
    """

    def __init__(self, node):
        """
        Initialise the overall shell of the body. This class acts as our linked list, which will hold multiple nodes.
        The first node passed in as an argument will act as the head of the snake and added to the linked list, and the
        length of the linked list will be respectively be set to 1.

        Args:
            node: The initial node (an instance of the BodyNode class) added to the linked list which acts as the head
                  of the snake.
        """
        self.head = node
        self.length = 1

    def head_location(self):
        """
        Gives the x and y co-ordinates of the first (head) node in the linked list.

        Returns:
            tuple: In the format (x, y) co-ordinates of the first node in the linked list.
        """
        return (self.head.x, self.head.y)

    def draw(self, screen, direction):
        """
        This method will go through the linked list, and call the 'draw' method part of the node object. It will
        alternate between two colours, and draw the head of the snake differently to the other parts of the snake.

        Args:
            screen: The screen object used to draw polygons onto.
            direction: The direction that the snake is going, represented as a string.
        """
        current_node = self.head
        i = 0
        while current_node is not None:
            if i % 2 == 0:
                if i != 0:
                    current_node.draw(screen, green, direction, False)
            else:
                current_node.draw(screen, yellow, direction, False)
            current_node = current_node.next
            i += 1

        # Draw the head last else when a node is added, last node will be drawn on top of the head
        current_node = self.head
        current_node.draw(screen, green, direction, True)

    # TODO: For you to implement
    def move(self, x, y):
        """
        The move method will move the snake in the direction it is going by changing the x and y value for each node in
        the linked list. The values of the parameters will be where the head node of the linked list needs to go, and
        then after each node in the linked list will be set to the location of the previous node in the linked list.

        Example:
            Linked list:            [(2, 2), (2, 3), (3, 3), (3, 4), (3, 5)]
            New head node location: (1, 2)
            => Moved linked list:   [(1, 2), (2, 2), (2, 3), (3, 3), (3, 4)]

        Args:
            x: The x co-ordinate of where the head of the snake will be next
            y: The y co-ordinate of where the head of the snake will be next
        """
        pass  # TODO: Remove this line on implementing functionality

    # TODO: For you to implement
    def addnode(self, x, y):
        """
        addnode will add a new node to the end of the linked list. The node can be initialised with the x and y
        co-ordinates passed as arguments, which represent the location of the where the head of the snake (the head
        node in the linked list) currently is. The location is arbitrary because when addnode is called, the game won't
        check to see any collisions (as the apple will be spawned at a 'valid' location), so spawning the new node with
        the co-ordinates as the same as the head is fine. The next time the snake moves, the node will be moved to it's
        correct spot. The length of the linked list should also decrease.

        Args:
            x: x co-ordinate of the head node of the linked list
            y: y co-ordinate of the head node of the linked list
        """
        pass  # TODO: Remove this line on implementing functionality

    # TODO: For you to implement
    def occupation(self):
        """
        The occupation method returns a list of the co-ordinates of all the nodes in the linked list. This method is
        used in the snake class to check to see if the snake has collided with itself.

        Returns:
            list: A list of the co-ordinates of all nodes in the linked list in respective (x, y) tuple format.
                  Example list returned: [(0, 2), (0, 3), (0, 4), (1, 4), (2, 4)]
        """
        pass  # TODO: Remove this line on implementing functionality

    # TODO: For you to implement
    def removelast(self):
        """
        This method will remove the last node in the linked list, to represent the snake shrinking. There must always
        be one node in the linked list (the head node must always exist), so the code should prevent being able to
        remove a node if there is only one node in the linked list. When a node is removed from the linked list, the
        length of the linked list should also decrease.
        """
        pass  # TODO: Remove this line on implementing functionality

    # TODO: For you to implement
    def reverse(self, direction):
        """
        This method will reverse the linked list, representing the snake 'flipping' around, and also change the
        direction of the snake based on the direction that the end of the snake would be facing if it was the face. The
        new direction of the snake can be calculated by taking the difference in the x and y co-ordinates of two
        adjacent nodes and selecting the new direction based on whether the change in the x or y co-ordinates is
        either -1 or 1.

        Args:
            direction: A string which represents the direction that the snake is currently facing.

        Returns:
            new_direction: A string which represents the direction that the snake will be facing next.
        """
        pass  # TODO: Remove this line on implementing functionality


class BodyNode:
    """
    The node class, used as the nodes within the linked list.
    """

    def __init__(self, x, y):
        """
        Initialise a node for the linked list, passing in the x and y co-ordinates of where the node should be located.

        Args:
            x: The x co-ordinate of where the node will be located.
            y: The y co-ordinate of where the node will be located.
        """
        self.x = x
        self.y = y
        self.next = None

    def draw(self, screen, colour, direction, head):
        """
        Draw the node as a square onto the screen given a colour. The node can also be drawn as the head, in which
        case the eyes of the snake have to be located at the correct locations within the square.

        Args:
            screen: The screen object used to draw polygons onto.
            colour: The colour of the node, which is given as an RGB value in tuple format.
            direction: A string representing the direction that the snake is facing.
            head: Boolean on whether the node we are drawing is the head or not.
        """
        pygame.draw.rect(screen, colour, [self.x*30+10, self.y*30+10, 30, 30])

        if head:  # If the current node we are drawing is the head of the snake
            if direction == "left":
                pygame.draw.ellipse(screen, white, [self.x*30+12, self.y*30+14, 10, 10])
                pygame.draw.ellipse(screen, white, [self.x*30+12, self.y*30+26, 10, 10])
                pygame.draw.ellipse(screen, black, [self.x*30+13, self.y*30+17, 4, 4])
                pygame.draw.ellipse(screen, black, [self.x*30+13, self.y*30+29, 4, 4])
            elif direction == "right":
                pygame.draw.ellipse(screen, white, [self.x*30+28, self.y*30+14, 10, 10])
                pygame.draw.ellipse(screen, white, [self.x*30+28, self.y*30+26, 10, 10])
                pygame.draw.ellipse(screen, black, [self.x*30+33, self.y*30+17, 4, 4])
                pygame.draw.ellipse(screen, black, [self.x*30+33, self.y*30+29, 4, 4])
            elif direction == "up":
                pygame.draw.ellipse(screen, white, [self.x*30+14, self.y*30+12, 10, 10])
                pygame.draw.ellipse(screen, white, [self.x*30+26, self.y*30+12, 10, 10])
                pygame.draw.ellipse(screen, black, [self.x*30+17, self.y*30+13, 4, 4])
                pygame.draw.ellipse(screen, black, [self.x*30+29, self.y*30+13, 4, 4])
            elif direction == "down":
                pygame.draw.ellipse(screen, white, [self.x*30+14, self.y*30+28, 10, 10])
                pygame.draw.ellipse(screen, white, [self.x*30+26, self.y*30+28, 10, 10])
                pygame.draw.ellipse(screen, black, [self.x*30+17, self.y*30+33, 4, 4])
                pygame.draw.ellipse(screen, black, [self.x*30+29, self.y*30+33, 4, 4])

    def __str__(self):
        """
        Allows you to debug the location of the node by including print(node) in the LinkedBody methods.

        Returns:
            str: String of the x and y co-ordinate locations of where the node currently is.
        """
        return "<Node location: ({},{})>".format(self.x, self.y)


class Apple:
    """
    The apple class is the object that the snake will be eating. There are three different types of apples: 'add' which
    will add a node to the snake, 'remove' which will shrink the snake, and 'reverse' which will reverse the snake.
    """

    def __init__(self, locations=None, appletype=None):
        """
        Initialise the apple for the snake to eat on the screen. The location of the apple is random unless specified,
        and the type of the apple is random is random unless specified. The type 'add' has a probability of 50% of
        being chosen, with the other types of apples both having a probability of 25%.

        Args:
            locations: A list of locations where the snake is allowed to spawn. Default is set to None.
            appletype: The type of apple to spawn given as a string. Default is set to None ('add').
        """
        if not locations:
            self.x = random.randint(0, 19)
            self.y = random.randint(0, 19)
        else:
            location = random.choice(locations)
            self.x = location[0]
            self.y = location[1]

        if not appletype:
            rngType = random.randint(0, 3)

            if 1 >= rngType >= 0:
                self.type = "add"
            elif rngType == 2:
                self.type = "remove"
            else:  # Last remaining possibility
                self.type = "reverse"
        else:  # Given a chosen type to make the apple
            self.type = appletype

    def location(self):
        """
        This method returns the location of the apple so it can be used to see if the apple has been eaten by the snake.

        Returns: A tuple with the x and y co-ordinates of the apple.
        """
        return (self.x, self.y)

    def draw(self, screen):
        """
        This method will draw the apple onto the screen. This method has two parts: drawing the circle onto the
        screen, and then returning the leaf (a ellipse that is rotated) back to the main code so that it can draw the
        leaf at the correct spot on the screen.

        Args:
            screen: The screen object used to draw polygons onto.

        Returns:
            leafSurface: A surface object containing a rotated ellipse that will be drawn onto the screen on top of the
                         apple.
            (x, y): The screen co-ordinates of where the leaf needs to be drawn.
        """
        leafSurface = pygame.Surface((80, 80), pygame.SRCALPHA, 32)
        pygame.draw.ellipse(leafSurface, forestGreen, [10, 10, 25, 15])
        leafSurface = pygame.transform.rotate(leafSurface, 45)

        if self.type == "add":
            pygame.draw.ellipse(screen, red, [self.x*30+10, self.y*30+10, 30, 30])
        elif self.type == "remove":
            pygame.draw.ellipse(screen, black, [self.x*30+10, self.y*30+10, 30, 30])
        else:  # Option for reversing the snake
            pygame.draw.ellipse(screen, blue, [self.x*30+10, self.y*30+10, 30, 30])

        return leafSurface, (self.x*30, self.y*30-40)
