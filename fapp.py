from flask import Flask, render_template,request,jsonify
from flask_socketio import SocketIO
from bs4 import BeautifulSoup
from flask import url_for


app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/jupyter')
def jupyter():
    return render_template('RSA.html')

    # Add your code to communicate with the Jupyter Notebook here
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/display_graph', methods=['POST'])
def display_graph():
    selected_option1 = request.form.get('dropdown1')
    selected_option2 = request.form.get('dropdown2')
    selected_option3 = request.form.get('dropdown3')
    selected_option4 = request.form.get('dropdown4')
    
    
    if selected_option1 == 'option1':
        selected_option = '-'.join([selected_option1, selected_option2, selected_option3, selected_option4])
        parameter_to_image = {
            'option1-optionA-item1-choiceX': 'image-for-option1-optionA-item1-choiceX',
            # Add more mappings for other options
        }

        image_id = parameter_to_image.get(selected_option)
        if image_id:
            with open('C:/Users/HP/Desktop/FrontRSA/templates/RSA.html', 'r', encoding='utf-8') as file:
                html_content = file.read()
            soup = BeautifulSoup(html_content, 'html.parser')
            image = soup.find('img', {'id': image_id})
            return f"<img src='{url_for('static', filename='images/img1.png')}'>"
if __name__ == '__main__':
    app.run(debug=True)
