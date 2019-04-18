import ujson as json
import spacy

nlp = spacy.load('en')

def model(message):
    message = json.loads(message)
    doc = nlp(message['text'])
    return json.dumps({
        'noun_chunks': [str(s) for s in set(doc.noun_chunks)],
        'entities': [str(s) for s in doc.ents]
    })
