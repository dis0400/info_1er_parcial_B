import arcade
import json
import sys
import imageio
import numpy as np
from tool import PencilTool, MarkerTool, SprayTool, EraserTool

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Paint"

COLORS = {
    "black": arcade.color.BLACK,
    "red": arcade.color.RED,
    "blue": arcade.color.BLUE,
    "yellow": arcade.color.YELLOW,
    "green": arcade.color.GREEN,
}

SIZES = {
    "small": 2,
    "medium": 5,
    "large": 10,
}

class Paint(arcade.Window):
    def __init__(self, load_path: str = None):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.WHITE)
        self.tool = PencilTool(SIZES["medium"])
        self.used_tools = {self.tool.name: self.tool}
        self.color = arcade.color.BLUE
        self.tool_size = SIZES["medium"]
        self.frames = []  

        if load_path is not None:
            self.traces = self.load_drawing(load_path)
        else:
            self.traces = []

    def on_key_press(self, symbol: int, modifiers: int):
    
        if symbol == arcade.key.F:
            self.tool = PencilTool(self.tool_size)
        elif symbol == arcade.key.E:
            self.tool = EraserTool(self.tool_size)
        elif symbol == arcade.key.P:
            self.tool = MarkerTool(self.tool_size)
        elif symbol == arcade.key.S:
            self.tool = SprayTool(self.tool_size)

        elif symbol == arcade.key.R:
            self.color = arcade.color.RED
        elif symbol == arcade.key.G:
            self.color = arcade.color.GREEN
        elif symbol == arcade.key.B:
            self.color = arcade.color.BLUE
        elif symbol == arcade.key.Y:
            self.color = arcade.color.YELLOW
        elif symbol == arcade.key.K:
            self.color = arcade.color.BLACK

        elif symbol == arcade.key.KEY_1:
            self.tool_size = SIZES["small"]
        elif symbol == arcade.key.KEY_2:
            self.tool_size = SIZES["medium"]
        elif symbol == arcade.key.KEY_3:
            self.tool_size = SIZES["large"]

        if symbol == arcade.key.O:
            self.save_drawing(self.traces)
  
        if symbol == arcade.key.V:
            self.save_gif("drawing.gif")
        
        self.used_tools[self.tool.name] = self.tool
        print(f"Herramienta: {self.tool.name}, Color: {self.color}, Tamaño: {self.tool_size}")

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        print(x, y)
        if button == arcade.MOUSE_BUTTON_LEFT:
            if isinstance(self.tool, EraserTool):
                self.traces = self.tool.erase(x, y, self.traces)
            else:
                self.traces.append({"tool": self.tool.name, "color": self.color, "trace": [(x, y)], "size": self.tool_size})

    def on_mouse_drag(self, x: int, y: int, dx: int, dy: int, buttons: int, modifiers: int):
        if self.traces and not isinstance(self.tool, EraserTool):
            self.traces[-1]["trace"].append((x, y))

    def on_draw(self):
        arcade.start_render()
        for tool in self.used_tools.values():
            tool.draw_traces(self.traces)
        
        image_data = arcade.get_image().convert("RGB") 
        image_np = np.array(image_data) 
        self.frames.append(image_np)
        
    # Imagen, bash: python main.py drawing.json
    def save_drawing(self, traces, file_path="drawing.json"):
        with open(file_path, "w") as file:
            json.dump(traces, file)

    def load_drawing(self, file_path):
        with open(file_path, "r") as file:
            return json.load(file)
     # Gif, bash: start drawing.gif
    def save_gif(self, filename="drawing.gif"):
       
        with imageio.get_writer(filename, mode='I') as writer:
            for frame in self.frames:
                writer.append_data(frame)
       
                
                


if __name__ == "__main__":
    if len(sys.argv) > 1:
        app = Paint(sys.argv[1])
    else:
        app = Paint()
    arcade.run()
