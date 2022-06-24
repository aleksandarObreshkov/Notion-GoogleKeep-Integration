import gkeepapi

def get_quick_capture_content():
    print('Signing into Google...')
    email = input("Email: ")   
    password = input("Password: ")
    keep = gkeepapi.Keep()
    keep.login(email.rstrip(), password.rstrip())
    keep.sync(True)

    notes = keep.all()
    quick_add_id = 0

    for note in notes:
        if note.title == "Quick add":
            quick_add_id = note.id
            break

    quick_add_note = keep.get(quick_add_id)
    note_content = quick_add_note.text
    keep.sync(True)

    return note_content