import cottonmouth.html

def render(*body):
    html = ['html',
            ['head',
             ['title', 'Room monitor'],
             ['meta', {'charset' : 'utf-8'}]],
            ['body'] + list(body)
        ]
    
    return cottonmouth.html.render('<!doctype html>', html)
