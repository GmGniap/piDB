from datasette.app import Datasette
app = Datasette(files=["./Ember-Climate/ember.db"]).app()