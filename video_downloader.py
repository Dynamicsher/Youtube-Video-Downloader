from yt_dlp import YoutubeDL

link = input("Enter YouTube URL: ")

choice = input("Download type (video/audio): ").lower()

# AUDIO DOWNLOAD

if choice == "audio":
    options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with YoutubeDL(options) as ydl:
        ydl.download([link])

    print("Audio download complete!")

# VIDEO DOWNLOAD

elif choice == "video":

    # First: extract info to show formats
    with YoutubeDL() as ydl:
        info = ydl.extract_info(link, download=False)

    print("\nAvailable formats:\n")
    formats = info['formats']

    for f in formats:
        if f.get('height') and f.get('ext') == 'mp4':
            print(f"ID: {f['format_id']} | {f['ext']} | {f['height']}p")

    fmt_id = input("\nEnter format ID you want: ")

    options = {
        'format': fmt_id + 'bestaudio/best'
    }

    with YoutubeDL(options) as ydl:
        ydl.download([link])

    print("Video download complete!")

else:
    print("Invalid choice! Please enter 'video' or 'audio'.")