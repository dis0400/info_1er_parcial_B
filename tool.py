import arcade
import random
from typing import Protocol, Union

class Tool(Protocol):
    name: str
    def draw_traces(self, traces: list[list[int]]):
        pass

    def get_name(self):
        return self.name

class PencilTool(Tool):
    name = "PENCIL"

    def __init__(self, size):
        self.size = size

    def draw_traces(self, traces: list[dict[str, Union[str, list[tuple[int, int]]]]]):
        for trace in traces:
            if trace["tool"] == self.name:
                arcade.draw_line_strip(trace["trace"], trace["color"], self.size)

class MarkerTool(Tool):
    name = "MARKER"

    def __init__(self, size):
        self.thickness = size

    def draw_traces(self, traces: list[dict[str, Union[str, list[tuple[int, int]]]]]):
        for trace in traces:
            if trace["tool"] == self.name:
                for point in trace["trace"]:
                    arcade.draw_circle_filled(point[0], point[1], self.thickness, trace["color"])

class SprayTool(Tool):
    name = "SPRAY"

    def __init__(self, size):
        self.radius = size * 2  
        self.density = size * 5  
    def draw_traces(self, traces: list[dict[str, Union[str, list[tuple[int, int]]]]]):
        for trace in traces:
            if trace["tool"] == self.name:
                for point in trace["trace"]:
                    for _ in range(self.density):
                        offset_x = random.randint(-self.radius, self.radius)
                        offset_y = random.randint(-self.radius, self.radius)
                        arcade.draw_point(point[0] + offset_x, point[1] + offset_y, trace["color"], 1)

class EraserTool(Tool):
    name = "ERASER"

    def __init__(self, size):
        self.size = size * 5 

    def draw_traces(self, traces: list[dict[str, Union[str, list[tuple[int, int]]]]]):
        
        pass

    def erase(self, x: int, y: int, traces: list[dict[str, Union[str, list[tuple[int, int]]]]]):
        new_traces = []
        for trace in traces:
            if not any(x - self.size <= point[0] <= x + self.size and
                       y - self.size <= point[1] <= y + self.size
                       for point in trace["trace"]):
                new_traces.append(trace)
        return new_traces
