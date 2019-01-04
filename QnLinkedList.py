from utils.collections import LinkedList

class MusicCollection:
  def __init__(self):
    self.list = LinkedList()

  def addMusicToFront(self, newMusic):
    self.list.prepend(newMusic)

  def addMusicToBack(self, newMusic):
    self.list.append(newMusic)

  def addMusicAtPosition(self, newMusic, n):
    self.list.addAt(newMusic, n)

  def getMusicAtPosition(self, n):
    return self.list.getAt(n)

  def removeMusicAtPosition(self, n):
    self.list.removeAt(n)

  def displayMusic(self, printStrategy):
    for i, music in enumerate(self.list.toArray()):
      printStrategy(music, i)

  def sortBy(self, attr, order='asc'):
    def compare(a, b):
      if getattr(a, attr) < getattr(b, attr):
        if order == 'asc':
          return -1
        else:
          return 1
      elif(getattr(a, attr) > getattr(b, attr)):
        if order == 'asc':
          return 1
        else:
          return -1
      else:
        return 0
    return self.list.sort(compare)

  def sortByArtistName(self, order='asc'):
    return self.sortBy('artist', order)

  def sortByMusicTitle(self, order='asc'):
    return self.sortBy('title', order)

class Music:
  def __init__(self, artist, musicTitle):
    self.artist = artist
    self.title = musicTitle


def main():
  musics = [
    Music('U2', 'Ultraviolet (Light My Way)'),
    Music('The Killers', 'Run for Cover'),
    Music('Bowling for Soup', '1985'),
    Music('Bright Eyes', 'Four Winds'),
    Music('Coldplay', 'Everglow'),
    Music('Eagles', 'Hotel California')
  ]

  def printListTitleByArtist(music, i):
    print('{0}. {1} by {2}'.format(i+1, music.title, music.artist))

  def printListArtistTitle(music, i):
    print('{0}. {2} - {1}'.format(i+1, music.title, music.artist))

  musicCollection = MusicCollection()
  musicCollection.addMusicToFront(musics[0])
  musicCollection.addMusicToBack(musics[1])
  musicCollection.addMusicToBack(musics[2])
  musicCollection.addMusicToFront(musics[3])
  musicCollection.addMusicAtPosition(musics[4], 3)
  musicCollection.addMusicAtPosition(musics[5], 2)

  print('Music Collection in current order:')
  musicCollection.displayMusic(printListArtistTitle)
  print('\n')
  print('Music Collection sorted by "Artist Name" in "ascending" order:')
  musicCollection.sortByArtistName(order='asc')
  musicCollection.displayMusic(printListArtistTitle)
  print('\n')
  print('Music Collection sorted by "Artist Name" in "descending" order:')
  musicCollection.sortByArtistName(order='desc')
  musicCollection.displayMusic(printListArtistTitle)

  print('\n')
  print('Music Collection sorted by "Music Title" in "descending" order:')
  musicCollection.sortByMusicTitle(order='asc')
  musicCollection.displayMusic(printListTitleByArtist)
  print('\n')
  print('Music Collection sorted by "Music Title" in "descending" order:')
  musicCollection.sortByMusicTitle(order='desc')
  musicCollection.displayMusic(printListTitleByArtist)

  print('\n')
  posToRemove = 2
  musicToRemove = musicCollection.getMusicAtPosition(posToRemove)
  print('Remove "{} by {}" at position {}:'.format(musicToRemove.title, musicToRemove.artist, posToRemove))
  musicCollection.removeMusicAtPosition(posToRemove)
  musicCollection.displayMusic(printListArtistTitle)