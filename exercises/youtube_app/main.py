import json
import time

import requests
from flask import Flask, render_template
from numerize.numerize import numerize

CHANNELS = {
    'freeCodeCamp': 'UC8butISFwT-Wl7EV0hUK0BQ',
    'CleverProgrammer': 'UCqrILQNl5Ed9Dz6CGMyvMTQ',
    'TWT': 'UC4JX40jDee_tINbkjycV4Sg'
}

# TODO: Replace NONE with  your API key below
headers = {
    "X-RapidAPI-Key": None,
    "X-RapidAPI-Host": "youtube-media-downloader.p.rapidapi.com"
}

def query_youtube_for_video_data(channel_id, headers=headers) -> json:
    """
    This function will query YouTube for the last 30 videos and return the data as a json
    :param channel_id: Channel ID of the channel to be queried
    :return: Last 30 videos as JSON data
    """
    endpoint_video_url = "https://youtube-media-downloader.p.rapidapi.com/v2/channel/videos"

    querystring = {"channelId": channel_id}

    video_response = requests.request("GET", endpoint_video_url, headers=headers, params=querystring)
    video_response = video_response.json()
    video_data = video_response['items']
    # Here is how you would extract the video id and its title for the video_data:
    # video_ids = [video['id'] for video in video_data]
    # video_titles = [video['title'] for video in video_data]
    # or i in range(len(video_data)):
    #    print(f'Video ID: ' + video_ids[i] + ': Title= ' + video_titles[i])
    return video_data


def query_youtube_for_channel_data(channel_id, headers=headers) -> json:
    """
    This function is used to query the channel data of a given ID and returns it as a JSON
    :param channel_id: Channel ID of the channel to be queried
    :return: Channel data as a JSON
    """
    endpoint_channel_url = "https://youtube-media-downloader.p.rapidapi.com/v2/channel/details"

    querystring = {"channelId": channel_id}
    channel_response = requests.request("GET", endpoint_channel_url, headers=headers, params=querystring)
    channel_data = channel_response.json()
    return channel_data


app = Flask(__name__, template_folder='templates')

# Youtube response datastructure
# as of 05.04.2023
'''example_data = { 'status': True, 'nextToken': 'loooooooong string we do not care about', 'items': [ {'type': 
'video', 'id': 'MsnQ5uepIaE', 'title': 'Frontend Web Development: In-Depth Project Tutorial (HTML, CSS, JavaScript, 
TypeScript, React)', 'isLiveNow': False, 'lengthTest': '10:02:10', 'viewCountText': '44,871 views', 
'publishedTimeText': '14 hours ago', 'thumbnails': [ { 'url': 
'https://i.ytimg.com/vi/MsnQ5uepIaE/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVPKriqkDDggBFQAAiEIYAXABwAEG&rs
=AOn4CLD4Okt9SPRD8MLJBwE0dF2i8A2r1w', 'width': 168, 'height': 94, 'moving': False }, { 'url': 
'https://i.ytimg.com/vi/MsnQ5uepIaE/hqdefault.jpg?sqp=-oaymwEbCMQBEG5IVPKriqkDDggBFQAAiEIYAXABwAEG&rs
=AOn4CLBja0zrtmJRUGrADRA7XTotVQe03w', 'width': 196, 'height': 110, 'moving': False } ] }, {'type': 'video', 
'id': 'lFo3Yy8Ro7w', 'title': 'Learn Minimal APIs in .NET 7', 'isLiveNow': False, 'lengthTest': '1:40:27', 
'viewCountText': '19,886 views', 'publishedTimeText': '1 day ago', 'thumbnails': [ { 'url': 
'https://i.ytimg.com/vi/lFo3Yy8Ro7w/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVPKriqkDDggBFQAAiEIYAXABwAEG&rs
=AOn4CLDUSqpDegNQFdWbMXkG3u9VhfYL9A', 'width': 168, 'height': 94, 'moving': False }, { 'url': 
'https://i.ytimg.com/vi/lFo3Yy8Ro7w/hqdefault.jpg?sqp=-oaymwEbCMQBEG5IVPKriqkDDggBFQAAiEIYAXABwAEG&rs
=AOn4CLBYFm1n94twckONmzLNklnChMThZg', 'width': 196, 'height': 110, 'moving': False } ]

        }
    ]
}
'''


@app.route('/')
def index():
    active_id = CHANNELS['CleverProgrammer']
    videos = query_youtube_for_video_data(active_id)
    time.sleep(1.1)
    channel = query_youtube_for_channel_data(active_id)
    return render_template('index.html', videos=videos, channel=channel)


@app.route('/fcc')
def get_fcc_data():
    active_id = CHANNELS['freeCodeCamp']
    videos = query_youtube_for_video_data(active_id)
    time.sleep(1.1)
    channel = query_youtube_for_channel_data(active_id)
    return render_template('fcc.html', videos=videos, channel=channel)


@app.route('/twt')
def get_twt_data():
    active_id = CHANNELS['TWT']
    videos = query_youtube_for_video_data(active_id)
    time.sleep(1.1)
    channel = query_youtube_for_channel_data(active_id)
    return render_template('twt.html', videos=videos, channel=channel)


@app.route('/cp')
def get_cp_data():
    active_channel = CHANNELS['CleverProgrammer']
    videos = query_youtube_for_video_data(active_channel)
    time.sleep(1.1)
    channel = query_youtube_for_channel_data(active_channel)
    return render_template('cp.html', videos=videos, channel=channel)


@app.template_filter()
def numberize(view_count_text: str) -> str:
    number_to_cast = ''
    numbers_text = view_count_text.split()
    for number_str in numbers_text[0]:
        if number_str.isdigit():
            number_to_cast += number_str

    result = ''
    try:
        view_count = int(number_to_cast)
        result = numerize(view_count, 1)
    except [TypeError]:
        print(TypeError)

    result = result + ' views'
    return result


@app.template_filter()
def highest_quality_thumbnail(thumbnails) -> str:
    if len(thumbnails) >= 4:
        img_src = thumbnails[3]['url']
    elif len(thumbnails) == 3:
        img_src = thumbnails[2]['url']
    elif len(thumbnails) == 2:
        img_src = thumbnails[1]['url']
    else:
        img_src = thumbnails[0]['url']
    return img_src


app.run('0.0.0.0', 81)
