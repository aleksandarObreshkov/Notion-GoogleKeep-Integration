from time import sleep
import notion
import keep

def main():

    email = input("Email: ")   
    password = input("Password: ")
    keep.login(email, password)

    while(True):
        print("Reading QuickNote content")
        quick_capture_note = keep.get_quick_capture_content()
        if quick_capture_note != None:
            print("Writing to Notion page")
            res = notion.write_content_to_quick_capture_page(quick_capture_note)
            if res.status_code==200:
                print("Clearing QuickNote content")
                keep.clear_note_content()
            else: 
                print(f"Unable to write to Notion page. Message: {res.reason}")
                print(res.json())
        sleep(10)

if __name__ == "__main__":
    main()