# SQLAlchemy for database
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Bcrypt for passwords hashing
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

# Limiter for bruteforce attacks preventing
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
limiter = Limiter(get_remote_address)

# Flask-WTF for CSRF tokens
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()