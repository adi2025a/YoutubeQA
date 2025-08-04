from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    ytt_api = YouTubeTranscriptApi()

    transcript_list = ytt_api.list(video_id)

    transcript = transcript_list.find_transcript(['en']).fetch()

    return " ".join([t.text for t in transcript])