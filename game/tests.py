from django.test import TestCase
from django.urls import reverse
import random
# Create your tests here.


class GameTests(TestCase):
    def test_play_game_view(self):
        choices = ['rock', 'paper', 'scissors']
        player_choice = random.choice(choices)

        response = self.client.get(reverse('play_game', args=[player_choice]))
        self.assertEqual(response.status_code, 200)