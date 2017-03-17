import arrow
import os
import yaml

class Entry:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

    def to_dict(self):
        ret = {
            "name" : self.name,
            "start": self.start.timestamp
        }

        if self.end:
            ret["end"] = self.end.timestamp
        
        return ret

    def from_dict(d):
        return Entry(d["name"], arrow.get(d["start"]), arrow.get(d["end"]))

class Log:
    def __init__(self, entries=None):
        if entries is None:
            entries = []
        self.entries = entries

    def load(path=None):
        if path is None:
            path = default_path()
        with open(path, "r") as f:
            return Log(list(map(lambda d: Entry.from_dict(d), yaml.load(f))))

    def save(self, path):
        if path is None:
            path = default_path()
        with open(path, "w") as f:
            f.write(yaml.dump(list(map(lambda e: e.to_dict(), self.entries))))

def default_path():
    return os.path.join(os.environ["HOME"], ".timer.yaml")
