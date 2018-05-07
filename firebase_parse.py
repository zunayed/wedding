import csv

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.Certificate('blog-741dd-firebase-adminsdk-07jqu-fbf8ff2dfc.json')

firebase_admin.initialize_app(cred, {
    'projectId': "blog-741dd",
})

db = firestore.client()

docs = db.collection(u'zu_rsvp').get()

with open('rsvp.csv' ,'w+') as csvfile:
    rsvp_writer = csv.writer(csvfile)

    fieldnames = ['name', 'holud', 'wedding', 'reception']
    rsvp_writer.writerow(fieldnames)

    for doc in docs:
        data = doc.to_dict()
        print(u'{} => {}'.format(doc.id, data))
        rsvp_writer.writerow([doc.id, data['holud'], data['wedding'], data['reception']])

