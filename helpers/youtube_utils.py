import streamlit as st
from pytube import extract
from youtube_transcript_api import (
    YouTubeTranscriptApi, YouTubeRequestFailed, VideoUnavailable, InvalidVideoId, TooManyRequests,
    TranscriptsDisabled, NoTranscriptAvailable, NotTranslatable, TranslationLanguageNotAvailable,
    CookiePathInvalid, CookiesInvalid, FailedToCreateConsentCookie, NoTranscriptFound
)

@st.cache_data
def extract_video_id_from_url(url):
    try:
        return extract.video_id(url)
    except Exception:
        st.error("Please provide a valid YouTube URL.")
        example_urls = [
            'http://youtu.be/SA2iWivDJiE',
            'http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu'
        ]
        st.info("Here are some valid formats: " + " ,".join(example_urls))
        st.stop()

@st.cache_data
def get_transcript_text(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([item["text"] for item in transcript])
    except (YouTubeRequestFailed, VideoUnavailable, InvalidVideoId, TooManyRequests, NoTranscriptAvailable, NotTranslatable,
            TranslationLanguageNotAvailable, CookiePathInvalid, CookiesInvalid, FailedToCreateConsentCookie):
        st.error("An error occurred while fetching the transcript. Please try another video.")
        st.stop()    
    except TranscriptsDisabled:
        st.error("Subtitles are disabled for this video. Please try another video.")
        st.stop()
    except NoTranscriptFound:
        st.error("The video doesn't have English subtitles. Please ensure the video you're selecting is in English or has English subtitles available.")
        st.stop()
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}. Please try again.")
        st.stop()