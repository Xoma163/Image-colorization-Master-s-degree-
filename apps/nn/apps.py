from django.apps import AppConfig

from apps.nn.NeuralNetwork import NeuralNetwork


class NnConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.nn'

    def ready(self):
        nn = NeuralNetwork()
        nn.load_model()
