# Data Analytics Portfolio Website

A professional, modular Flask-based portfolio website optimized for data analytics job applications. Features SEO-friendly content with industry keywords, responsive design, and easy content management through JSON files.

## Features

- **SEO Optimized**: Packed with data analytics keywords (Python, SQL, Machine Learning, Tableau, Power BI, etc.)
- **Modular Design**: Add projects and certificates by simply adding JSON files
- **Responsive**: Mobile-friendly design that looks great on all devices
- **Professional UI**: Clean, easy-to-read design with professional color scheme
- **Single Page + Multi-page**: Scrollable landing page with separate page routes
- **Easy to Deploy**: Ready for PythonAnywhere hosting

## Project Structure

```
portfolio/
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
│
├── templates/
│   ├── base.html              # Base template
│   └── index.html             # Main landing page
│
├── static/
│   ├── css/
│   │   └── style.css          # Main stylesheet
│   ├── js/
│   │   ├── main.js            # Main JavaScript
│   │   └── contact.js         # Contact form handler
│   └── images/
│       ├── profile.jpg        # Your profile picture
│       ├── projects/          # Project images/screenshots
│       └── certificates/      # Certificate images
│
└── data/
    ├── profile.json           # Your personal information
    ├── projects/              # Project JSON files
    │   ├── project_example.json
    │   └── customer_segmentation.json
    └── certificates/          # Certificate JSON files
        └── cert_example.json
```

## Setup Instructions

### Local Development

1. **Clone or download the project files**

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser** and go to `http://localhost:5000`

### Deploying to PythonAnywhere

1. **Sign up** at [PythonAnywhere.com](https://www.pythonanywhere.com) (free tier available)

2. **Upload your files** using the Files tab

3. **Create a virtual environment** in the Bash console:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 myenv
   pip install flask
   ```

4. **Configure the Web app**:
   - Go to Web tab
   - Add a new web app
   - Choose Flask
   - Set the source code directory
   - Configure WSGI file to point to your app.py

5. **Reload the web app** and visit your URL

## Adding Content

### Setting Up Your Profile

Edit the `data/profile.json` file with your personal information:

```json
{
    "name": "Your Full Name",
    "title": "Data Analyst",
    "tagline": "Your professional tagline",
    "bio": "A brief description about yourself and your skills",
    "email": "your.email@example.com",
    "phone": "+1 (234) 567-8900",
    "location": "City, State, Country",
    "linkedin": "https://linkedin.com/in/yourprofile",
    "github": "https://github.com/yourusername",
    "image": "profile.jpg"
}
```

**Profile Image:**
- Place your profile picture in `static/images/`
- Name it `profile.jpg` (or update the filename in profile.json)
- Recommended: Square image, at least 400x400px
- Professional headshot works best

**Hero Background Image:**
- Place a background image named `background.jpg` in `static/images/`
- This will be used as the hero section background
- Recommended: High resolution (1920x1080px or larger)
- The image will be overlaid with a purple gradient (30% opacity) for readability
- Best with images that have good contrast or interesting patterns

### Adding a New Project

Create a new JSON file in `data/projects/` directory:

```json
{
    "title": "Your Project Title",
    "description": "Detailed description highlighting data analytics skills, tools used, and impact. Mention specific metrics and outcomes.",
    "date": "2024-11",
    "technologies": ["Python", "SQL", "Tableau", "Pandas"],
    "github": "https://github.com/yourusername/project",
    "demo": "https://your-demo-link.com",
    "image": "my_project_screenshot.png"
}
```

**Image Guidelines:**
- Place your project screenshot in `static/images/projects/`
- Recommended size: 800x500px (16:10 ratio)
- Supported formats: PNG, JPG, WebP
- If no image is provided, the card will adjust automatically

**Tips:**
- Use past tense and action verbs (Analyzed, Developed, Implemented)
- Include quantifiable results (increased by X%, processed Y records)
- Mention relevant technologies and methodologies
- Date format: YYYY-MM for automatic sorting

### Adding a New Certificate

Create a new JSON file in `data/certificates/` directory:

```json
{
    "title": "Certificate Name",
    "issuer": "Issuing Organization",
    "date": "2024-11",
    "credential_url": "https://credential-verification-link.com",
    "image": "my_certificate.png"
}
```

**Image Guidelines:**
- Place your certificate image in `static/images/certificates/`
- Recommended size: 600x400px (3:2 ratio)
- You can use a screenshot of your certificate or badge
- If no image is provided, a default certificate icon will be shown

## Customization

### Update Personal Information

Simply edit `data/profile.json` with your details. The website will automatically update:
- Your name in the navigation and hero section
- Profile picture (if provided)
- Contact information in about and contact sections
- Social media links in footer
- Bio and tagline

### Change Colors

Edit CSS variables in `static/css/style.css`:

```css
:root {
    --primary-color: #2563eb;      /* Main brand color */
    --secondary-color: #1e40af;    /* Secondary brand color */
    --accent-color: #3b82f6;       /* Accent color */
    /* ... other colors ... */
}
```

### Update Skills

Edit the skills grid in `templates/index.html` in the about section to match your expertise.

## SEO Keywords Included

The website is optimized for these data analytics keywords:
- Data Analyst, Data Analytics, Business Intelligence
- Python, SQL, R Programming
- Pandas, NumPy, Scikit-learn, Machine Learning
- Tableau, Power BI, Data Visualization
- Statistical Analysis, Predictive Modeling
- ETL, Data Mining, Data Cleaning
- Excel, Jupyter Notebook, Git
- Exploratory Data Analysis (EDA)
- Database Management, PostgreSQL, MySQL

## Best Practices for Recruiters

✅ **Clear Navigation**: One-click access to all sections
✅ **Quantifiable Results**: Projects show measurable impact
✅ **Technical Skills**: Comprehensive list of tools and technologies
✅ **Professional Design**: Clean, distraction-free layout
✅ **Mobile Responsive**: Looks great on phones and tablets
✅ **Fast Loading**: Optimized performance
✅ **Easy Contact**: Simple contact form

## Tips for Job Applications

1. **Update Regularly**: Add new projects and certificates as you complete them
2. **Tailor Projects**: Highlight projects relevant to the job you're applying for
3. **Use Keywords**: Match job description keywords in your project descriptions
4. **Show Impact**: Always include metrics and results
5. **Keep it Current**: Date your projects to show recent activity
6. **Link Everything**: Include GitHub links and live demos when possible

## Troubleshooting

**Projects/Certificates not showing?**
- Ensure JSON files are in the correct directories
- Check JSON syntax is valid (use a JSON validator)
- Restart the Flask application

**Styles not loading?**
- Clear browser cache
- Check file paths in templates
- Ensure static folder structure is correct

**Contact form not working?**
- Check browser console for errors
- Verify the `/send-message` route is accessible
- Add email functionality using Flask-Mail if needed

## License

This project is free to use for personal portfolio purposes.

## Support

For questions or issues, feel free to reach out through the contact form on your deployed site.

---

**Good luck with your job search! 🚀**