from sqlite3 import Time
from time import sleep
import notion
import keep

def main():
    while(True):
        quick_capture_note = keep.get_quick_capture_content()
        notion.write_content_to_quick_capture_page(quick_capture_note)
        sleep(60)

if __name__ == "__main__":
    main()