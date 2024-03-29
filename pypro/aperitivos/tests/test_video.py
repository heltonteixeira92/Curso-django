from django.urls import reverse
from model_mommy import mommy
from pypro.aperitivos.models import Video
from pypro.django_assertions import assert_contains
import pytest as pytest


@pytest.fixture
def video(db):
    return mommy.make(Video)


@pytest.fixture
def resp(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug,)))


@pytest.fixture
def resp_video_nao_encontrado(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug + 'video_nao_existente',)))


def test_status_code_video_nao_encontrado(resp_video_nao_encontrado):
    assert resp_video_nao_encontrado.status_code == 404


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp, video):
    assert_contains(resp, video.titulo)


def test_conteudo_video(resp, video):
    assert_contains(resp, '<div style="padding:56.21% 0 0 0;position:relative;">'
                          f'<iframe src="https://player.vimeo.com/video/{video.vimeo_id}?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" '
                          'frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="aula-01-motivacao-curso-de-python-gratis.mp4"></iframe>'
                          '</div><script src="https://player.vimeo.com/api/player.js"></script>')
