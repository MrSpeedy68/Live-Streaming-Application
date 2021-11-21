from waitress import serve
from livevideo import app

serve(app, host='0.0.0.0', port=8080, url_scheme='RTMP', threads=6)

