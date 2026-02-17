from flask import Flask, render_template, request, send_from_directory, jsonify
from werkzeug.utils import secure_filename
import json
import os
from pathlib import Path
from datetime import datetime
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def load_projects():
    """Load projects from JSON file"""
    try:
        with open('projects.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


@app.route('/')
def index():
    """Home page"""
    projects = load_projects()
    featured_projects = projects[:3] if projects else []
    return render_template('index.html', featured_projects=featured_projects)


@app.route('/projects')
def projects():
    """Projects page"""
    projects = load_projects()
    return render_template('projects.html', projects=projects)


@app.route('/projects/<int:project_id>')
def project_detail(project_id):
    """Project detail page"""
    projects = load_projects()
    project = next((p for p in projects if p['id'] == project_id), None)

    if project is None:
        return render_template('404.html'), 404

    return render_template('project_detail.html', project=project)


@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')


@app.route('/api/projects')
def api_projects():
    """API endpoint for projects"""
    projects = load_projects()
    return jsonify(projects)


@app.route('/download/<filename>')
def download_file(filename):
    """Download file from uploads folder"""
    try:
        return send_from_directory(
            app.config['UPLOAD_FOLDER'],
            filename,
            as_attachment=True
        )
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404


@app.route('/upload', methods=['POST'])
def upload_file():
    """Upload file (admin use)"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_')
        filename = timestamp + filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'success': True, 'filename': filename}), 200

    return jsonify({'error': 'File type not allowed'}), 400


def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
