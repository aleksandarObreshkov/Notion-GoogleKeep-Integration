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
        if quick_capture_note != []:
            print("Writing to Notion page")
            try:
                notion.write_array_to_quick_capture_page(quick_capture_note)
                print("Clearing QuickNote content")
                keep.clear_note_content()
            except RuntimeError as re:
                print(f"Error in writing to Notion. Message: {re.args[0]}")
        sleep(10)

if __name__ == "__main__":
    main()