# -*- coding: UTF-8 -*-

import requests
import json

BASE_URL = 'https://bortnik.hipchat.com'
# in future we can use context.base_url instead of BASE_URL and token from env.secret


class ApiRequest(object):

    def _get(self, url, payload, token):
        r = requests.get(BASE_URL + url, payload, headers={'Authorization': 'Bearer ' + token})
        return json.loads(r.text)

    def _post(self, url, payload, token):
        r = requests.post(BASE_URL + url, json.dumps(payload), headers={'Authorization': 'Bearer ' + token})
        return json.loads(r.text)

    def _delete(self, url, token):
        r = requests.delete(BASE_URL + url,  headers={'Authorization': 'Bearer ' + token})
        return json.loads(r.text)

    def _put(self, url, payload, token):
        r = requests.put(BASE_URL + url, json.dumps(payload), headers={'Authorization': 'Bearer ' + token})
        return json.loads(r.text)

    def create_token_with_api(self, payload):
        r = requests.post(BASE_URL + "/v2/oauth/token", json.dumps(payload))
        return json.loads(r.text)

    def delete_room(self, room):
        self._delete(BASE_URL + "/chat/room/" + room, token=token)
        return json.loads(r.text)

    def get_user(self, startindex=None, maxresults=None, includeguests=None, includedeleted=None, token=None):
        return self._get('/v2/user', {'start-index': startindex,
                                      'max-results': maxresults,
                                      'include-guests': includeguests,
                                      'include-deleted': includedeleted},
                         token=token)

    def create_user(self, name=None, roles=[], title='', mention_name=None, is_group_admin=False,
                    timezone='UTC', password='', email=None, token=None):
        return self._post('/v2/user', {'name': name, 'roles': roles, 'title': title, 'mention': mention_name,
                                       'is_group_admin': is_group_admin, 'timezoze': timezone, 'password': password,
                                       'email': email}, token=token)

    def view_user(self, id_or_email=None, token=None):
        return self._get('/v2/user/'+id_or_email, None, token=token)

