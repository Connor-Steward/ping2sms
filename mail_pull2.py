import imaplib


def get_mail():
    # Create conn to G-Mail acc (spec. the PINGPLOTTER inbox)
    m = imaplib.IMAP4_SSL('imap.gmail.com')
    m.login('email@gmail.com', 'p4ssw0rd')
    m.select("PINGPLOTTER")

    # search through all mail in inbox
    typ, data = m.search(None, 'ALL')
    for num in data[0].split():
        data = m.fetch(num, '(BODY[HEADER.FIELDS (SUBJECT)])')
        return data

    # Close connection + logout
    m.close()
    m.logout()

def clean_data():
    # Sanitize data to send
    dirty_text = get_mail()
    subject = dirty_text[1][0][1]
    print(subject)
    return subject


def wipe_mailbox():
    m = imaplib.IMAP4_SSL('imap.gmail.com')
    m.login('email@gmail.com', 'p4ssw0rd')
    m.select("PINGPLOTTER")

    typ, data = m.search(None, 'ALL')
    for num in data[0].split():
        data = m.fetch(num, '(BODY[HEADER.FIELDS (SUBJECT)])')
        m.store(num, '+FLAGS', '\\Deleted')
        m.expunge()
    m.close()
    m.logout()



