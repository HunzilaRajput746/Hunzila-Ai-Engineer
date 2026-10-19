const projectsData = {
    'revenue-crm': {
        'title': 'Revenue.inc — Sales CRM & Operations Platform',
        'img': 'images/projects/revenue-analytics.png',
        'gallery': ['images/projects/revenue-analytics.png', 'images/projects/revenue-tasks.png', 'images/projects/revenue-dashboard.png'],
        'label': 'Production CRM Platform',
        'tech': ['React', 'Node.js', 'Express', 'MongoDB', 'Tailscale VPS', 'Tailwind CSS', 'AI Automation'],
        'desc': 'Full-stack enterprise CRM platform in live active production (dashboard.revenue.inc). Deployed and maintained on a private Tailscale-secured VPS. Integrates comprehensive sales analytics (calls tracking, closed TCV, MRR signed, conversion metrics), a developer task Kanban board with sprint refinement, automated SOP documentation, and AI-powered workflow automations.',
        'workflow': 'Full-stack application architecture built with React, Node.js, Express, and MongoDB. Secured via Tailscale private networking on dedicated VPS. Implements real-time sales pipeline tracking, dev sprint management, role-based admin controls, and automated client workflows.'
    },
    'c17-crm': {
        'title': 'C17 CRM — Lead & Customer Intelligence Platform',
        'img': 'images/projects/c17-dashboard.jpg',
        'label': 'Production CRM Platform',
        'tech': ['React', 'Node.js', 'Express', 'MongoDB', 'Tailscale Server', 'AI Workflows', 'REST API'],
        'desc': 'Enterprise-grade CRM platform currently live and in active use at dashboard.c17.ai. Built end-to-end to streamline lead tracking, customer deal stages, and AI-driven automation workflows. Securely deployed and orchestrated on a private VPS connected through Tailscale mesh networking.',
        'workflow': 'React client interfaces with Express/Node.js REST backend and MongoDB. Deployed on high-performance VPS with Tailscale private tunnel. Features automated lead scoring, dynamic deal stage tracking, customer lifecycle management, and intelligent notification triggers.'
    },
    'n8n-automation': {
        'title': 'Self-Hosted n8n Workflow Automation Engine',
        'img': 'images/projects/workflow.jpg',
        'label': 'DevOps & Automation',
        'tech': ['n8n', 'Oracle Cloud VPS', 'Docker', 'Webhooks', 'REST APIs', 'AI Agents'],
        'desc': 'Self-hosted production n8n automation engine deployed on Oracle Cloud VPS infrastructure. Powers custom multi-step event triggers, webhook ingestions, database synchronizations between MongoDB and external tools, and multi-agent AI execution pipelines with zero third-party subscription limits.',
        'workflow': 'Containerized n8n running on an Oracle Cloud compute instance. Listens to inbound webhooks from CRM and client apps, runs intelligent branch logic with AI nodes (Groq / OpenAI / LangChain), transforms payloads, and updates databases in real time.'
    },
    'p1': {
        'title': 'Smart Helmet with Navigation System',
        'img': 'images/projects/helmet.jpg',
        'label': 'Final Year Project · A+ Grade',
        'tech': ['Arduino', 'ESP32', 'Node.js', 'Express', 'Leaflet', 'Face-API', 'IoT'],
        'desc': 'Comprehensive IoT-based safety system integrating GPS navigation, crash detection, and facial recognition. Features real-time tracking dashboard, environmental monitoring with multiple sensors (GPS NEO-6M, Ultrasonic HC-SR04, MPU6050, DHT11), and automated emergency alerts with 95% reliability.',
        'workflow': 'Data from MPU6050 and DHT11 is processed by the ESP32. In case of anomaly (crash), GPS coordinates are fetched and an emergency payload is pushed via HTTP to the Node.js backend. The backend triggers SMS alerts and updates the real-time Leaflet.js dashboard using WebSockets. Face-API ensures only authorized riders can start the ignition.'
    },
    'gourmet-os': {
        'title': 'GourmetOS — Restaurant Operations System',
        'img': 'images/projects/orbitwork-employer-dashboard.png',
        'label': 'Full-Stack Next.js SaaS',
        'tech': ['Next.js App Router', 'MongoDB', 'Tailwind CSS', 'NextAuth', 'AI Assisted'],
        'desc': 'Full-stack restaurant operations platform featuring role-based authentication (Admin/Staff), interactive Point-of-Sale terminal, live Kitchen Display System (Kanban order flow), menu and inventory control, revenue analytics dashboard, and an AI-assisted menu pricing engine.',
        'workflow': 'Next.js App Router with React Server Components, MongoDB Atlas, and Tailwind CSS. NextAuth handles role-based credentials. Kitchen display updates orders live via API polling and WebSockets. AI pricing tool analyzes margins and ingredient costs to suggest optimal dish pricing.'
    },
    'p2': {
        'title': 'Breast Cancer Detection System',
        'img': 'images/projects/cancer.jpg',
        'label': 'Machine Learning',
        'tech': ['Python', 'Scikit-learn', 'TensorFlow', 'XGBoost', 'CNN', 'Pandas'],
        'desc': 'End-to-end machine learning pipeline for breast cancer detection. Performed comprehensive EDA, feature engineering, and class balancing. Trained Random Forest, XGBoost, and CNN classifiers with hyperparameter optimization achieving 96% accuracy.',
        'workflow': '1. Data ingestion & cleaning (Pandas). 2. Feature selection via PCA and correlation matrices. 3. Class balancing using SMOTE. 4. Model training across ensemble methods (XGBoost/RF) and a custom CNN. 5. Final inference pipeline exposed via FastAPI.'
    },
    'p10': {
        'title': 'Orbitwork — Job Board & Freelance Marketplace',
        'img': 'images/projects/orbitwork-employer-dashboard.png',
        'label': 'Full-Stack MERN',
        'tech': ['React', 'Material UI', 'Node.js', 'Express', 'MongoDB', 'Mongoose', 'JWT', 'bcryptjs'],
        'desc': 'Production-ready job board and freelance marketplace connecting employers with independent talent. Employers can publish roles, review applicants, and update application statuses, while candidates can search open positions, apply with cover messages, and track their applications.',
        'workflow': 'The React and Material UI client communicates with an Express REST API. MongoDB stores users, jobs, and applications through Mongoose models. JWT authentication and role-based middleware protect every private route, while server-side ownership checks prevent users from modifying resources they do not own. A compound MongoDB index prevents duplicate applications for the same job and candidate.',
        'gallery': ['images/projects/orbitwork-login.png', 'images/projects/orbitwork-employer-dashboard.png', 'images/projects/orbitwork-candidate-dashboard.png']
    },
    'p3': {
        'title': 'Video-based Depression Screening',
        'img': 'images/projects/depression.jpg',
        'label': 'Computer Vision',
        'tech': ['OpenCV', 'Python', 'CNN', 'LSTM', 'SVM', 'dlib', 'Audio Processing'],
        'desc': 'Advanced computer vision system for mental health screening. Built end-to-end pipeline extracting facial and audio features from user videos. Implemented feature-level fusion with CNN/LSTM and SVM classifiers using OpenCV facial landmarks and audio analysis.',
        'workflow': 'The system simultaneously processes the video stream (extracting Action Units via dlib/OpenCV) and audio stream (extracting MFCCs). A temporal CNN-LSTM network analyzes facial micro-expressions while an SVM classifies audio features. Both modalities are fused at the decision level to predict depression markers.'
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
