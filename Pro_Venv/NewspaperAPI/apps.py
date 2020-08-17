from django.apps import AppConfig


class NewspaperapiConfig(AppConfig):
    name = 'NewspaperAPI'

    def ready(self):
        from. import updater
        updater.start()
