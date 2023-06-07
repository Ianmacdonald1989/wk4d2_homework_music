import pdb 
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository  
import repositories.artist_repository as artist_repository
album_repository.delete_all()
artist_repository.delete_all()




artist_1 = Artist("David", "Bowie")
artist_repository.save(artist_1)
artist = artist_repository.select_all()
artist_repository.update(artist_1)
# artist_repository.delete(artist_1)




album_1 = Album("Hunky Dory", "Rock", artist_1)
album_repository.save(album_1)
# album = album_repository.select_all()

album_1.title=("Dunky Dory")
album_repository.update(album_1)
albums = album_repository.select_all()
# album_repository.delete(album_1)


pdb.set_trace()






