<<<<<<< HEAD
# Create  secrey key so we can use sessions
SECRET_KEY = 'c80820f2c78f60bc2dab263b1eeb6c7b'

# Create in-memory database
DATABASE_FILE = 'smart_farming'
SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/' + DATABASE_FILE

SECURITY_PASSWORD_SALT = "ATGUOHAELKiubahiughaerGOJAEGj"


# Flask-Security features
SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = True
SECURITY_RECOVERABLE =True
SECURITY_SEND_PASSWORD_RESET_EMAIL = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECURITY_TRACKABLE = True

=======
# Create  secrey key so we can use sessions
SECRET_KEY = 'c80820f2c78f60bc2dab263b1eeb6c7b'

# Create in-memory database
DATABASE_FILE = 'smart_farming'
SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/' + DATABASE_FILE

SECURITY_PASSWORD_SALT = "ATGUOHAELKiubahiughaerGOJAEGj"


# Flask-Security features
SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = True
SECURITY_RECOVERABLE =True
SECURITY_SEND_PASSWORD_RESET_EMAIL = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECURITY_TRACKABLE = True

>>>>>>> parent of 5a30ca7... commit message
UPLOAD_FOLDER ="./uploads"