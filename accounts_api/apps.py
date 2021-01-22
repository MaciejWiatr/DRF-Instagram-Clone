from django.apps import AppConfig


class AccountsApiConfig(AppConfig):
    name = 'accounts_api'

    def ready(self):
        import accounts_api.signals  # pylint: disable=unused-import,import-outside-toplevel
