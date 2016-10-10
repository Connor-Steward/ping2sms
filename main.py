import mail_pull2
import text

# Main program loop/logic intersection


# TODO: Create exchange email instead of using external Gmail account
# TODO:
try:
    # Get info/sanitize
    mail_pull2.get_mail()
    mail_pull2.clean_data()

    #Send text's
    text.send_txt_connor()
    # text.send_txt_yusuf()
    # text.send_txt_damian()
    # text.send_txt_richard()

    #Wipe mailbox
    mail_pull2.wipe_mailbox()

except:
    print("No new mail")