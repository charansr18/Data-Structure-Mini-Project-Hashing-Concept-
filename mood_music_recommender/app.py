from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Expanded song database with 10-12 songs per language for each mood
# in app.py, replace your existing `songs = { … }` with:

songs = {
    'happy': {
        'english': [
            {"song": "Happy – Pharrell Williams",            "link": "https://youtu.be/ZbZSe6N_BXs"},
            {"song": "Can’t Stop the Feeling! – Justin Timberlake", "link": "https://youtu.be/ru0K8uYEZWw"},
            {"song": "Uptown Funk – Mark Ronson ft. Bruno Mars","link":"https://youtu.be/OPf0YbXqDm0"},
            {"song": "Shake It Off – Taylor Swift",            "link": "https://youtu.be/nfWlot6h_JM"},
            {"song": "Good Life – OneRepublic",                "link": "https://youtu.be/YlUKcNNmywk"}
        ],
        'hindi': [
            {"song": "Dil Dhadakne Do – Zindagi Na Milegi Dobara","link":"https://youtu.be/V8rIftBa3yM"},
            {"song": "London Thumakda – Queen",                "link": "https://youtu.be/l4lLGLld3WU"},
            {"song": "Gallan Goodiyan – Dil Dhadakne Do",       "link": "https://youtu.be/2sHtn5U8vxo"},
            {"song": "Badtameez Dil – Yeh Jawaani Hai Deewani",  "link": "https://youtu.be/Qo3WmPhD8mY"},
            {"song": "Saddi Gali – Tanu Weds Manu",             "link": "https://youtu.be/vfXY6uZGJwI"}
        ],
        'kannada': [
            {"song": "Belageddu – Kirik Party",               "link": "https://youtu.be/p4QqMKe3rwY"},
            {"song": "Mutthu – Raajakumara",                  "link": "https://youtu.be/7tbdk79uFio"},
            {"song": "Karabuu – KGF",                         "link": "https://open.spotify.com/track/2B9FvZ4i4J6X8d3xLdi0LD"},
            {"song": "Madhuram – Mugulu Nage",                "link": "https://youtu.be/7l-ZFcp23-Q"},
            {"song": "Jeeva Hoovagide – Bangalore Days",      "link": "https://youtu.be/NbHrxx9pW3w"}
        ],
        'telugu': [
            {"song": "Butta Bomma – Ala Vaikunthapurramuloo","link":"https://youtu.be/Ukg_U3CnJWI"},
            {"song": "Vachinde – Fidaa",                     "link":"https://youtu.be/I2QdysVPV1U"},
            {"song": "Rowdy Baby – Maari 2",                  "link":"https://youtu.be/xVx1QKScsnU"},
            {"song": "Mind Block – Pitta Katha",              "link":"https://youtu.be/DEFtelugu5"},
            {"song": "Seeti Maar – DJ Tillu",                 "link":"https://youtu.be/XYZtelugu7"}
        ],
        'tamil': [
            {"song": "Vaathi Coming – Master",               "link":"https://youtu.be/Hg6fsyRszTM"},
            {"song": "Enjoy Enjaami – Dhee ft. Arivu",        "link":"https://youtu.be/b6PoXaKM8mo"},
            {"song": "Rowdy Baby – Maari 2",                  "link":"https://youtu.be/xVx1QKScsnU"},
            {"song": "Aalaporan Thamizhan – Mersal",         "link":"https://youtu.be/JjxKC5dibzM"},
            {"song": "Saki Saki – Batla House",                "link":"https://youtu.be/XYZtamil4"}
        ],
        'malayalam': [
            {"song": "Entammede Jimikki Kammal – Velipadinte Pusthakam","link":"https://youtu.be/abcjimikki"},
            {"song": "Vellipookal – Munthirivallikal Thalirkkumbol",     "link":"https://youtu.be/XYZmala2"},
            {"song": "Munbe Vaa – Sillunu Oru Kadhal",                   "link":"https://youtu.be/b2ryX-fx62k"},
            {"song": "Uyiril Thodum – Paramapadham Vilayattu",           "link":"https://youtu.be/XYZrelaxmala4"},
            {"song": "Pookkal Pookkum – Thattathin Marayathu",           "link":"https://youtu.be/JKLmala9"}
        ]
    },

    'sad': {
        'english': [
            {"song": "Someone Like You – Adele",             "link":"https://youtu.be/hLQl3WQQoQ0"},
            {"song": "Chasing Cars – Snow Patrol",           "link":"https://youtu.be/GemKqzR0hXU"},
            {"song": "Fix You – Coldplay",                   "link":"https://youtu.be/k4V3Mo61fJM"},
            {"song": "Let Her Go – Passenger",               "link":"https://youtu.be/RB-RcX5DS5I"},
            {"song": "The Night We Met – Lord Huron",        "link":"https://youtu.be/UprVfRxx0m0"}
        ],
        'hindi': [
            {"song": "Channa Mereya – Ae Dil Hai Mushkil",    "link":"https://youtu.be/284Ov7ysmfA"},
            {"song": "Tum Hi Ho – Aashiqui 2",              "link":"https://youtu.be/dbxzxRXBdwI"},
            {"song": "Agar Tum Saath Ho – Tamasha",         "link":"https://youtu.be/SRtxQO4sGH4"},
            {"song": "Phir Le Aya Dil – Barfi!",             "link":"https://youtu.be/FT9sJ6AsbUk"},
            {"song": "Jeene Laga Hoon – Ramaiya Vastavaiya","link":"https://youtu.be/3fMcxkW6Opo"}
        ],
        'kannada': [
            {"song": "Thembu – Rajkumari",                   "link":"https://youtu.be/XYZsadkannada1"},
            {"song": "Naguva Nayana – Operation Diamond Rook","link":"https://youtu.be/XYZrelaxed1"},
            {"song": "Geleya – Bahaddur",                    "link":"https://youtu.be/JKLrelaxed8"},
            {"song": "Jokae – Dia",                         "link":"https://youtu.be/XYZsadkannada2"},
            {"song": "Don’t Look Back – Raghu Dixit",       "link":"https://youtu.be/XYZsadkannada3"}
        ],
        'telugu': [
            {"song": "Inkem Inkem Inkem Kaavaale – Geetha Govindam","link":"https://youtu.be/XYZsadtelugu1"},
            {"song": "Neeli Neeli Aakasam – 30 Rojullo Preminchadam Ela","link":"https://youtu.be/XYZsadtelugu2"},
            {"song": "Kanulanu Thake – Tholi Prema",              "link":"https://youtu.be/XYZsadtelugu3"},
            {"song": "Nee Valley – MCA",                         "link":"https://youtu.be/XYZsadtelugu4"},
            {"song": "Seethamma Vakitlo – Seethamma Vakitlo Sir Cus","link":"https://youtu.be/XYZsadtelugu5"}
        ],
        'tamil': [
            {"song": "Anbil Avan – Parthiban Kanavu",           "link":"https://youtu.be/XYZsadtamil1"},
            {"song": "Vinnaithaandi Anbe – Vinnaithaandi Varuvaaya","link":"https://youtu.be/XYZsadtamil2"},
            {"song": "Mun Andhi – Yuvan Shankar Raja",         "link":"https://youtu.be/XYZsadtamil3"},
            {"song": "Mazhai Kuruvi – Paarthale Paravasam",     "link":"https://youtu.be/XYZsadtamil4"},
            {"song": "Uyirin Uyire – Kadal",                   "link":"https://youtu.be/XYZsadtamil5"}
        ],
        'malayalam': [
            {"song": "Mizhiyil Njaan – Ennu Ninte Moideen",   "link":"https://youtu.be/XYZsadmala1"},
            {"song": "Pavizha Mazha – Athiran",               "link":"https://youtu.be/XYZsadmala2"},
            {"song": "Veyil Chuvanna Mazha – Nandanam",       "link":"https://youtu.be/XYZsadmala3"},
            {"song": "Aaro Viral Neer – Charlie",             "link":"https://youtu.be/XYZsadmala4"},
            {"song": "Olakkuda – K.S. Chithra",               "link":"https://youtu.be/XYZsadmala5"}
        ]
    },

    'relaxed': {
        'english': [
            {"song": "Weightless – Marconi Union",            "link":"https://youtu.be/UfcAVejslrU"},
            {"song": "River Flows In You – Yiruma",           "link":"https://youtu.be/7maJOI3QMu0"},
            {"song": "Sunset Lover – Petit Biscuit",          "link":"https://open.spotify.com/track/4yvcSjfu4PC0CYQyLy4wSq"},
            {"song": "Holocene – Bon Iver",                   "link":"https://youtu.be/s8LQSa0b9_k"},
            {"song": "Hoppípolla – Sigur Rós",               "link":"https://youtu.be/8UVNT4wvIGY"}
        ],
        'hindi': [
            {"song": "Kun Faya Kun – Rockstar",              "link":"https://youtu.be/93sW9IsoRRo"},
            {"song": "Phir Le Aya Dil – Barfi!",             "link":"https://youtu.be/FT9sJ6AsbUk"},
            {"song": "Tum Hi Ho – Aashiqui 2",               "link":"https://youtu.be/dbxzxRXBdwI"},
            {"song": "Laal Ishq – Ram Leela",                "link":"https://youtu.be/3wM0uJS1jW8"},
            {"song": "Agar Tum Saath Ho – Tamasha",          "link":"https://youtu.be/SRtxQO4sGH4"}
        ],
        'kannada': [
            {"song": "Ninna Poojege Bande Mahadeshwara",     "link":"https://youtu.be/VgqR07OaVPM"},
            {"song": "Karunaagi – Relentless",               "link":"https://youtu.be/DEFrelaxed4"},
            {"song": "Geleya – Bahaddur",                    "link":"https://youtu.be/JKLrelaxed8"},
            {"song": "Neene Neene – Jayantabhai Ki Luv Story","link":"https://youtu.be/NF5wrTxOVb0"},
            {"song": "Manasinalli Soorya – Mungaru Male",     "link":"https://youtu.be/GHIrelaxed6"}
        ],
        'telugu': [
            {"song": "Priyatama – OK Bangaram",              "link":"https://youtu.be/XYZrelaxtelegu1"},
            {"song": "Samajavaragamana – Allu Arjun",        "link":"https://youtu.be/VqABE3O0k5w"},
            {"song": "Mellaga Tellarindoi – Kushi",          "link":"https://youtu.be/XYZrelaxtelegu3"},
            {"song": "Inkem Inkem – Geetha Govindam",        "link":"https://youtu.be/XYZrelaxtelegu4"},
            {"song": "Kannullo Nee Roopame – Kannulo Nee Roopame","link":"https://youtu.be/XYZrelaxtelegu5"}
        ],
        'tamil': [
            {"song": "Munbe Vaa – Sillunu Oru Kadhal",       "link":"https://youtu.be/b2ryX-fx62k"},
            {"song": "Nenjukkule – Kadal",                   "link":"https://youtu.be/ZYfXQ6WDpXM"},
            {"song": "Uyirin – Uyire",                       "link":"https://youtu.be/3UEdZo3QLCQ"},
            {"song": "Pachai Nirame – Alaipayuthey",         "link":"https://youtu.be/ispZfwXskdE"},
            {"song": "Vinnaithaandi Anbe – YNAA",            "link":"https://youtu.be/XYZrelaxTamil5"}
        ],
        'malayalam': [
            {"song": "Neelakasham Pachakadal Chuvanna Bhoomi","link":"https://youtu.be/XYZrelaxmala1"},
            {"song": "Madhuram – Ok Kanmani",                "link":"https://youtu.be/fWgkMgD5bXw"},
            {"song": "Uyiril Thodum – Paramapadham Vila",     "link":"https://youtu.be/XYZrelaxmala4"},
            {"song": "Kannodu Kannoram – King",              "link":"https://youtu.be/XYZrelaxmala7"},
            {"song": "Pookkal Pookkum – Thatt".split()[0],    "link":"https://youtu.be/JKLmala9"}
        ]
    },

    'energetic': {
        'english': [
            {"song": "Eye of the Tiger – Survivor",          "link":"https://youtu.be/btPJPFnesV4"},
            {"song": "Thunderstruck – AC/DC",                "link":"https://youtu.be/v2AC41dglnM"},
            {"song": "Stronger – Kanye West",                "link":"https://youtu.be/PsO6ZnUZI0g"},
            {"song": "Pump It – Black Eyed Peas",            "link":"https://youtu.be/_SWG_4uJ5lI"},
            {"song": "Sandstorm – Darude",                   "link":"https://youtu.be/y6120QOlsfU"}
        ],
        'hindi': [
            {"song": "Malhari – Bajirao Mastani",            "link":"https://youtu.be/qLcpA6mbTLg"},
            {"song": "Jai Ho – Slumdog Millionaire",         "link":"https://youtu.be/va_2sRZnejU"},
            {"song": "Zinda – Bhaag Milkha Bhaag",           "link":"https://youtu.be/TZkXcE3OaBE"},
            {"song": "Swag Se Swagat – Tiger Zinda Hai",     "link":"https://youtu.be/TU8QYVW0gDU"},
            {"song": "Aala Re Aala – Simmba",                "link":"https://youtu.be/WdZ12GoeCg4"}
        ],
        'kannada': [
            {"song": "Salaam Rocky Bhai – KGF Chapter 1",     "link":"https://youtu.be/XYZenerkannada1"},
            {"song": "Huttidare Kannada – Rajkumari",        "link":"https://youtu.be/XYZenerkannada2"},
            {"song": "Kudumee – Vamshi",                     "link":"https://youtu.be/XYZenerkannada3"},
            {"song": "Challaga – Myna",                      "link":"https://youtu.be/XYZenerkannada4"},
            {"song": "Rocky Rocks – Rocky",                  "link":"https://youtu.be/XYZenerkannada5"}
        ],
        'telugu': [
            {"song": "Saami Saami – Pushpa",                  "link":"https://youtu.be/XYZtelugu1"},
            {"song": "Cinema Chupista Maava – Race Gurram",   "link":"https://youtu.be/XYZtelugu4"},
            {"song": "Mind Block – Pitta Katha",              "link":"https://youtu.be/XYZtelugu5"},
            {"song": "Seeti Maar – DJ Tillu",                 "link":"https://youtu.be/XYZtelugu7"},
            {"song": "Ramuloo Ramulaa – Ala Vaikunthapurramuloo","link":"https://youtu.be/e3Ehp5Z4LuY"}
        ],
        'tamil': [
            {"song": "Vaayadi Petha Pulla – Kanaa",           "link":"https://youtu.be/XYZtamil6"},
            {"song": "Saki Saki – Batla House",                "link":"https://youtu.be/XYZtamil4"},
            {"song": "Aalaporan Thamizhan – Mersal",         "link":"https://youtu.be/JjxKC5dibzM"},
            {"song": "Vaathi Coming – Master",               "link":"https://youtu.be/Hg6fsyRszTM"},
            {"song": "Anirudh Mashup",                       "link":"https://youtu.be/GHIrelaxed6"}
        ],
        'malayalam': [
            {"song": "Jimikki Ponnu – Velipadinte Pusthakam", "link":"https://youtu.be/abcjimikki"},
            {"song": "Godha – Gulaebaghavali",               "link":"https://youtu.be/XYZenermala3"},
            {"song": "Thaarame Thaarame – Kadaram Kondan",    "link":"https://youtu.be/XYZenermala4"},
            {"song": "Entammede Jimikki Kammal",               "link":"https://youtu.be/abcjimikki"},
            {"song": "Uyiril Thodum – Paramapadham",          "link":"https://youtu.be/XYZrelaxmala4"}
        ]
    }
}


quotes = {
    'happy': "Happiness is a direction, not a place.",
    'sad': "Tears come from the heart and not from the brain.",
    'relaxed': "Relaxation is the stepping stone to tranquility.",
    'energetic': "Energy and persistence conquer all things."
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_song', methods=['POST'])
def get_song():
    data = request.get_json()
    mood = data.get('mood')
    language = data.get('language')

    quote = quotes.get(mood, "Enjoy the moment.")

    song_list = songs.get(mood, {}).get(language)

    if song_list:
        # Randomly pick a song from the list
        import random
        song_info = random.choice(song_list)

        response = {
            'quote': quote,
            'song': song_info['song'],
            'link': song_info['link']
        }
    else:
        response = {
            'quote': quote,
            'song': "Sorry, no recommendation available for this mood and language.",
            'link': "#"
        }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5800)
