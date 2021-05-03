from django.urls import reverse
from pypro.django_assertions import assert_contains
import pytest as pytest


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:video', args=('motivacao',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp):
    assert_contains(resp, 'Video Aperitivo: Motivação')


def test_conteudo_video(resp):
    assert_contains(resp, '<div style="padding:56.21% 0 0 0;position:relative;">'
                          '<iframe src="https://player.vimeo.com/video/542810699?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" '
                          'frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="aula-01-motivacao-curso-de-python-gratis.mp4"></iframe>'
                          '</div><script src="https://player.vimeo.com/api/player.js"></script>')
