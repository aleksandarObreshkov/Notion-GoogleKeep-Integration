import requests
from string import Template
import os

INTEGRATION_KEY = os.environ["NOTION_SECRET"]
NOTION_API_ENDPOINT = "https://api.notion.com/v1"
QUICK_CAPTURE_PAGE = "19335353b2dc4282bfed975e93df02d3"

BLOCK_ADDING_URL = f'{NOTION_API_ENDPOINT}/blocks/{QUICK_CAPTURE_PAGE}/children'
AUTHORIZATION_HEADER = f'Bearer {INTEGRATION_KEY}'


headers = {
    "Authorization" : AUTHORIZATION_HEADER,
    "Notion-Version" : "2022-02-22",
    "Accept" : "application/json",
    "Content-Type" : "application/json"
}

content = Template('''{
    "children": [
    {
      "object": "block",
      "type": "bulleted_list_item",
      "bulleted_list_item": {
        "rich_text": [{ "type": "text", "text": { "content": "${note}"} }]
      }
    }
  ]
}''')

def write_content_to_quick_capture_page(text_from_note):
    data = content.substitute(note = text_from_note)
    print("Writing to Notion page")
    res = requests.patch(BLOCK_ADDING_URL, data=data, headers=headers)
    #Add exception messages