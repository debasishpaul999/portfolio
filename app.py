from flask import Flask, render_template, request, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

# Configuration
PROJECTS_DIR = 'data/projects'
CERTIFICATES_DIR = 'data/certificates'
PROFILE_FILE = 'data/profile.json'

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