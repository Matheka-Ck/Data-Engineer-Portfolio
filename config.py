import os


class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or 'dev-secret-key-change-in-production'
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static/uploads')
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100MB max file size
    ALLOWED_EXTENSIONS = {'pdf', 'docx', 'xlsx',
                          'csv', 'txt', 'zip', 'pptx', 'json'}


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    UPLOAD_FOLDER = '/tmp/test_uploads'
