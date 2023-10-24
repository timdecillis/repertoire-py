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

'''
  saveSong: (req) => {
    let { email, song, artist } = req;
    return User.findOne({ email: email })
      .then((foundUser) => {
        foundUser.songs.push({
          name: song,
          artist: artist,
          completed: false,
          notes: ''
        });
        return foundUser.save();
      });
  },
  getSongs: (email) => {
    return User.findOne({ email: email })
      .exec()
      .then((foundUser) => {
        return foundUser;
      });
  },
  deleteSong: (email, song, artist) => {
    return User.findOne({ email: email })
      .then((foundUser) => {
        foundUser.songs = foundUser.songs.filter((s) => !(s.name === song && s.artist === artist));
        return foundUser.save();
      });
  },
  updateSong: (email, song, artist) => {
    const query = {email: email, 'songs.name': song, 'songs.artist': artist};
    const update = {$set: {'songs.$.completed': {$not: '$songs.$.completed'}}};
    return User.findOneAndUpdate(query, update, {new: true});
  },
  updateNotes: (email, song, artist, notes) => {
    const query = { email: email, 'songs.name': song, 'songs.artist': artist };
    const update = { $set: { 'songs.$.notes': notes } };
    return User.findOneAndUpdate(query, update, { new: true });
  }
};
'''