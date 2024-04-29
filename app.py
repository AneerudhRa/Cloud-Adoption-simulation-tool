from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        company_size = request.form['company_size']
        industry_type = request.form['industry_type']
        budget = int(request.form['budget'])
        it_infrastructure = request.form['it_infrastructure']

        # Simple logic to determine cloud readiness and suggest a strategy
        if budget < 5000:
            recommendation = "Rehost: Low budget suggests minimal changes to cut costs."
        elif it_infrastructure == 'hybrid':
            recommendation = "Refactor: Optimize existing applications for the cloud."
        else:
            recommendation = "Rebuild: Invest in completely redesigning applications for cloud optimization."

        return render_template('result.html', recommendation=recommendation)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
