from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
      
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.direction_locked = False

    def create_snake(self) -> None:
        """Creating a Snake body"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self) -> None:
        """Move snake piece by piece by replaceing the first position to the next position and so on"""
        for seg_num in range(len(self.segments)-1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num-1].pos())
        self.head.forward(MOVE_DISTANCE)
        self.direction_locked = False

    def add_segment(self, position) -> None:
        """Create new snake segment"""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self) -> None:
        """Add a new segment to the snake"""
        self.add_segment(self.segments[-1].position())

    def up(self) -> None:
        """Move snake upwards"""
        if self.head.heading() != DOWN and not self.direction_locked:
            self.head.seth(UP)
            self.direction_locked = True

    def down(self) -> None:
        """Move snake downwards"""
        if self.head.heading() != UP and not self.direction_locked:
            self.head.seth(DOWN)
            self.direction_locked = True

    def left(self) -> None:
        """Move snake towards left"""
        if self.head.heading() != RIGHT and not self.direction_locked:
            self.head.seth(LEFT)
            self.direction_locked = True

    def right(self) -> None:
        """Move snake towards right"""
        if self.head.heading() != LEFT and not self.direction_locked:
            self.head.seth(RIGHT)
            self.direction_locked = True
