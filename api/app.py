from flask import Flask, request
from flask_caching import Cache

import scrape

app = Flask(__name__)
app.config.from_object('config.BaseConfig')
cache = Cache(app)

@app.route('/birthday')
@cache.cached(timeout=500, query_string=True)
def get_birthday():
    name = request.args.get('name')
    return scrape.find_birthday(name)

@app.route('/bestgifts')
@cache.cached(timeout=500, query_string=True)
def get_best_gifts():
    name = request.args.get('name')
    return scrape.find_best_gifts(name)

@app.route('/universalloves')
@cache.cached(timeout=500, query_string=True)
def get_universal_loves():
    return scrape.find_universal_loves()

@app.route('/fishinfo')
@cache.cached(timeout=500, query_string=True)
def get_fish_info():
    fish = request.args.get('fish')
    return scrape.find_fish_info(fish)

@app.route('/cropinfo')
@cache.cached(timeout=500, query_string=True)
def get_crop_info():
    crop = request.args.get('crop')
    return scrape.find_crop_info(crop)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)