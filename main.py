from urllib import response
import notion
import keep
from flask import Flask, jsonify
import os


server = Flask(__name__)

@server.route("/sync")
def sync():

    email = os.getenv("PERSONAL_EMAIL")
    password = os.getenv("PERSONAL_PASSWORD")
    keep.login("aleks.yasuo@gmail.com", "Inolongerwishtoadult0092")

    print("Reading QuickNote content")
    quick_capture_note = keep.get_quick_capture_content()

    if quick_capture_note != []:
        print("Writing to Notion page")
        try:
            notion.write_array_to_quick_capture_page(quick_capture_note)
            print("Clearing QuickNote content")
            keep.clear_note_content()
            resp = jsonify(success=True)
            return resp
        except RuntimeError as re:
            print(f"Error in writing to Notion. Message: {re.args[0]}")
            resp = jsonify(success=True)
            return resp
     


if __name__ == "__main__":
    server.run()