from sys import argv, stderr
from flask import Flask, make_response, url_for
from flask import render_template
import random

app = Flask(__name__, template_folder='.')
captions = {'ayn_rand': 'I, Ayn Rand, "will never live for the sake of another man". Individual rights are right. Laissez faire capitalism is the most fair through its objective rationality. She had an inner circle of close friends including Alan Greenspan. Is she alone? (Source: Ayn Rand in front of Grand Central in midtown Manhattan in 1957. New York Times Co.—Getty Images)',
 'behaviorism': 'It lives in the deepest recesses of the uncanny valley. Lifeless yet warm, friendly yet neglectful. Behavioral inheritance between inanimate and living creatures shows the complexity and indirection of the parent-child relationship. What role does attention play in effective parenting? (Source: Harlow, Harry F. “The Nature of Love.” The Macaque Connection, 2012, pp. 19–31., doi:10.1007/978-1-4614-3967-7_2. )',
 'boston_massacre': 'Sensationalized media have long history in the United States. Paul Revere himself played an important role in the inception of revolutionary messaging. It can sometimes be justified to capture attention for the wrong reasons but towards a righteous goal. Who will sound the alarm today? (Source: Engraving by Paul Revere on March 5, 1770)',
 'camera_obscura': 'The classical model of the human subject has as its core metaphor, the camera obscura. Some time between 1790 and 1860, the classical model came apart as science uncovered the complexity of perception. The repositioning of the subject towards “attention” restabilized the "self". What is the new model? Where is the self now? (Source: Illustration of a "portable" camera obscura in Kircher\'s Ars Magna Lucis Et Umbra 1646)',
 'escher': 'Behold the imperfect reflection. The lens and artist condition the image even when attending to ourselves. To change the image, you can manipulate the object or you can manipulate yourself. Which reflections are most true? How can one see the (best) self best? (Source: A lithograph by Dutch artist M. C. Escher, first printed in January 1935)',
 'guydebord_1': 'nan (Source: nan)',
 'mass_distraction': 'Jeff, Mark, Sundar, and Jack. How much of your day do they control? At least you can see nuclear warheads coming. These platforms suffuse themselves in our lives without us noticing their spread while allowing us to hardly notice anything else. Meaningless lives are medicated and bad ideas are legitimized. How do we defuse the potential violence fostered by these systems? (Source: Gasaway, Rich. “Weapons of Mass Distraction.” Situational Awareness Matters!™, 15 Nov. 2019, www.samatters.com/weapons-of-mass-distraction/. )',
 'paganini': 'Audiences were so enthralled by his performances that they claimed he sold his soul to the devil. His eyes seem disembodied as he unfocuses through music. The art seems to flow and not emerge from him. How does deeply attentive performance depersonalize the artist and the observers? (Source: 1831 bulletin advertising a performance of Paganini)',
 'panopticon': "Totalizing surveillance characterizes the payment of the modern attentional transaction. Technologies capture our attention as well as our behavioral patterns in its expenditure. We are the prisoners and algorithms are in the watchtower. How can we recenter ourselves and liberate others from their hypervisibility? (Source: Plan of Jeremy Bentham's panopticon prison, drawn by Willey Reveley in 1791)",
 'tank_man': 'He stands alone. Powerless to stop "progress". Attending to power thus less alone. Amid massive protests demanding justice he merely waits on the powerful. Is he foolish or brave? How does visibility of resistance change its efficacy? (Source: A man stands alone to block a line of tanks heading east on Beijing’s Changan Boulevard in Tiananmen Square on June 5, 1989. Credit: Jeff Widener/Associated Press)'}
@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
@app.route('/index', methods=['GET'])
def home():
    image = random.choice(list(captions.keys()))
    html = render_template('home.html',
            image=url_for('images', filename=image+'.jpeg'),
            caption=captions[image])
    response = make_response(html)
    return response