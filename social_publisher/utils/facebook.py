from django.conf import settings
from facepy import GraphAPI


def publish_to_fb_wall(image_path):
    token = '%s|%s' % (settings.FB_APP_KEY, settings.FB_APP_SECRET)
    graph = GraphAPI(token)

    result = graph.post(
        path='me/photos',
        source=open(image_path, 'rb')
    )