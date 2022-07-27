from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get('/question')
def render_question():
    """ creates the form on question page from the
    Story instance prompts list"""

    # get a list of prompts from from Story instance
    prompts = silly_story.prompts if silly_story.prompts else []

    # pass that list into questions temp to paint the dom
    return render_template('questions.html', prompts=prompts)


@app.get('/story')
def render_story_page():
    """ renders the story page with the story,
    from the Story instance template text"""
    # make a dict form the form inputs
    return render_template('results.html')
