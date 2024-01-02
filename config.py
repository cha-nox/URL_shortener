from os import urandom, environ
from datetime import timedelta

class AppInfos:
    @staticmethod
    def link_lengths(key : str) -> int :
        if key == 'default' : return 6
        elif key == 'min' : return 5
        elif key == 'max' : return 10
        else : raise ValueError("Invalid key.")

    @staticmethod
    def web_app_name() -> str : return 'Easy Link'

    @staticmethod
    def domain_name() -> str : return 'http://localhost:8052/'

    @staticmethod
    def allowed_extensions() -> tuple :
        return (
            # Allowed document file formats
            'xml', 'json', 'csv', 'toml', 'yaml',
            'txt', 'md', 'pdf', 'rtf', 'epub',
            'odt', 'odp', 'ods', 'odg',
            'doc', 'ppt', 'xls',
            'docx', 'pptx', 'xlsx', 'pub',

            # Allowed image file formats
            'png', 'jpg', 'jpeg', 'webp', 'gif',

            # Allowed music file formats
            'mp3', 'ogg', 'wav',

            # Allowed video file formats
            'mp4', 'avi',

            # Allowed zipped file formats
            'zip', 'rar', 'tar', 'gz'
        )
    
    @staticmethod
    def upload_folder() -> str : return "app/static/uploads"

    @staticmethod
    def tmp_folder() -> str : return AppInfos.upload_folder() + '/tmp'

    @staticmethod
    def max_upload_size(requested_type : type = int) -> int|str :
        if requested_type == int : return 16 * 1024 * 1024
        elif requested_type == str : return '16 Mo'
        else : raise TypeError("Invalid requested type.")

    @staticmethod
    def password_limits() -> str : return '200/day;100/hour;20/minute'

class Config:
    SECRET_KEY = environ.get('SECRET_KEY')\
        or urandom(32).hex()
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=10)
    UPLOAD_FOLDER = AppInfos.upload_folder()
    # MAX_CONTENT_LENGTH = AppInfos.max_upload_size()