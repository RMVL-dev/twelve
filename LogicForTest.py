class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

    def __repr__(self):
        return repr((self.name, self.distance, self.speed))


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)
        self.participants.sort(key=lambda r: r.speed, reverse=True)

    def start(self):
        finishers = {}
        place = 1

        while len(self.participants) != len(finishers): ## new
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance and not participant in finishers.values(): ## new
                    finishers[place] = participant
                    place += 1

        return finishers
