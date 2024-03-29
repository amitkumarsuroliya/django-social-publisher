import json
import requests


def publish_to_vk_wall(vk, image_path, url, text):
    attachments = []
    if image_path:
        photo = upload_photo_to_vk_wall(vk, image_path)
        attachments.append(photo[0]['id'])
    attachments.append(url)
    message = '%(text)s %(url)s %(tags)s' % {'text': text, 'url': url, 'tags': []}
    vk.get('wall.post', message=message, attachments=','.join(attachments))


def upload_photo_to_vk_wall(vk, file_path):
    upload_server = vk.get('photos.getWallUploadServer')
    files = {'photo': open(file_path, 'rb')}
    result = requests.post(upload_server['upload_url'], files=files)
    json_result = json.loads(result.text, strict=False)
    return vk.get('photos.saveWallPhoto', photo=json_result['photo'], server=json_result['server'],
                  hash=json_result['hash'])


