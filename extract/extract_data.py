import pandas as pd
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="/Users/patrickanderson/Desktop/DACSS 690A/690A Final/.env")
API_KEY = os.getenv('API_KEY')

print(f"Loaded API Key: {API_KEY}") 

def extract_trending_videos(region_code='US', max_results=50):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    request = youtube.videos().list(
        part="snippet,statistics",
        chart="mostPopular",
        regionCode=region_code,
        maxResults=max_results
    )
    response = request.execute()

    videos = []
    for item in response['items']:
        videos.append({
            'video_id': item['id'],
            'title': item['snippet']['title'],
            'category_id': item['snippet']['categoryId'],
            'publish_time': item['snippet']['publishedAt'],
            'view_count': item['statistics'].get('viewCount', 0),
            'like_count': item['statistics'].get('likeCount', 0),
            'comment_count': item['statistics'].get('commentCount', 0),
        })

    return pd.DataFrame(videos)

if __name__ == "__main__":
    df = extract_trending_videos(region_code='US', max_results=5)  # Reduce results for testing
    print(df.head())  # Display the first few rows to confirm output

