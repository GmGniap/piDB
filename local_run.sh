set -euf -o pipefail 

datasette ".\GEM\gem.db" ".\Ember-Climate\ember.db" -m metadata.json