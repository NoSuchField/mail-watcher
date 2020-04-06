#!/usr/bin/python
import imaplib
import email
import os
import email.header
import time
import json
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

def decode_mime_words(s):
    return u''.join(
        word.decode(encoding or 'utf8') if isinstance(word, bytes) else word
        for word, encoding in email.header.decode_header(s))

with open("/opt/matcher/config.json", 'r') as f:
    config = json.loads(f.read())
    for c in config:
        IMAP4_HOST      = c['host']
        IMAP4_PORT      = c['port']
        IMAP4_USER      = c['user']
        IMAP4_PASS      = c['pass']
        IMAP4_MAILBOX   = c['mailbox']

        imap = imaplib.IMAP4_SSL(IMAP4_HOST)
        (retcode, capabilities) = imap.login(IMAP4_USER, IMAP4_PASS)
        imap.list()
        imap.select('inbox')

        (retcode, messages) = imap.search(None, '(UNSEEN)')
        if retcode == 'OK':
            for num in messages[0].split():
                typ, data = imap.fetch(num, '(RFC822)')
                for response_part in data:
                    if isinstance(response_part, tuple):
                        original = email.message_from_bytes(response_part[1])
                        title = decode_mime_words(original['From'])
                        brief = decode_mime_words(original['Subject'])
                        Notify.init(title)
                        Hello = Notify.Notification.new(title, brief, "evolution-mail")
                        Hello.show()
        imap.close()
        imap.logout()
    exit()    
