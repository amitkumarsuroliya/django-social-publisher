import json
import requests


def upload_file_to_vk_wall(vk, file_path):
    upload_server = vk.get('photos.getWallUploadServer')
    files = {'photo': open(file_path, 'rb')}
    result = requests.post(upload_server['upload_url'], files=files)
    json_result = json.loads(result.text, strict=False)
    return vk.get('photos.saveWallPhoto', photo=json_result['photo'], server=json_result['server'],
                  hash=json_result['hash'])