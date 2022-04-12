from my_ap import app
from flask import Blueprint, jsonify, request
from my_ap.model.app_model import Articles,  db, article_schema,articles_schema
controll_app = Blueprint('api', __name__, url_prefix='/api')

@controll_app.route('/get', methods=['GET'])
def get_articles():
    all_articles = Articles.query.all()
    results = articles_schema.dump(all_articles)

    return jsonify(results)

@controll_app.route('/get/<id>/', methods=['GET'])
def get_details(id):
    article = Articles.query.get(id)
    print(f"article id {id} = ", article)
    if article is None:
        return jsonify({})
    return article_schema.jsonify(article)

@controll_app.route('/update/<id>/', methods=['PUT'])
def update_article(id):
    article = Articles.query.get(id)
    title = request.json['title']
    body = request.json['body']

    article.title = title
    article.body = body
    db.session.commit()

    return article_schema.jsonify(article)

@controll_app.route('/delete/<id>/', methods=['DELETE'])
def delete_article(id):
    article = Articles.query.get(id)
    db.session.delete(article)
    db.session.commit()
    return  article_schema.jsonify(article)

@controll_app.route("/add", methods=['POST'])
def add_article():
    title = request.json['title']
    body = request.json['body']
    articles = Articles(title, body)
    db.session.add(articles)
    db.session.commit()
    print(title, body)
    result = article_schema.jsonify(articles)
    print("aqui = ", result)
    return result
