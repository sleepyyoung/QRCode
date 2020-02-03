from urllib import request
from urllib import parse
import json

def tran(data):
    Request_URL="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    form_data={}
    form_data['i']=data
    form_data['from'] = 'AUTO'
    form_data['to'] = 'AUTO'
    form_data['smartresult'] = 'dict'
    form_data['doctype']='json'
    form_data['version']='2.1'
    form_data['action']='FY_BY_CLICKBUTTION'
    form_data['typoResult']='false'

    data=parse.urlencode(form_data).encode('utf-8')
    response=request.urlopen(Request_URL,data)
    html=response.read().decode('utf-8')
    translate_results = json.loads(html)
    translate_result = translate_results["translateResult"][0][0]['tgt']
    # print(translate_result)
    return translate_result
