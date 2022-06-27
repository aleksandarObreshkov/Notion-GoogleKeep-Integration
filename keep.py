import gkeepapi

keep = gkeepapi.Keep()

def login(email:str, password:str):
    keep.login(email.rstrip(), password.rstrip())
    keep.sync(True)
    

def get_quick_capture_content()-> list[str]:    
    keep.sync(True)
    notes = keep.all()
    quick_add_id = -1

    for note in notes:
        if note.title == "Quick add":
            quick_add_id = note.id
            break

    if quick_add_id==-1:
        raise RuntimeError('QuickAdd note does not exist')

    quick_add_note = keep.get(quick_add_id)
    note_content:str = quick_add_note.text
    if note_content != "":
        return note_content.splitlines()
    print("Quick capture note is empty")
    return []

def clear_note_content():
    notes = keep.all()
    for note in notes:
        if note.title == "Quick add":
            note.text=''
            keep._sync_notes(True)