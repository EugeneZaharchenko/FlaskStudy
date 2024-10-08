# from flask import Flask, render_template
#
# from utils.view_modifiers import response
#
# app = Flask(__name__)
#
#
# def get_films():
#     return [
#         {
#             'id': 1,
#             'title': 'Harry Potter and the Philosopher\'s Stone',
#             'release_date': 'November 4, 2001',
#         },
#         {
#             'id': 2,
#             'title': 'Harry Potter and Chamber of Secrets',
#             'release_date': 'November 3, 2002',
#         }
#     ]
#
#
# @app.route('/')
# @app.route('/hello')
# @response(template_file='hello.html')
# def hello():
#     films = get_films()
#     return {'films': films}
#
#
# @app.route('/about')
# def about():
#     return render_template('about.html', title='About')
#
#
# @app.route('/<string:name>')
# def greeting(name: str):
#     return f'Hello, {name.capitalize()}'
#
#
# if __name__ == '__main__':
#     app.run()


from src import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
