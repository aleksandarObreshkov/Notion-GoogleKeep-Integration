import gkeepapi

keep = gkeepapi.Keep()

def login(email:str, password:str):
    keep.login(email.rstrip(), password.rstrip())
    keep.sync(True)
    

def get_quick_capture_content():    
    keep.sync(True)
    notes = keep.all()
    quick_add_id = 0

    for note in notes:
        if note.title == "Quick add":
            quick_add_id = note.id
            break

    quick_add_note = keep.get(quick_add_id)
    note_content = quick_add_note.text
    if note_content != "":
        print(f"Note content: {note_content}")
        keep.sync(True)
        return note_content
    print("Quick capture note is empty")
    return None

def clear_note_content():
    notes = keep.all()
    for note in notes:
        if note.title == "Quick add":
            note.text=''
            keep._sync_notes(True)