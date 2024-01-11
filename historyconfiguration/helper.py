from historyconfiguration.models import HistoryConfiguration


def history_enable(model_name):
    config = HistoryConfiguration.objects.filter(model_name=model_name).first()
    if config and config.enable:
        return True
    return False
