import json

# Project Data for the Modal
projects_data = {
    'p1': {
        'title': 'Smart Helmet with Navigation System',
        'img': 'images/projects/helmet.jpg',
        'label': 'Featured Project',
        'tech': ['Arduino', 'ESP32', 'Node.js', 'Express', 'Leaflet', 'Face-API', 'IoT'],
        'desc': 'Comprehensive IoT-based safety system integrating GPS navigation, crash detection, and facial recognition. Features real-time tracking dashboard, environmental monitoring with multiple sensors (GPS NEO-6M, Ultrasonic HC-SR04, MPU6050, DHT11), and automated emergency alerts with 95% reliability.',
        'workflow': 'Data from MPU6050 and DHT11 is processed by the ESP32. In case of anomaly (crash), GPS coordinates are fetched and an emergency payload is pushed via HTTP to the Node.js backend. The backend triggers SMS alerts and updates the real-time Leaflet.js dashboard using WebSockets. Face-API ensures only authorized riders can start the ignition.'
    },
    'p2': {
        'title': 'Breast Cancer Detection System',
        'img': 'images/projects/cancer.jpg',
        'label': 'Machine Learning',
        'tech': ['Python', 'Scikit-learn', 'TensorFlow', 'XGBoost', 'CNN', 'Pandas'],
        'desc': 'End-to-end machine learning pipeline for breast cancer detection. Performed comprehensive EDA, feature engineering, and class balancing. Trained Random Forest, XGBoost, and CNN classifiers with hyperparameter optimization achieving 96% accuracy.',
        'workflow': '1. Data ingestion & cleaning (Pandas). 2. Feature selection via PCA and correlation matrices. 3. Class balancing using SMOTE. 4. Model training across ensemble methods (XGBoost/RF) and a custom CNN. 5. Final inference pipeline exposed via FastAPI.'
    },
    'p3': {
        'title': 'Video-based Depression Screening',
        'img': 'images/projects/depression.jpg',
        'label': 'Computer Vision',
        'tech': ['OpenCV', 'Python', 'CNN', 'LSTM', 'SVM', 'dlib', 'Audio Processing'],
        'desc': 'Advanced computer vision system for mental health screening. Built end-to-end pipeline extracting facial and audio features from user videos. Implemented feature-level fusion with CNN/LSTM and SVM classifiers using OpenCV facial landmarks and audio analysis.',
        'workflow': 'The system simultaneously processes the video stream (extracting Action Units via dlib/OpenCV) and audio stream (extracting MFCCs). A temporal CNN-LSTM network analyzes facial micro-expressions while an SVM classifies audio features. Both modalities are fused at the decision level to predict depression markers.'
    },
    'p4': {
        'title': 'Google Maps Lead Scraper',
        'img': 'images/projects/maps-scraper.jpg',
        'label': '⚡ Vibe Coded · 2025',
        'tech': ['Python', 'Selenium', 'BeautifulSoup', 'Pandas', 'OpenPyXL', 'MD5 Hashing'],
        'desc': 'End-to-end lead generation scraper targeting Google Maps. Extracts business emails, phone numbers, and metadata with no listing cap — scrapes till the last result. Supports multi-city input (semicolon-separated), combined Excel export with city-by-city breakdown, and MD5-based duplicate detection across cells and sessions.',
        'workflow': 'Selenium drives the hidden browser to inject scroll events into the Maps results pane. BeautifulSoup parses the DOM dynamically. Extracted nodes are hashed via MD5 to prevent duplicates in the Pandas DataFrame. Finally, data is chunked and written to formatted Excel sheets via OpenPyXL.'
    },
    'p5': {
        'title': 'AI Social Media Auto-Poster Bot',
        'img': 'images/projects/social-bot.jpg',
        'label': '⚡ Vibe Coded · 2025',
        'tech': ['Python', 'LinkedIn API v2', 'Facebook Graph API', 'OpenAI', 'python-dotenv'],
        'desc': 'AI-powered automation bot that generates topic-based content and simultaneously posts to LinkedIn (API v2), Facebook Pages, and multiple Facebook Groups via Graph API. Handles FB image limitation by pre-uploading images as unpublished Page posts.',
        'workflow': '1. Fetches trending topics or user prompts. 2. Calls OpenAI API to generate platform-optimized copy. 3. Authenticates via OAuth2 (LinkedIn/FB). 4. If image is included, pre-uploads to FB Graph API to get Media ID. 5. Dispatches final payloads asynchronously to all targeted platforms.'
    },
    'p6': {
        'title': 'N8N Workflow Generator (Groq AI)',
        'img': 'images/projects/workflow.jpg',
        'label': '⚡ Vibe Coded · 2025',
        'tech': ['Python', 'Groq API', 'n8n', 'CLI', 'NLP'],
        'desc': 'CLI tool using Groq API to auto-generate n8n automation workflows from natural language prompts. Integrated python-dotenv for secure API key management. Describe a workflow in plain English, get a ready-to-import n8n JSON instantly — 3-step setup.',
        'workflow': 'User inputs a natural language prompt via the CLI. The prompt is injected into a specialized system prompt detailing the n8n JSON schema. The payload is sent to Groq API (Llama 3). The response is parsed, validated against the n8n schema, and saved as a downloadable JSON file ready for import.'
    },
    'p7': {
        'title': 'HealthSaaS — AI Clinic Management',
        'img': 'images/projects/health-saas.jpg',
        'label': '⚡ Vibe Coded · 2025',
        'tech': ['FastAPI', 'MongoDB', 'Next.js', 'Groq AI', 'Twilio', 'Railway', 'Vercel'],
        'desc': 'Full-stack AI-powered clinic management SaaS with a smart chatbot receptionist handling appointment booking, doctor scheduling, and lab test queries 24/7. REST backend with FastAPI and MongoDB; integrated Groq AI for conversational responses and Twilio for WhatsApp booking confirmations.',
        'workflow': 'Client interacts with Next.js frontend or WhatsApp (via Twilio). FastAPI backend orchestrates requests. Conversational queries hit Groq AI. Structured booking intents trigger MongoDB transactions. Real-time dashboard updates via WebSockets for the clinic admins.'
    },
    'p8': {
        'title': 'Wanderlust — Travel Platform',
        'img': 'images/projects/travel.jpg',
        'label': 'Full Stack Web',
        'tech': ['MongoDB', 'Express', 'React', 'Node.js', 'JWT', 'Cloudinary'],
        'desc': 'Full-stack MERN travel listing platform with complete authentication using Passport and JWT. Features responsive Bootstrap UI, secure image uploads via Multer and Cloudinary, comprehensive CRUD operations, and advanced search/filter functionality. Deployed on Vercel with MongoDB Atlas.',
        'workflow': 'Standard MVC architecture. React frontend communicates with Express API. JWT validates protected routes. Images are streamed directly to Cloudinary during upload, storing only secure URLs in MongoDB Atlas. Geolocation queries filter listings based on user proximity.'
    },
    'p9': {
        'title': 'IPL Data Analytics',
        'img': 'images/projects/analytics.jpg',
        'label': 'Data Science',
        'tech': ['Python', 'Pandas', 'Plotly', 'Data Analysis', 'Visualization'],
        'desc': 'Comprehensive EDA on IPL match and player datasets using Pandas and Plotly. Extracted actionable insights including top scorers, strike rates, venue patterns, and team performance metrics to support stakeholder decisions in scouting and strategic analysis.',
        'workflow': 'Raw CSV data ingested via Pandas. Extensive cleaning (handling nulls, standardizing team names). Aggregation of player stats. Plotly used to generate interactive dashboards detailing run-rates, toss-decisions impact, and predictive factors for team victories.'
    }
}

