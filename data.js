const projectsData = {
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
        'label': 'Vibe Coded 2025',
        'tech': ['Python', 'Selenium', 'BeautifulSoup', 'Pandas', 'OpenPyXL', 'MD5 Hashing'],
        'desc': 'End-to-end lead generation scraper targeting Google Maps. Extracts business emails, phone numbers, and metadata with no listing cap — scrapes till the last result. Supports multi-city input (semicolon-separated), combined Excel export with city-by-city breakdown, and MD5-based duplicate detection across cells and sessions.',
        'workflow': 'Selenium drives the hidden browser to inject scroll events into the Maps results pane. BeautifulSoup parses the DOM dynamically. Extracted nodes are hashed via MD5 to prevent duplicates in the Pandas DataFrame. Finally, data is chunked and written to formatted Excel sheets via OpenPyXL.'
    },
    'p5': {
        'title': 'AI Social Media Auto-Poster Bot',
        'img': 'images/projects/social-bot.jpg',
        'label': 'Vibe Coded 2025',
        'tech': ['Python', 'LinkedIn API v2', 'Facebook Graph API', 'OpenAI', 'python-dotenv'],
        'desc': 'AI-powered automation bot that generates topic-based content and simultaneously posts to LinkedIn (API v2), Facebook Pages, and multiple Facebook Groups via Graph API. Handles FB image limitation by pre-uploading images as unpublished Page posts.',
        'workflow': '1. Fetches trending topics or user prompts. 2. Calls OpenAI API to generate platform-optimized copy. 3. Authenticates via OAuth2 (LinkedIn/FB). 4. If image is included, pre-uploads to FB Graph API to get Media ID. 5. Dispatches final payloads asynchronously to all targeted platforms.'
    },
    'p6': {
        'title': 'N8N Workflow Generator (Groq AI)',
        'img': 'images/projects/workflow.jpg',
        'label': 'Vibe Coded 2025',
        'tech': ['Python', 'Groq API', 'n8n', 'CLI', 'NLP'],
        'desc': 'CLI tool using Groq API to auto-generate n8n automation workflows from natural language prompts. Integrated python-dotenv for secure API key management. Describe a workflow in plain English, get a ready-to-import n8n JSON instantly — 3-step setup.',
        'workflow': 'User inputs a natural language prompt via the CLI. The prompt is injected into a specialized system prompt detailing the n8n JSON schema. The payload is sent to Groq API (Llama 3). The response is parsed, validated against the n8n schema, and saved as a downloadable JSON file ready for import.'
    },
    'p7': {
        'title': 'HealthSaaS — AI Clinic Management',
        'img': 'images/projects/health-saas.jpg',
        'label': 'Vibe Coded 2025',
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
        'workflow': 'Data loaded via Pandas from raw CSVs. Cleaned missing values and handled datetime conversions. GroupBy aggregations and statistical analysis performed to identify key trends. Interactive Plotly charts (bar, scatter, heatmaps) generated for reporting.'
    }
};
