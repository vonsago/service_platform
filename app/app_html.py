from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/index/',methods=['get','post'])
def index_page():
    image=request.form.get('image')
    port=request.form.get('port')
    volumes=request.form.get('volumes')
    if image and port and volumes:
        return 'succeed！'
    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', 8090, debug=True)