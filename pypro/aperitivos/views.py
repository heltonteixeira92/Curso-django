from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao':{'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': 542810699},
        'instalacao-windows':{'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': 542810699},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
