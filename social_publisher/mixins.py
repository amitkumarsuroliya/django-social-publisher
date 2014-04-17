import vkontakte
from social_publisher.utils import upload_file_to_vk_wall


class SocialPublisher(object):
    vk_access_token = ''
    image_path = ''

    def publish(self):
        self.publish_to_vk_wall()

    def publish_to_vk_wall(self):
        vk = vkontakte.API(token=self.vk_access_token)
        photo = upload_file_to_vk_wall(vk, self.image_path)
        attachments = photo[0]['id']
        attachments += ',http://google.com'
        vk.get('wall.post', message='Test message', attachments=attachments)