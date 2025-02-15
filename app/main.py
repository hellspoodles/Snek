import bottle
import os
import random

class snekspin(object):
	def __init__(self):
		self.turn = 0
		
	def spinny(self):
		return self.turn % 4
	
	def turninc(self):
		self.turn += 1

@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():
    data = bottle.request.json
	S = snekspin()
    game_id = data['game_id']
    board_width = data['width']
    board_height = data['height']
    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )
	
    # TODO: Do things with data
    #comment

    return {
        'color': '#00FF00',
        'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_url': head_url,
        'name': 'pure-aggression-snake'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json
	
    # TODO: Do things with data
    directions = ['up', 'left', 'down', 'right']
	
	S.turninc()
	
    return {
        'move': directions[S.spinny()],
        'taunt': 'SSSSsSssssss!'
    }


	



# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
	