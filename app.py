import os

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    company_size = request.form['company_size']
    budget = request.form['budget']
    it_infrastructure = request.form['it_infrastructure']
    
    # Simple logic to determine cloud readiness and suggest a strategy
    if budget == 'Under $10,000':
        recommendation = "Rehost"
        explanation = "Given the limited budget, rehosting offers a cost-effective way to migrate with minimal changes."
    elif it_infrastructure == 'Hybrid':
        recommendation = "Refactor"
        explanation = "Since you have hybrid infrastructure, refactoring allows you to optimize existing applications for the cloud."
    else:
        recommendation = "Rebuild"
        explanation = "Invest in completely redesigning applications for cloud optimization to fully leverage cloud capabilities."
    
    return render_template('result.html', recommendation=recommendation, explanation=explanation)

if __name__ == '__main__':
    # Get port number from the environment variable or use 5000 as fallback
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
