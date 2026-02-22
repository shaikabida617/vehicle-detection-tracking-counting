class Tracker:
    def __init__(self):
        self.tracks = []
        self.id_count = 0

    def update(self, detections):
        self.tracks = []

        for det in detections:
            x1, y1, x2, y2 = det
            self.id_count += 1
            self.tracks.append([x1, y1, x2, y2, self.id_count])