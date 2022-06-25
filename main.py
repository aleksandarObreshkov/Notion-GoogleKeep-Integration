from time import sleep
import notion
import keep
 

def main():
    email = input("Email: ")   
    password = input("Password: ")
    keep.login(email, password)

    while(True):
        quick_capture_note = keep.get_quick_capture_content()
        if quick_capture_note != None:
            notion.write_content_to_quick_capture_page(quick_capture_note)
        sleep(10)

if __name__ == "__main__":
    main()