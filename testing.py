requests = [
    {
        'deleteParagraphBullets': {
            'range': {
                'startIndex': 1,
                'endIndex': 50
            },
        }
    }
]

result = service.documents().batchUpdate(
    documentId=DOCUMENT_ID, body={'requests': requests}).execute()
