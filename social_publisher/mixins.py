from django.conf import settings
import vkontakte
from social_publisher.utils.facebook import publish_to_fb_wall
from social_publisher.utils.vkontakte import publish_to_vk_wall


class SocialPublisher(object):
    image_path = ''

    def publish(self):
        self.publish_to_vk()
        self.publish_to_facebook()

    def publish_to_vk(self):
        vk = vkontakte.API(token=settings.VK_ACCESS_TOKEN)
        url = 'http://google.com'
        text = 'Test message'
        publish_to_vk_wall(vk, self.image_path, url, text)

    def publish_to_facebook(self):
        publish_to_fb_wall(self.image_path)