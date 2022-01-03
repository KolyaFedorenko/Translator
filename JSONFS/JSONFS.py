import requests
import json

def translate(user_text):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = "q=" + user_text + "&target=ru&source=en"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'accept-encoding': "application/gzip",
        'x-rapidapi-host': "google-translate1.p.rapidapi.com",
        'x-rapidapi-key': "ef714bf923msh1ba1a55dac12f62p1941aajsn8af1c5703574"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    response=response.text

    def find_values(id, json_repr):
        results = []

        def _decode_dict(a_dict):
            try:
                results.append(a_dict[id])
            except KeyError:
                pass
            return a_dict

        json.loads(json_repr, object_hook=_decode_dict) # Return value ignored.
        return results

    a=find_values("translatedText",response)
    a=str(a).replace("[","").replace("]","").replace("'","")
    print(a)
    return

inp_text='none'
while inp_text!='stop':
    inp_text=input()
    translate(inp_text)