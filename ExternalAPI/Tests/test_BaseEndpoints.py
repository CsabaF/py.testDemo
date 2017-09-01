import requests
import importlib
importlib.import_module('os.path')

class BaseEndpointsSmokeTestSuite(object):

    def test_getInfo(method, getBasicAuthKey, featureInstance):
        r = requests.get(url=featureInstance + '/api/',
                         headers={'Accept': 'application/json',
                                  'Authorization': 'Basic ' + getBasicAuthKey})
        response = r.json()
        assert(response[u'url'] != "" and response[u'url'] != None)
        assert(response[u'version'] != "" and response[u'version'] != None)
        assert(r.status_code == 200)

    def test_getVersion(method, getBasicAuthKey, featureInstance):
        r = requests.get(url=featureInstance + '/api/version',
                         headers={'Accept': 'application/json',
                                  'Authorization': 'Basic ' + getBasicAuthKey})
        response = r.json()
        assert(response[u'default'] != "" and response[u'default'] != None)
        assert(response[u'versions'] != None)
        assert(r.status_code == 200)

    def test_getDefaultVersion(method, getBasicAuthKey, featureInstance):
        r = requests.get(url=featureInstance + '/api/version/default',
                         headers={'Accept': 'application/json',
                                  'Authorization': 'Basic ' + getBasicAuthKey})
        assert(r.status_code == 200)

    def test_getUserInfo(method, getBasicAuthKey, featureInstance):
        r = requests.get(url=featureInstance + '/api/info/me',
                         headers={'Accept': 'application/json',
                                  'Authorization': 'Basic ' + getBasicAuthKey})
        assert(r.status_code == 200)

    def test_getUserRoles(method, getBasicAuthKey, featureInstance):
        r = requests.get(url=featureInstance + '/api/info/me/roles',
                         headers={'Accept': 'application/json',
                                  'Authorization': 'Basic ' + getBasicAuthKey})
        assert(r.status_code == 200)

    def test_getCurrentOrganization(method, getBasicAuthKey, featureInstance):
        r = requests.get(url=featureInstance + '/api/info/organization',
                         headers={'Accept': 'application/json',
                                  'Authorization': 'Basic ' + getBasicAuthKey})
        assert(r.status_code == 200)

    def test_getOrganizationProperties(method, getBasicAuthKey, featureInstance):
        r = requests.get(url=featureInstance + '/api/info/organization/properties',
                         headers={'Accept': 'application/json',
                                  'Authorization': 'Basic ' + getBasicAuthKey})
        assert(r.status_code == 200)

    def test_postRecreateIndex(method, getBasicAuthKey, featureInstance):
        r = requests.post(url=featureInstance + '/api/index/recreateIndex',
                         headers={'Accept': 'application/json',
                                  'Authorization': 'Basic ' + getBasicAuthKey})
        assert(r.status_code == 200)