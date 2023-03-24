from flask import Flask, render_template
import requests
app = Flask(__name__)

API_json_data = "https://api.npoint.io/e034c8f4ee84d63ac248"
# Getting the json data from the text
all_articles = requests.get(API_json_data).json()

@app.route("/")
def home_route():
    return render_template('index.html', articles=all_articles)

@app.route("/contact.html")
def contact_route():
    return render_template('contact.html')

@app.route("/about.html")
def about_route():
    return render_template('about.html')

@app.route("/index.html")
def return_home():
    return render_template('index.html', articles=all_articles)

@app.route("/post.html")
def post():
    return render_template('post.html')

@app.route("/post/<int:index>")
def show_article(index):
    requested_post = None
    requested_image_url = None
    for blog_post in all_articles:
        if blog_post['id'] == index:
            requested_post = blog_post
            requested_image_url = blog_post['image_url']
    return render_template("post.html", post=requested_post, image_id=index, image_url=requested_image_url)



if __name__ == "__main__":
    app.run(debug=True)
