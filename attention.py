from sys import argv, stderr
from flask import Flask, make_response, url_for, request
from flask import render_template
import random

app = Flask(__name__, template_folder='.')
info = \
  {'EburnatedKnee': {'caption': 'Skeletons excavated from the monastic site of St. Stephen’s, dating back to Byzantine Jerusalem, often exhibit eburnation of the knee, a skeletal-degenerative disorder whereby the cartilage around the knee wears away, revealing subchondral bone. Historians speculate that these malformations were caused by constant and repetitive genuflection on the hard stone floors of the monastery during prayer and other religious rites. Prayer is the consummate attentional act; the will is focused so completely that the devotional act can supersede all other corporeal desires and instincts of self-preservation.',
  'question': 'nan',
  'source': 'Source: Excavation of a Byzantine Jerusalem Monastery'},
 'FrenchAdvertisementPrint': {'caption': 'In the late 1860’s, the streets and edifices of Paris bore witness to a new kind of advertisement: artistic advertisement posters - larger and more vibrant than ever before - that seemed to pull in any who passed by. Yet, it was only a matter of time before the posters became clutter, covering nearly every available surface in the city and obfuscating the beauty that they were originally conceptualized to productively enhance. An advertising tool whose aesthetic distinctiveness was key to its attention-catching capabilities expanded to fill the space provided until its powers asymptotically reduced to null, and not for the last time.',
  'question': 'nan',
  'source': 'Source: nan'},
 'SignOfTheTimes': {'caption': 'Signs of the Times (2017) was an art installation project by Scott Kelly and Ben Polkinghorne, placing “recommendations” at the sites of numerous travel destinations and significant locales. The signs were intended to become intrusion made manifest, drawing attention to the growing infringement of digital algorithms upon physical reality. As the world has come to internalize the relational computational logic of machines, the things we attend to are increasingly mediated by a layer of recommendations.',
  'question': 'nan',
  'source': 'Source: Art project by Scott Kelly and Ben Polkinghorne(2017)'},
 'TheSunNewspaper': {'caption': 'nan',
  'question': 'nan',
  'source': 'Source: National Museum of American History, Behring Center, January 4, 2013, https://americanhistory.si.edu/blog/2013/01/the-pony-press-and-the-patent-model-collection.html '},
 'ayn_rand': {'caption': 'I, Ayn Rand, "will never live for the sake of another man". Individual rights are right. Laissez faire capitalism is the most fair through its objective rationality. She had an inner circle of close friends including Alan Greenspan. ',
  'question': 'Is she alone?',
  'source': 'Source: Ayn Rand in front of Grand Central in midtown Manhattan in 1957. New York Times Co.—Getty Images'},
 'behaviorism': {'caption': 'It lives in the deepest recesses of the uncanny valley. Lifeless yet warm, friendly yet neglectful. Behavioral inheritance between inanimate and living creatures shows the complexity and indirection of the parent-child relationship. ',
  'question': 'What role does attention play in effective parenting?',
  'source': 'Source: Harlow, Harry F. “The Nature of Love.” The Macaque Connection, 2012, pp. 19–31., doi:10.1007/978-1-4614-3967-7_2. '},
 'boston_massacre': {'caption': 'Sensationalized media have long history in the United States. Paul Revere himself played an important role in the inception of revolutionary messaging. It can sometimes be justified to capture attention for the wrong reasons but towards a righteous goal. ',
  'question': 'Who will sound the alarm today?',
  'source': 'Source: Engraving by Paul Revere on March 5, 1770'},
 'camera_obscura': {'caption': 'The classical model of the human subject has as its core metaphor, the camera obscura. Some time between 1790 and 1860, the classical model came apart as science uncovered the complexity of perception. The repositioning of the subject towards “attention” restabilized the "self".',
  'question': 'What is the new model? Where is the self now?',
  'source': 'Source: Illustration of a "portable" camera obscura in Kircher\'s Ars Magna Lucis Et Umbra 1646'},
 'duhamel': {'caption': 'nan',
  'question': 'nan',
  'source': 'Source: Duhamel, Georges, and Charles Miner Thompson. America: the Menace: Scenes From the Life of the Future. Boston: Houghton Mifflin Company, 1931. (p.28)'},
 'escher': {'caption': 'Behold the imperfect reflection. The lens and artist condition the image even when attending to ourselves. To change the image, you can manipulate the object or you can manipulate yourself. ',
  'question': 'Which reflections are most true? How can one see the (best) self best?',
  'source': 'Source: A lithograph by Dutch artist M. C. Escher, first printed in January 1935'},
 'mass_distraction': {'caption': 'Jeff, Mark, Sundar, and Jack. How much of your day do they control? At least you can see nuclear warheads coming. These platforms suffuse themselves in our lives without us noticing their spread while allowing us to hardly notice anything else. Meaningless lives are medicated and bad ideas are legitimized. ',
  'question': 'How do we defuse the potential violence fostered by these systems?',
  'source': 'Source: Gasaway, Rich. “Weapons of Mass Distraction.” Situational Awareness Matters!™, 15 Nov. 2019, www.samatters.com/weapons-of-mass-distraction/. '},
 'paganini': {'caption': 'Audiences were so enthralled by his performances that they claimed he sold his soul to the devil. His eyes seem disembodied as he unfocuses through music. The art seems to flow and not emerge from him. ',
  'question': 'How does deeply attentive performance depersonalize the artist and the observers?',
  'source': 'Source: 1831 bulletin advertising a performance of Paganini'},
 'panopticon': {'caption': 'Totalizing surveillance characterizes the payment of the modern attentional transaction. Technologies capture our attention as well as our behavioral patterns in its expenditure. We are the prisoners and algorithms are in the watchtower. ',
  'question': 'How can we recenter ourselves and liberate others from hypervisibility?',
  'source': "Source: Plan of Jeremy Bentham's panopticon prison, drawn by Willey Reveley in 1791"},
 'tank_man': {'caption': 'He stands alone. Powerless to stop "progress". Attending to power thus less alone. Amid massive protests demanding justice he merely waits on the powerful. ',
  'question': 'Is he foolish or brave? How does visibility of resistance change its efficacy?',
  'source': 'Source: June 5, 1989. Credit: Jeff Widener/Associated Press'}}
@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
@app.route('/index', methods=['GET'])
def home():
    image = request.args.get('image')
    if (image == None):
        image = random.choice(list(info.keys()))
    html = render_template('home.html',
            image=image+'.jpeg',
            info=info[image])
    response = make_response(html)
    return response
@app.route('/test', methods=['GET'])
def test():
    image = request.args.get('image')
    if (image == None):
        image = random.choice(list(info.keys()))
    html = render_template('home_test.html',
            image=image+'.jpeg',
            info=info[image])
    response = make_response(html)
    return response