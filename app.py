from flask import Flask,  render_template
from flask_pymongo import PyMongo
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config["MONGO_URI"] = "mongodb+srv://dubliner73:test123@cluster0.klq8d.mongodb.net/Idealista?retryWrites=true&w=majority"
mongo = PyMongo(app)
playlists = list(mongo.db.scrapy_items.find({}).sort("rent_range"))



#@app.route('/')
#def index():
#    """Return homepage."""
#    return render_template('home.html', msg='Flask is Cool!!')

# OUR MOCK ARRAY OF PROJECTS
#playlists = [
#    { 'title': 'Cat Videos', 'description': 'Cats acting weird' },
#    { 'title': '80\'s Music', 'description': 'Don\'t stop believing!' }
#]

@app.route('/')
def playlists_index():
    """Show all playlists."""
    return render_template('playlists_index.html', playlists=playlists)    

if __name__ == '__main__':
    app.run(debug=True)