from tools.computer_vision import object_detection

# Example: Use object detection tool to detect objects in an image

image_path = 'path/to/image.jpg'

results = object_detection(image_path)

print(results)

from tools.data_visualization import plot_scatter

# Example: Use data visualization tool to plot scatter plot

data = [
    {'x': 1, 'y': 2, 'label': 'A'},
    {'x': 3, 'y': 4, 'label': 'B'},
    {'x': 2, 'y': 3, 'label': 'C'},
]

plot_scatter(data, 'x', 'y', 'label')
