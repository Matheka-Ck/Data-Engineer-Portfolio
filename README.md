# Data Engineer Portfolio Website

A professional Flask-based portfolio website to showcase data engineering projects and skills. Features project listings, detailed project pages, file downloads, and a responsive design.

## Features

- ✨ **Responsive Design** - Mobile-friendly layout that works on all devices
- 📁 **Project Showcase** - Display your data engineering projects with details
- 📥 **File Downloads** - Share project documents, reports, and resources
- 🏷️ **Project Filtering** - Filter projects by category
- 📱 **Mobile Navigation** - Hamburger menu for mobile devices
- ⚡ **Performance** - Lightweight, fast-loading website
- 🎨 **Modern UI** - Clean, professional design with smooth animations
- 📊 **Skills Section** - Highlight your technical skills

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Modern CSS with Flexbox and Grid
- **Icons**: Font Awesome

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/flask-portfolio.git
   cd flask-portfolio
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create necessary directories**

   ```bash
   mkdir -p static/uploads
   ```

5. **Run the application**

   ```bash
   python app.py
   ```

6. **Visit the website**
   Open your browser and go to `http://localhost:5000`

## Configuration

Update `config.py` to customize settings:

```python
SECRET_KEY = 'your-secret-key'  # Change in production
MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # Max file upload size
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'xlsx', 'csv', 'txt'}  # Allowed file types
```

## Project Structure

```
flask-portfolio/
├── app.py                      # Main Flask application
├── config.py                   # Configuration settings
├── requirements.txt            # Python dependencies
├── projects.json              # Project data
├── templates/
│   ├── base.html              # Base template with navigation
│   ├── index.html             # Home page
│   ├── projects.html          # Projects listing page
│   ├── project_detail.html    # Individual project page
│   ├── about.html             # About page
│   ├── 404.html               # Not found page
│   └── 500.html               # Server error page
├── static/
│   ├── css/
│   │   └── style.css          # Main stylesheet
│   ├── js/
│   │   └── script.js          # JavaScript functionality
│   └── uploads/               # File upload directory
└── README.md                  # This file
```

## Customization

### Edit Your Profile

1. Update `templates/about.html` with your information
2. Add social media links in `templates/base.html` footer
3. Update email in `templates/about.html` contact section

### Add Projects

Edit `projects.json` to add your projects:

```json
{
  "projects": [
    {
      "id": 1,
      "title": "Your Project Title",
      "category": "ETL",
      "description": "Short description",
      "long_description": "Detailed description",
      "technologies": ["Python", "Spark"],
      "date": "2024-01-15",
      "links": [{ "text": "GitHub", "url": "https://github.com/..." }],
      "files": [{ "name": "Report", "url": "/download/report.pdf" }]
    }
  ]
}
```

### Upload Files

Place project files in `static/uploads/` directory and reference them in `projects.json`.

## Usage

### Home Page

- View featured projects
- See technical skills
- Quick introduction

### Projects Page

- Browse all projects
- Filter by category
- Access project details

### Project Details

- Full project description
- Technologies used
- Download resources
- External links

### About Page

- Personal introduction
- Skills and competencies
- Contact information

## Deployment

### Heroku Deployment

1. **Create Procfile**

   ```
   web: gunicorn app:app
   ```

2. **Add gunicorn to requirements.txt**

   ```bash
   pip install gunicorn
   pip freeze > requirements.txt
   ```

3. **Deploy to Heroku**
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   ```

### Other Platforms

The application can be deployed to:

- AWS (Elastic Beanstalk, EC2)
- Google Cloud Platform
- Azure App Service
- DigitalOcean
- Vercel/Netlify (with serverless setup)

## Security Notes

⚠️ **Important for Production:**

1. Change `SECRET_KEY` in `config.py`
2. Set `DEBUG = False` in production
3. Use environment variables for sensitive data
4. Implement HTTPS
5. Add CSRF protection for file uploads
6. Validate and sanitize all user inputs
7. Run `pip install python-dotenv` and use `.env` file:
   ```
   SECRET_KEY=your-production-secret-key
   FLASK_ENV=production
   ```

## Contributing

Feel free to fork this project and customize it for your own portfolio!

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please create an issue in the repository.

## Author

Data Engineer Portfolio - 2026

---

**Start showcasing your data engineering projects today!** 🚀
