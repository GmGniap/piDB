set -euf -o pipefail 

datasette ".\GEM\gem.db" ".\Ember-Climate\ember.db" ".\Sport\sport.db" ".\BP\bp_energy.db" -m metadata.json