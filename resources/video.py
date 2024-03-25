class Video:
    def __init__(self, title, duration, resolution, format):
        self.title = title
        self.duration = duration
        self.resolution = resolution
        self.format = format

    def __repr__(self):
        return f"Video('{self.title}', {self.duration}, {self.resolution}, {self.format})"

    def get_properties(self):
        return {
            "title": self.title,
            "duration": self.duration,
            "resolution": self.resolution,
            "format": self.format
        }

    def is_compatible_with(self, player):
        return player.can_play(self.format)
