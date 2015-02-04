from server.utils.wstypes import HTMLVer
import os


__WWW_DIR__ = os.path.abspath('../elab/www/')
__SESSIONS_DIR__ = os.path.abspath('sessions/')
__INTERNAL_PORT__ = 8013
__LISTEN_ADDRESS__ = ''
__SESSION_COOKIE_NAME__ = 'sessionId'
__ALLOWED_DIRS__ = []
__ALLOWED_DIRS_AND_SUB__ = \
    [
        os.path.abspath('../elab/www/')
    ]
__ALLOWED_EXTENSIONS__ = []
__DENIED_EXTENSIONS__ = ['*.exe']
__MAX_POST_LENGTH__ = 2097152
__INDEX_PAGE__ = 'index.py'
__ENABLE_MULTITHREADING__ = True
__HTML_VER__ = HTMLVer.HTML5
