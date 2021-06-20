import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains
from model_mommy import mommy

from pypro.modulos.models import Aula, Modulo


@pytest.fixture
def modulo(db):
    return mommy.make(Modulo)


@pytest.fixture
def aula(modulo):
    return mommy.make(Aula, modulo=modulo)


@pytest.fixture
def resp(client, aula):
    resp = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp


def test_titulo(resp, aula: Aula):
    assert_contains(resp, aula.titulo)


def test_vimeo(resp, aula: Aula):
    assert_contains(resp, '<div style="padding:56.21% 0 0 0;position:relative;">'
                          f'<iframe src="https://player.vimeo.com/video/{aula.vimeo_id}?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" '
                          'frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="aula-01-motivacao-curso-de-python-gratis.mp4"></iframe>'
                          '</div><script src="https://player.vimeo.com/api/player.js"></script>')