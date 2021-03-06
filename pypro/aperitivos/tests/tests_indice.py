from django.urls import reverse
from pypro.django_assertions import assert_contains
import pytest as pytest


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'titulo',
    [
        'Video Aperitivo: Motivação',
        '',

    ]
)
def test_titulo_indice(resp, titulo):
    assert_contains(resp, titulo)
