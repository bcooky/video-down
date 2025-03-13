from pytube import YouTube

def download_video(url):
    try:
        # YouTube অবজেক্ট তৈরি
        yt = YouTube(url)
        
        # ভিডিও তথ্য দেখানো
        print(f"Downloading: {yt.title}")
        print(f"Duration: {yt.length} seconds")
        
        # সর্বোচ্চ রেজোলিউশনে ভিডিও ডাউনলোড
        stream = yt.streams.get_highest_resolution()
        stream.download()
        
        print("Download Completed!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    video_url = input("Enter the video URL: ")
    download_video(video_url)
