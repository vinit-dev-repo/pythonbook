class Playlist:
    def __init__(self, songs):
        self._songs = list(songs)

    def __len__(self):
        return len(self._songs)

    def __getitem__(self, index):
        if isinstance(index, slice):
            # index is a slice object — return a new Playlist
            return Playlist(self._songs[index])
        return self._songs[index]

    def __repr__(self):
        return f"Playlist({self._songs})"

pl = Playlist(["Song A", "Song B", "Song C", "Song D"])
print(pl[1])          # a plain int index
print(pl[1:3])         # a slice — returns a Playlist, not a bare list
