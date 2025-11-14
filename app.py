from flask import Flask, render_template, request, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

# Configuration
PROJECTS_DIR = 'data/projects'
CERTIFICATES_DIR = 'data/certificates'
PROFILE_FILE = 'data/profile.json'

# Technology logo mapping (using CDN links)
TECH_LOGOS = {
    'Python': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg',
    'SQL': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg',
    'MySQL': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg',
    'PostgreSQL': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg',
    'Pandas': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg',
    'NumPy': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg',
    'Matplotlib': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/matplotlib/matplotlib-original.svg',
    'Seaborn': 'https://seaborn.pydata.org/_images/logo-mark-lightbg.svg',
    'Scikit-learn': 'https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg',
    'TensorFlow': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg',
    'Keras': 'https://upload.wikimedia.org/wikipedia/commons/a/ae/Keras_logo.svg',
    'Flask': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg',
    'Django': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg',
    'Tableau': 'https://cdn.worldvectorlogo.com/logos/tableau-software.svg',
    'PowerBI': 'https://upload.wikimedia.org/wikipedia/commons/c/cf/New_Power_BI_Logo.svg',
    'Power BI': 'https://upload.wikimedia.org/wikipedia/commons/c/cf/New_Power_BI_Logo.svg',
    'Excel': 'https://upload.wikimedia.org/wikipedia/commons/3/34/Microsoft_Office_Excel_%282019%E2%80%93present%29.svg',
    'Jupyter': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original.svg',
    'Git': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg',
    'GitHub': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg',
    'Docker': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg',
    'AWS': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original-wordmark.svg',
    'Azure': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/azure/azure-original.svg',
    'R': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/r/r-original.svg',
    'Java': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg',
    'JavaScript': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg',
    'HTML': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg',
    'CSS': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg',
    'React': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg',
    'MongoDB': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg',
    'Spark': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/apachespark/apachespark-original.svg',
    'Hadoop': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/hadoop/hadoop-original.svg',
    'Kaggle': 'https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/189_Kaggle_logo_logos-512.png',
}

def get_tech_logo(tech_name):
    """Get logo URL for a technology, with fallback"""
    # Try exact match first
    if tech_name in TECH_LOGOS:
        return TECH_LOGOS[tech_name]
    
    # Try case-insensitive match
    tech_lower = tech_name.lower()
    for key, value in TECH_LOGOS.items():
        if key.lower() == tech_lower:
            return value
    
    # Default fallback - generic code icon
    return 'https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/code.svg'

# Make the function available in templates
app.jinja_env.globals.update(get_tech_logo=get_tech_logo)

def load_json_files(directory):
    """Load all JSON files from a directory"""
    items = []
    if os.path.exists(directory):
        for filename in os.listdir(directory):
            if filename.endswith('.json'):
                with open(os.path.join(directory, filename), 'r') as f:
                    items.append(json.load(f))
    return sorted(items, key=lambda x: x.get('date', ''), reverse=True)

def load_profile():
    """Load profile data from JSON file"""
    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, 'r') as f:
            return json.load(f)
    return {
        "name": "Your Name",
        "title": "Data Analyst",
        "tagline": "Transforming Data into Actionable Insights",
        "bio": "Aspiring Data Analyst with strong analytical skills and a passion for extracting meaningful insights from complex datasets.",
        "email": "your.email@example.com",
        "phone": "+1 234 567 8900",
        "location": "City, Country",
        "linkedin": "https://linkedin.com/in/yourprofile",
        "github": "https://github.com/yourusername",
        "image": "profile.jpg"
    }

@app.route('/')
def index():
    """Main landing page with all sections"""
    profile = load_profile()
    projects = load_json_files(PROJECTS_DIR)
    certificates = load_json_files(CERTIFICATES_DIR)
    return render_template('index.html', profile=profile, projects=projects, certificates=certificates)

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

@app.route('/projects')
def projects():
    """Projects page"""
    projects = load_json_files(PROJECTS_DIR)
    return render_template('projects.html', projects=projects)

@app.route('/certificates')
def certificates():
    """Certificates page"""
    certificates = load_json_files(CERTIFICATES_DIR)
    return render_template('certificates.html', certificates=certificates)

@app.route('/contact')
def contact():
    """Contact page"""
    return render_template('contact.html')

@app.route('/send-message', methods=['POST'])
def send_message():
    """Handle contact form submission"""
    data = request.get_json()
    # Here you can add email functionality or save to database
    # For now, we'll just return success
    return jsonify({'success': True, 'message': 'Message received! I will get back to you soon.'})

if __name__ == '__main__':
    # Create necessary directories
    os.makedirs(PROJECTS_DIR, exist_ok=True)
    os.makedirs(CERTIFICATES_DIR, exist_ok=True)
    os.makedirs('static/css', exist_ok=True)
    os.makedirs('static/js', exist_ok=True)
    os.makedirs('static/images/projects', exist_ok=True)
    os.makedirs('static/images/certificates', exist_ok=True)
    
    app.run(debug=True)