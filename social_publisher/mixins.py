import vkontakte


class SocialPublisher(object):
    vk_access_token = ''

    def publish(self):
        vk = vkontakte.API(token=self.vk_access_token)
        vk.get('wall.post', message='Test')

    def get_vkontakte_albums(self):
        vk = vkontakte.API(token=self.vk_access_token)
        return vk.get('photos.getAlbums')