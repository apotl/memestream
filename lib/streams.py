import secrets

class HlsStream:
    key = None
    def __init__(self):
        self.key = secrets.token_urlsafe(4)
        self._save()

    """
    Save model
    """
    def _save(self):
        pass

    """
    Launch container on AWS configured for stream
    """
    def initialize(self):
        pass

class RtmpStream:
    pass