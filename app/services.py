from yt_dlp import YoutubeDL
import os

def download_videos(urls, download_path, quality):
    quality_settings = {
        'best': 'bestvideo+bestaudio/best',
        'worst': 'worstvideo+worstaudio/worst',
        '1080p': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
        '720p': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
        '480p': 'bestvideo[height<=480]+bestaudio/best[height<=480]',
        '360p': 'bestvideo[height<=360]+bestaudio/best[height<=360]'
    }

    format_spec = quality_settings.get(quality.lower(), 'best')

    ydl_opts = {
        'format': format_spec,
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'ignoreerrors': True,
        'merge_output_format': 'mp4',
        'progress_hooks': [lambda d: print(f"İndiriliyor: {d.get('filename', 'Bilinmeyen')}")],
    }

    with YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            ydl.download([url])