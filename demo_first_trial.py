import os
from evoman.environment import Environment
from first_trial_controller import player_controller

experiment_name = 'first_trial'

if not os.path.exists(experiment_name):
    os.makedirs(experiment_name)

# Update the number of neurons for this specific example
n_hidden_neurons = 0
# initializes environment for multi objetive mode (generalist)  with static enemy and ai player
env = Environment(experiment_name=experiment_name,
				  playermode="ai",
				  player_controller=player_controller(),
		  		  speed="normal",
				  enemymode="static",
                  fullscreen=False,
                  visuals=True,
				  level=2)

env.update_parameter('enemies', [1])
env.play()
