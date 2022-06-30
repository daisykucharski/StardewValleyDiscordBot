from flask import Flask, request
import scrape

app = Flask(__name__)

@app.route('/birthday')
def get_birthday():
    name = request.args.get('name')
    return scrape.find_birthday(name)

@app.route('/bestgifts')
def get_best_gifts():
    name = request.args.get('name')
    return scrape.find_best_gifts(name)

@app.route('/universalloves')
def get_universal_loves():
    return scrape.find_universal_loves()

@app.route('/fishinfo')
def get_fish_info():
    fish = request.args.get('fish')
    return scrape.find_fish_info(fish)

@app.route('/cropinfo')
def get_crop_info():
    crop = request.args.get('crop')
    return scrape.find_crop_info(crop)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)