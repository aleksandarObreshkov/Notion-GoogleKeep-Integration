import notion
import keep
from flask import Flask
import os

server = Flask(__name__)

@server.route("/sync")
def sync():

    email = os.getenv("PERSONAL_EMAIL")
    password = os.getenv("PERSONAL_PASSWORD")
    keep.login(email, password)

    print("Reading QuickNote content")
    quick_capture_note = keep.get_quick_capture_content()

    if quick_capture_note != []:
        print("Writing to Notion page")
        try:
            notion.write_array_to_quick_capture_page(quick_capture_note)
            print("Clearing QuickNote content")
            keep.clear_note_content()
        except RuntimeError as re:
            print(f"Error in writing to Notion. Message: {re.args[0]}")