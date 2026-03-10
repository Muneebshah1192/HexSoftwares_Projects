from flask import Flask, render_template, request
import pickle
import pandas as pd
import random

app = Flask(__name__)
music_dict = pickle.load(open('music_dict.pkl', 'rb'))
music_df = pd.DataFrame(music_dict)
similarity_deep = pickle.load(open('similarity_deep.pkl', 'rb'))

def recommend(song_name):
    try:
        song_index = music_df[music_df['track_name'] == song_name].index[0]
        
       
        top_30_indices = similarity_deep[song_index][:30]
        selected_indices = random.sample(top_30_indices, 6)
        
        recommended_songs = []
        for i in selected_indices:
            recommended_songs.append({
                'name': music_df.iloc[i].track_name,
                'artist': music_df.iloc[i].artist_name,
                'id': music_df.iloc[i].track_id
            })
        return recommended_songs
    except Exception as e:
        return []

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    selected_song = ""
    song_list = sorted(music_df['track_name'].dropna().unique().tolist())

    if request.method == 'POST':
        selected_song = request.form.get('song_name')
        recommendations = recommend(selected_song)

    return render_template('index.html', songs=song_list, recommendations=recommendations, selected_song=selected_song)

if __name__ == '__main__':
    app.run(debug=True)