# Generate JS code block
js_data_block = f"const projectsData = {json.dumps(projects_data, indent=2)};"

# Read existing script.js
with open('D:/My_projects/portfolio/script.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Update Typing Phrases & Speed
import re
js_content = re.sub(r'const phrases = \[.*?\];', "const phrases = ['AI Engineer', 'Agentic AI Expert'];", js_content, flags=re.DOTALL)
js_content = js_content.replace('setTimeout(typeLoop, isDeleting ? 55 : 90);', 'setTimeout(typeLoop, isDeleting ? 40 : 120);')
js_content = js_content.replace('setTimeout(typeLoop, 1800);', 'setTimeout(typeLoop, 2500);')

# Add Modal Logic at the end
modal_js = f'''
/* ═══════════════════════════════════
   PROJECT MODAL (IMMERSIVE DETAIL VIEW)
═══════════════════════════════════ */
{js_data_block}

const modal = document.getElementById('projectModal');
const modalClose = document.querySelector('.modal-close');
const projectCards = document.querySelectorAll('.project-card');

function openModal(id) {
    const data = projectsData[id];
    if(!data) return;

    // Populate Data
    document.getElementById('modalImg').src = data.img;
    document.getElementById('modalLabel').textContent = data.label;
    document.getElementById('modalTitle').textContent = data.title;
    document.querySelector('.modal-description p').textContent = data.desc;
    document.getElementById('modalWorkflow').innerHTML = <p></p>;
    
    // Populate Tech
    const techHtml = data.tech.map(t => <span></span>).join('');
    document.getElementById('modalTech').innerHTML = techHtml;

    // Open Animation (Spring Physics feel via GSAP)
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';

    gsap.fromTo(modal, 
        {{ opacity: 0 }}, 
        {{ opacity: 1, duration: 0.4, ease: 'power2.out' }}
    );
    
    gsap.fromTo('.modal-container',
        {{ y: 100, scale: 0.95, opacity: 0 }},
        {{ y: 0, scale: 1, opacity: 1, duration: 0.7, ease: 'back.out(1.4)', delay: 0.1 }}
    );
}

function closeModal() {
    gsap.to('.modal-container', {{
        y: 60, scale: 0.95, opacity: 0, duration: 0.4, ease: 'power2.in'
    }});
    gsap.to(modal, {{
        opacity: 0, duration: 0.4, ease: 'power2.in', delay: 0.1,
        onComplete: () => {{
            modal.classList.remove('active');
            document.body.style.overflow = '';
        }}
    }});
}

projectCards.forEach(card => {{
    card.style.cursor = 'pointer';
    card.addEventListener('click', (e) => {{
        // Prevent opening if clicking on github/link icons
        if(e.target.closest('.project-link')) return;
        const id = card.getAttribute('data-project-id');
        if(id) openModal(id);
    }});
}});

if(modalClose) modalClose.addEventListener('click', closeModal);
if(modal) modal.addEventListener('click', (e) => {{
    if(e.target === modal || e.target.classList.contains('modal-backdrop')) closeModal();
}});
'''

if 'const projectsData =' not in js_content:
    with open('D:/My_projects/portfolio/script.js', 'a', encoding='utf-8') as f:
        f.write(modal_js)
    print("JS updated successfully!")
else:
    print("JS already contains modal logic.")
