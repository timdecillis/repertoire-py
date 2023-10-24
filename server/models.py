from database import collection

def create_user (email, password):
   data = {email: email, password: password}
   result = collection.insert_one(data)
   return result.inserted_id

def save_song (req):
   email = req['email']
   song = req['song']
   artist = req['artist']

   found_user = collection.find_one({'email': email})
   if found_user:
      found_user['songs'].append({
         'name': song,
         'artist': artist,
         'completed': False,
         'notes': ''
         })
      collection.update_one({'email': email}, {'$set': found_user})

def get_songs (email):
   found_user = collection.find_one({email: email})
   if found_user:
      return found_user

def delete_song (email, song, artist):
   found_user = collection.find_one({email: email})
   if found_user:
      found_user.songs = [s for s in found_user.songs if not (s['name'] == song and s['artist'] == artist)]
      found_user.save()