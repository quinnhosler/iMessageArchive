#!/usr/bin/python

from shutil import copyfile
import sqlite3
import sys
import hashlib

backup = sys.argv[1]
basepath = "/Users/Quinn/Library/Application Support/MobileSync/Backup/%s/" % backup


conn = sqlite3.connect(basepath+"3d/3d0d7e5fb2ce288813306e4d4636395e047a3d28")
c = conn.cursor()
c.execute("SELECT filename, transfer_name FROM chat LEFT OUTER JOIN chat_message_join ON chat.ROWID = chat_id LEFT OUTER JOIN message ON message.ROWID = chat_message_join.message_id LEFT OUTER JOIN message_attachment_join ON message.ROWID = message_attachment_join.message_id LEFT OUTER JOIN attachment ON attachment_id = attachment.ROWID")

for row in c.fetchall():
	if not row[0]:
		continue
	filepath = row[0].replace('~/', 'MediaDomain-')
	sha = hashlib.sha1()
	sha.update(filepath)
	filename = sha.hexdigest()
	try:
		copyfile(basepath+filename[:2]+"/"+filename, "/Users/Quinn/Desktop/_export/"+row[1])
	except:
		pass
	