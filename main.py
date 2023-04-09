from flask import Flask, request, render_template
import wikipedia

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        language = request.form['language']
        print(query)
        wikipedia.set_lang(language)

        try:
            result = wikipedia.summary(query, sentences=5)
            related_pages = [[x, wikipedia.page(x).url] for x in wikipedia.search(query)]
        except wikipedia.exceptions.DisambiguationError as e:
            result ='DisambiguationError:'
            related_pages = e.options
        except Exception as e:
            result = "Error: "
            related_pages = None

        return render_template('index.html', result=result, related_pages=related_pages)

    return render_template('index.html')


if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
