import os

css_content = """@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=DM+Mono:ital,wght@0,300;0,400;0,500;1,400&family=Inter:wght@300;400;500;600;700&display=swap');

/* -------------------------------------------------------------
   ULTRA-PREMIUM LUXURY PORTFOLIO - PEARL WHITE & CHAMPAGNE GOLD
------------------------------------------------------------- */
:root {
  /* Luxury Light Color Scheme */
  --bg-base:       #fafafa; /* Pearl White */
  --bg-surface:    #ffffff; /* Pure White */
  --bg-raised:     #f4f4f5; /* Light Gray */
  --bg-card:       #ffffff;

  /* Accents */
  --accent:        #b8860b; /* Dark Goldenrod / Champagne */
  --accent-soft:   #8a7d6b; /* Muted Gold/Taupe */
  --accent-dim:    rgba(184, 134, 11, 0.08);
  --teal:          #71717a; /* Zinc/Silver for gradients */
  --teal-dim:      rgba(113, 113, 122, 0.08);
  --rose:          #b76e79;
  --amber:         #d97706;
  --cyan:          #b8860b;

  /* Text */
  --text-1:  #18181b; /* Deep Charcoal (Almost Black) */
  --text-2:  #52525b; /* Slate Gray */
  --text-3:  #71717a; /* Light Slate */
  --text-muted: #d4d4d8;

  /* Borders & Shadows */
  --border:       rgba(0, 0, 0, 0.06);
  --border-med:   rgba(0, 0, 0, 0.12);
  --border-hi:    rgba(184, 134, 11, 0.2);
  --shadow-sm:    0 8px 24px rgba(0,0,0,0.03);
  --shadow-md:    0 16px 40px rgba(0,0,0,0.06);
  --shadow-lg:    0 32px 80px rgba(0,0,0,0.1);

  /* Typography */
  --font-sans:  'Inter', system-ui, sans-serif;
  --font-mono:  'DM Mono', 'Fira Code', monospace;
  --font-head:  'Outfit', sans-serif;

  /* Layout */
  --r-sm:  4px;
  --r-md:  8px;
  --r-lg:  16px;
  --r-xl:  24px;
  
  --ease-out:    cubic-bezier(0.16, 1, 0.3, 1);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* -- Reset -- */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; overflow-x: hidden; }
body {
  font-family: var(--font-sans);
  background: var(--bg-base);
  color: var(--text-1);
  line-height: 1.8;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
  cursor: auto;
}
.cursor, .cursor-follower { display: none !important; }

/* Noise Background - Extremely subtle for texture */
body::before {
  content: ''; position: fixed; inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.03'/%3E%3C/svg%3E");
  z-index: 10000; pointer-events: none; opacity: 0.6; mix-blend-mode: multiply;
}
/* Ambient Glows - Very diffuse gold */
.bg-glow-1 { position: fixed; top: -30vh; left: -20vw; width: 80vw; height: 80vw; background: radial-gradient(circle, rgba(184,134,11,0.02) 0%, transparent 50%); z-index: 0; pointer-events: none; }
.bg-glow-2 { position: fixed; bottom: -30vh; right: -20vw; width: 80vw; height: 80vw; background: radial-gradient(circle, rgba(113,113,122,0.02) 0%, transparent 50%); z-index: 0; pointer-events: none; }

/* -------------------------------------------------------------
   PRELOADER (Elegant Agentic)
------------------------------------------------------------- */
#preloader {
  position: fixed; inset: 0; background: var(--bg-base);
  display: flex; align-items: center; justify-content: center;
  z-index: 999999; transition: opacity 1.2s ease, visibility 1.2s ease;
}
#preloader.hidden { opacity: 0; visibility: hidden; }
.preloader-content { text-align: center; display: flex; flex-direction: column; align-items: center; gap: 32px; }
.preloader-neural {
  position: relative; width: 70px; height: 70px; display: flex; align-items: center; justify-content: center;
  border-radius: 50%; background: rgba(184, 134, 11, 0.05); border: 1px solid rgba(184, 134, 11, 0.2);
  box-shadow: 0 0 50px rgba(184, 134, 11, 0.05);
}
.preloader-neural::before, .preloader-neural::after {
  content: ''; position: absolute; inset: -1px; border-radius: 50%;
  border: 1px solid transparent; border-top-color: rgba(184, 134, 11, 0.6); animation: spinSlow 3s cubic-bezier(0.4, 0, 0.2, 1) infinite;
}
.preloader-neural::after { inset: -15px; border-top-color: rgba(113, 113, 122, 0.3); border-bottom-color: rgba(184, 134, 11, 0.2); animation: spinSlow 5s linear infinite reverse; }
@keyframes spinSlow { to { transform: rotate(360deg); } }
.preloader-icon { font-size: 1.8rem; color: var(--accent); animation: pulseBrain 3s ease-in-out infinite; }
@keyframes pulseBrain { 0%, 100% { transform: scale(1); filter: drop-shadow(0 0 10px rgba(184,134,11,0.3)); } 50% { transform: scale(1.05); filter: drop-shadow(0 0 20px rgba(184,134,11,0.5)); } }
.glitch-wrapper { margin-top: 10px; }
.glitch { font-family: var(--font-head); font-size: 1.4rem; font-weight: 400; letter-spacing: 0.3em; color: var(--text-1); position: relative; text-transform: uppercase; }
.loading-bar { width: 240px; height: 1px; background: rgba(0,0,0,0.1); overflow: hidden; position: relative; margin-top: 5px; }
.loading-progress { position: absolute; top: 0; left: 0; height: 100%; width: 0%; background: var(--accent); box-shadow: 0 0 15px var(--accent); transition: width 0.1s linear; }
.loading-text { font-family: var(--font-mono); font-size: 0.7rem; color: var(--text-2); letter-spacing: 0.2em; text-transform: uppercase; margin-top: 15px; }

/* -------------------------------------------------------------
   NAVBAR
------------------------------------------------------------- */
.navbar { position: fixed; top: 0; left: 0; right: 0; z-index: 1000; padding: 32px 0; transition: all 0.6s var(--ease-out); }
.navbar.scrolled { background: rgba(255, 255, 255, 0.85); backdrop-filter: blur(30px) saturate(180%); -webkit-backdrop-filter: blur(30px) saturate(180%); border-bottom: 1px solid var(--border); padding: 20px 0; box-shadow: var(--shadow-sm); }
.nav-container { max-width: 1400px; margin: 0 auto; padding: 0 40px; display: flex; align-items: center; justify-content: space-between; }
.logo { font-family: var(--font-head); font-size: 1.2rem; font-weight: 500; color: var(--text-1); text-decoration: none; letter-spacing: 0.2em; text-transform: uppercase; }
.logo-bracket { color: var(--accent); font-weight: 400; }
.nav-menu { list-style: none; display: flex; gap: 32px; align-items: center; margin: 0; padding: 0; }
.nav-link { font-family: var(--font-sans); font-size: 0.85rem; font-weight: 500; color: var(--text-2); text-decoration: none; letter-spacing: 0.05em; transition: all 0.4s ease; position: relative; }
.nav-link::after { content: ''; position: absolute; bottom: -4px; left: 0; width: 0%; height: 1px; background: var(--accent); transition: width 0.4s var(--ease-out); }
.nav-link:hover { color: var(--text-1); }
.nav-link:hover::after, .nav-link.active::after { width: 100%; }
.nav-link.active { color: var(--text-1); }
.hamburger { display: none; flex-direction: column; gap: 6px; cursor: pointer; padding: 8px; background: none; border: none; }
.hamburger span { display: block; width: 30px; height: 1px; background: var(--text-1); transition: all 0.3s ease; }

/* -------------------------------------------------------------
   HERO SECTION
------------------------------------------------------------- */
.hero-section { min-height: 100vh; display: flex; align-items: center; position: relative; overflow: hidden; padding: 140px 0 80px; }
#particles-js { position: absolute; inset: 0; z-index: 0; opacity: 0.2; filter: invert(1); } /* Dark particles on light bg */
.hero-content { max-width: 1400px; margin: 0 auto; padding: 0 40px; display: grid; grid-template-columns: 1fr 500px; gap: 100px; align-items: center; position: relative; z-index: 2; width: 100%; }
.hero-badge { display: inline-flex; align-items: center; gap: 12px; background: transparent; border: 1px solid var(--border-med); border-radius: 99px; padding: 10px 24px; font-family: var(--font-mono); font-size: 0.8rem; color: var(--text-2); letter-spacing: 0.15em; margin-bottom: 40px; text-transform: uppercase; }
.hero-badge-dot { width: 6px; height: 6px; background: var(--accent); border-radius: 50%; box-shadow: 0 0 10px rgba(184,134,11,0.3); animation: pulseDot 2s infinite; }
@keyframes pulseDot { 0%, 100% { opacity: 1; transform: scale(1); } 50% { opacity: 0.4; transform: scale(0.8); } }
.hero-title { font-family: var(--font-head); font-size: clamp(3.5rem, 7vw, 6rem); font-weight: 300; line-height: 1.1; letter-spacing: -0.04em; margin-bottom: 24px; color: var(--text-1); }
.text-line { display: block; }
.hero-title .highlight { font-weight: 600; background: linear-gradient(135deg, #18181b 0%, var(--accent) 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.typing-container { font-family: var(--font-head); font-size: 1.5rem; font-weight: 400; color: var(--accent); margin-bottom: 32px; min-height: 2em; display: flex; align-items: center; gap: 4px; letter-spacing: 0.05em; }
.cursor-blink { animation: blink 1s step-end infinite; color: var(--accent); font-weight: 300; }
@keyframes blink { 50% { opacity: 0; } }
.hero-description { font-size: 1.15rem; color: var(--text-2); max-width: 600px; line-height: 1.9; margin-bottom: 56px; font-weight: 400; }
.hero-cta { display: flex; gap: 24px; flex-wrap: wrap; margin-bottom: 48px; align-items: center; }

/* Buttons (Luxury Minimal Light) */
.btn { display: inline-flex; align-items: center; justify-content: center; gap: 12px; padding: 18px 40px; font-family: var(--font-sans); font-weight: 500; font-size: 0.9rem; letter-spacing: 0.1em; text-transform: uppercase; text-decoration: none; transition: all 0.4s var(--ease-out); cursor: pointer; border: 1px solid transparent; position: relative; overflow: hidden; }
.btn-primary { background: var(--text-1); color: #fff; }
.btn-primary:hover { background: var(--accent); color: #fff; box-shadow: 0 10px 30px rgba(184,134,11,0.2); transform: translateY(-2px); }
.btn-secondary { background: transparent; color: var(--text-1); border-color: var(--border-med); }
.btn-secondary:hover { border-color: var(--text-1); transform: translateY(-2px); background: rgba(0,0,0,0.02); }

.social-links { display: flex; gap: 16px; }
.social-icon { width: 48px; height: 48px; display: flex; align-items: center; justify-content: center; border-radius: 50%; border: 1px solid var(--border); color: var(--text-2); font-size: 1.1rem; transition: all 0.4s var(--ease-out); background: transparent; }
.social-icon:hover { color: var(--accent); border-color: var(--accent); transform: translateY(-4px); background: #fff; box-shadow: var(--shadow-sm); }

.hexagon-wrapper { width: 450px; height: 450px; position: relative; margin: 0 auto; }
.hexagon-svg { width: 100%; height: 100%; position: absolute; top: 0; left: 0; z-index: 2; opacity: 0.5; }
.hexagon-border { fill: none; stroke: var(--accent); stroke-width: 0.5; opacity: 0.6; stroke-dasharray: 4 4; }
.profile-pic { width: 400px; height: 400px; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); z-index: 1; overflow: hidden; border-radius: 50%; background: var(--bg-card); border: 1px solid var(--border-med); box-shadow: inset 0 0 30px rgba(0,0,0,0.05), var(--shadow-md); }
.avatar-placeholder1 { width: 100%; height: 100%; object-fit: cover; filter: sepia(20%) contrast(1.1); transition: filter 0.8s ease; }
.hexagon-wrapper:hover .avatar-placeholder1 { filter: sepia(0%) contrast(1.05); }

/* -------------------------------------------------------------
   GLOBAL SECTIONS
------------------------------------------------------------- */
section { padding: 180px 0; position: relative; z-index: 1; border-top: 1px solid var(--border); }
section:first-of-type { border-top: none; }
.container { max-width: 1400px; margin: 0 auto; padding: 0 40px; }
.section-header { margin-bottom: 80px; display: flex; flex-direction: column; align-items: flex-start; }
.section-number { font-family: var(--font-mono); font-size: 0.85rem; color: var(--accent); letter-spacing: 0.2em; display: block; margin-bottom: 24px; font-weight: 500; }
.section-title { font-family: var(--font-head); font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 300; color: var(--text-1); letter-spacing: -0.03em; margin-bottom: 0; }

.reveal { transition: opacity 0.8s var(--ease-out), transform 0.8s var(--ease-out); }

/* -------------------------------------------------------------
   ABOUT SECTION
------------------------------------------------------------- */
.about-section { background: var(--bg-surface); }
.about-content { display: grid; grid-template-columns: 1.5fr 1fr; gap: 100px; align-items: start; }
.lead-text { font-size: 1.4rem; color: var(--text-1); line-height: 1.8; margin-bottom: 32px; font-weight: 400; }
.about-text p { color: var(--text-2); line-height: 1.9; margin-bottom: 24px; font-size: 1.1rem; font-weight: 400; }
.about-text .highlight { color: var(--text-1); font-weight: 500; border-bottom: 1px solid var(--accent-dim); }
.about-highlights { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-top: 48px; }
.highlight-item { display: flex; align-items: flex-start; gap: 20px; padding: 32px; background: transparent; border: 1px solid var(--border); transition: all 0.4s ease; border-radius: var(--r-md); }
.highlight-item:hover { border-color: var(--accent-dim); background: #ffffff; box-shadow: var(--shadow-sm); }
.highlight-item i { font-size: 1.2rem; color: var(--accent); flex-shrink: 0; margin-top: 4px; }
.highlight-item h4 { font-family: var(--font-sans); font-size: 0.8rem; color: var(--text-3); text-transform: uppercase; letter-spacing: 0.15em; margin-bottom: 12px; font-weight: 600; }
.highlight-item p { font-size: 1.15rem; color: var(--text-1); font-weight: 500; }
.stat-card { padding: 40px; background: transparent; border: 1px solid var(--border); border-radius: var(--r-md); display: flex; flex-direction: column; gap: 16px; margin-bottom: 24px; transition: all 0.4s ease; }
.stat-card:hover { border-color: var(--border-med); background: #ffffff; box-shadow: var(--shadow-sm); }
.stat-icon { font-size: 1.2rem; color: var(--accent); }
.stat-number { font-family: var(--font-head); font-size: 4rem; font-weight: 300; line-height: 1; color: var(--text-1); }
.stat-label { font-size: 0.9rem; color: var(--text-2); font-weight: 500; letter-spacing: 0.05em; text-transform: uppercase; }

/* -------------------------------------------------------------
   SKILLS SECTION
------------------------------------------------------------- */
.skills-section { background: var(--bg-base); }
.skills-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px; }
.skill-category { background: transparent; padding: 48px; border: 1px solid var(--border); border-radius: var(--r-md); transition: all 0.4s ease; }
.skill-category:hover { border-color: var(--border-med); background: #ffffff; box-shadow: var(--shadow-sm); }
.skill-category h3 { font-family: var(--font-head); font-size: 1.2rem; font-weight: 500; color: var(--text-1); margin-bottom: 40px; display: flex; align-items: center; gap: 16px; letter-spacing: 0.05em; text-transform: uppercase; }
.skill-category h3 i { color: var(--accent); font-size: 1rem; }
.skill-item { margin-bottom: 32px; }
.skill-info { display: flex; justify-content: space-between; margin-bottom: 12px; font-family: var(--font-sans); font-size: 0.95rem; font-weight: 400; color: var(--text-2); }
.skill-bar { width: 100%; height: 2px; background: var(--border-med); overflow: hidden; }
.skill-progress { height: 100%; background: var(--accent); width: 0; transition: width 1.5s cubic-bezier(0.1, 0.7, 0.1, 1); }
.tools-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; }
.tool-tag { display: inline-flex; align-items: center; gap: 12px; padding: 12px 0; font-family: var(--font-sans); font-size: 0.95rem; font-weight: 400; color: var(--text-2); transition: all 0.3s ease; border-bottom: 1px solid transparent; }
.tool-tag i { color: var(--text-3); font-size: 0.9rem; transition: color 0.3s ease; }
.tool-tag:hover { color: var(--text-1); border-bottom-color: var(--border-med); }
.tool-tag:hover i { color: var(--accent); }

/* -------------------------------------------------------------
   AGENTIC AI SERVICES
------------------------------------------------------------- */
.agentic-section { background: var(--bg-surface); }
.agentic-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px; }
.agentic-card { background: transparent; padding: 64px 40px; border: 1px solid var(--border); border-radius: var(--r-md); text-align: left; transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1); }
.agentic-card:hover { border-color: var(--border-med); background: #ffffff; box-shadow: var(--shadow-sm); transform: translateY(-8px); }
.agentic-icon { font-size: 1.5rem; color: var(--accent); margin-bottom: 40px; transition: transform 0.5s ease; }
.agentic-card:hover .agentic-icon { transform: scale(1.1); }
.agentic-card h3 { font-family: var(--font-head); font-size: 1.5rem; font-weight: 400; color: var(--text-1); margin-bottom: 24px; letter-spacing: -0.01em; }
.agentic-card p { font-size: 1.05rem; color: var(--text-2); line-height: 1.8; margin-bottom: 32px; font-weight: 400; }
.agentic-features { list-style: none; margin-top: 32px; padding-top: 32px; border-top: 1px solid var(--border); }
.agentic-features li { display: flex; align-items: flex-start; gap: 16px; margin-bottom: 16px; font-size: 0.95rem; font-weight: 400; color: var(--text-2); }
.agentic-features li i { color: var(--accent); font-size: 0.7rem; margin-top: 6px; }

/* -------------------------------------------------------------
   EXPERIENCE (TIMELINE) & EDUCATION
------------------------------------------------------------- */
.education-section { background: var(--bg-base); }
.timeline { position: relative; padding-left: 0; max-width: 1000px; margin: 0 auto; }
.timeline::before { display: none; }
.timeline-item, .edu-item { padding: 48px 0; border-bottom: 1px solid var(--border); display: grid; grid-template-columns: 200px 1fr; gap: 48px; align-items: start; transition: all 0.4s ease; }
.timeline-item:last-child, .edu-item:last-child { border-bottom: none; }
.timeline-item:hover, .edu-item:hover { background: #ffffff; padding-left: 24px; padding-right: 24px; margin-left: -24px; width: calc(100% + 48px); box-shadow: var(--shadow-sm); border-radius: var(--r-md); border-bottom-color: transparent; }
.timeline-date, .edu-date { font-family: var(--font-mono); font-size: 0.85rem; color: var(--text-3); letter-spacing: 0.1em; margin: 0; padding-top: 8px; font-weight: 500; }
.timeline-content, .edu-content { padding: 0; background: transparent; border: none; box-shadow: none; }
.timeline-content:hover, .edu-content:hover { transform: none; box-shadow: none; background: transparent; border-color: transparent; }
.timeline-dot, .edu-icon { display: none; }
.timeline-content h3, .edu-content h3 { font-family: var(--font-head); font-size: 1.6rem; font-weight: 500; color: var(--text-1); margin-bottom: 8px; }
.timeline-content h4, .edu-content h4 { font-size: 1.1rem; color: var(--accent); font-weight: 400; margin-bottom: 24px; }
.timeline-content p, .edu-description { font-size: 1.1rem; color: var(--text-2); line-height: 1.8; margin-bottom: 24px; font-weight: 400; }
.edu-highlights { display: flex; flex-direction: column; gap: 12px; }
.edu-highlights .highlight { display: flex; align-items: flex-start; gap: 12px; color: var(--text-2); font-size: 0.95rem; font-weight: 400; }
.edu-highlights .highlight i { color: var(--accent); font-size: 0.7rem; margin-top: 6px; }

/* -------------------------------------------------------------
   PROJECTS
------------------------------------------------------------- */
.projects-section { background: var(--bg-surface); }
.projects-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(450px, 1fr)); gap: 48px; }
.project-card { background: transparent; border: 1px solid var(--border); border-radius: var(--r-md); overflow: hidden; transition: all 0.6s cubic-bezier(0.16, 1, 0.3, 1); display: flex; flex-direction: column; cursor: pointer; }
.project-card:hover { border-color: var(--border-med); transform: translateY(-8px); box-shadow: var(--shadow-md); background: #ffffff; }
.project-image { position: relative; height: 320px; overflow: hidden; background: #eaeaea; }
.project-img { width: 100%; height: 100%; object-fit: cover; opacity: 0.85; transition: all 0.8s ease; filter: sepia(10%); }
.project-card:hover .project-img { transform: scale(1.05); opacity: 1; filter: sepia(0%); }
.project-overlay { display: none; }
.project-info { padding: 40px; flex: 1; display: flex; flex-direction: column; }
.vibe-label { display: inline-block; font-family: var(--font-mono); font-size: 0.75rem; color: var(--accent); margin-bottom: 20px; text-transform: uppercase; letter-spacing: 0.2em; font-weight: 500; }
.project-info h3 { font-family: var(--font-head); font-size: 1.8rem; font-weight: 400; margin-bottom: 16px; color: var(--text-1); letter-spacing: -0.01em; }
.project-description { font-size: 1.05rem; color: var(--text-2); line-height: 1.8; margin-bottom: 32px; font-weight: 400; }
.project-tech { display: flex; flex-wrap: wrap; gap: 12px; margin-top: auto; }
.project-tech span { font-family: var(--font-sans); font-size: 0.85rem; color: var(--text-3); font-weight: 500; letter-spacing: 0.05em; }
.project-tech span::after { content: '•'; margin-left: 12px; color: var(--border-med); }
.project-tech span:last-child::after { display: none; }

/* -------------------------------------------------------------
   CERTIFICATIONS
------------------------------------------------------------- */
.certifications-section { background: var(--bg-base); }
.cert-grid { display: grid; grid-template-columns: 1fr; max-width: 800px; margin: 0 auto; }
.cert-card { background: transparent; border: 1px solid var(--border); border-radius: var(--r-md); padding: 48px; display: grid; grid-template-columns: 180px 1fr; gap: 48px; align-items: center; transition: all 0.5s ease; }
.cert-card:hover { border-color: var(--border-med); background: #ffffff; box-shadow: var(--shadow-sm); }
.cert-icon { display: none; }
.cert-info h3 { font-family: var(--font-head); font-size: 1.6rem; font-weight: 500; color: var(--text-1); margin-bottom: 12px; line-height: 1.3; }
.cert-issuer { font-size: 1.1rem; color: var(--text-2); margin-bottom: 24px; font-weight: 400; }
.cert-date { display: inline-block; font-family: var(--font-mono); font-size: 0.85rem; color: var(--accent); letter-spacing: 0.1em; font-weight: 500; }
.cert-card--image { flex-direction: row; }
.cert-image-placeholder { width: 100%; height: 140px; background: rgba(0,0,0,0.02); border: 1px solid var(--border); border-radius: var(--r-sm); display: flex; align-items: center; justify-content: center; overflow: hidden; }
.cert-img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.4s ease; }
.cert-card--image:hover .cert-img { transform: scale(1.05); }

/* -------------------------------------------------------------
   CONTACT & FOOTER
------------------------------------------------------------- */
.contact-section { background: var(--bg-surface); }
.contact-content { display: grid; grid-template-columns: 1fr 1.5fr; gap: 100px; }
.contact-intro p { font-size: 1.2rem; color: var(--text-2); line-height: 1.9; margin-bottom: 56px; font-weight: 400; }
.contact-item { display: flex; align-items: center; gap: 24px; margin-bottom: 32px; }
.contact-item i { font-size: 1rem; color: var(--accent); }
.contact-item span, .contact-item a { font-size: 1.1rem; color: var(--text-1); text-decoration: none; font-weight: 400; transition: color 0.3s ease; }
.contact-item a:hover { color: var(--accent); }

.contact-form { background: transparent; padding: 0; border: none; box-shadow: none; }
.form-group { margin-bottom: 32px; }
.form-group label { display: block; font-family: var(--font-mono); font-size: 0.75rem; color: var(--text-3); margin-bottom: 12px; letter-spacing: 0.15em; text-transform: uppercase; font-weight: 500; }
.form-control { width: 100%; background: transparent; border: none; border-bottom: 1px solid var(--border-med); border-radius: 0; padding: 12px 0; font-family: var(--font-sans); font-size: 1.1rem; font-weight: 400; color: var(--text-1); transition: all 0.4s ease; }
.form-control:focus { outline: none; border-color: var(--accent); background: transparent; box-shadow: none; }
.form-control::placeholder { color: var(--text-muted); }
textarea.form-control { resize: vertical; min-height: 120px; }

.footer { background: var(--bg-base); padding: 80px 0; border-top: 1px solid var(--border); text-align: center; }
.footer-logo { font-family: var(--font-head); font-size: 1.2rem; font-weight: 500; color: var(--text-2); margin-bottom: 32px; letter-spacing: 0.2em; text-transform: uppercase; }
.footer .social-links { justify-content: center; margin-bottom: 40px; }
.footer .social-icon { border-color: transparent; }
.footer-text { color: var(--text-3); font-size: 0.9rem; font-weight: 400; letter-spacing: 0.05em; }
.heart { color: var(--accent); }

/* -------------------------------------------------------------
   PROJECT MODAL (PREMIUM LUXURY)
------------------------------------------------------------- */
.project-modal { position: fixed; inset: 0; z-index: 100000; display: flex; align-items: center; justify-content: center; opacity: 0; visibility: hidden; pointer-events: none; }
.project-modal.active { visibility: visible; pointer-events: auto; }
.modal-backdrop { position: absolute; inset: 0; background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); }
.modal-container { position: relative; width: 100%; height: 100%; max-width: none; max-height: none; background: transparent; border: none; border-radius: 0; overflow-y: auto; overflow-x: hidden; box-shadow: none; display: flex; flex-direction: column; }
.modal-container::-webkit-scrollbar { width: 4px; }
.modal-container::-webkit-scrollbar-thumb { background: var(--border-med); }
.modal-close { position: fixed; top: 40px; right: 40px; width: 60px; height: 60px; background: transparent; border: 1px solid var(--border-med); border-radius: 50%; color: var(--text-1); font-size: 1rem; display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 10; transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1); }
.modal-close:hover { background: var(--bg-surface); border-color: var(--text-1); transform: rotate(90deg); box-shadow: var(--shadow-sm); }
.modal-hero { position: relative; height: 60vh; width: 100%; flex-shrink: 0; background: #eaeaea; }
.modal-hero img { width: 100%; height: 100%; object-fit: cover; opacity: 0.9; }
.modal-hero-overlay { position: absolute; inset: 0; background: linear-gradient(to bottom, transparent 0%, var(--bg-base) 100%); }
.modal-body { padding: 0 10vw 100px; margin-top: -15vh; position: relative; z-index: 2; max-width: 1400px; margin-left: auto; margin-right: auto; width: 100%; }
.modal-header { margin-bottom: 56px; text-align: center; }
#modalTitle { font-family: var(--font-head); font-size: clamp(3rem, 6vw, 5.5rem); font-weight: 400; color: var(--text-1); line-height: 1.1; letter-spacing: -0.02em; margin-bottom: 32px; }
.modal-tech { display: flex; flex-wrap: wrap; justify-content: center; gap: 16px; margin-bottom: 0; padding-bottom: 0; border: none; }
.modal-tech span { font-family: var(--font-mono); font-size: 0.85rem; color: var(--text-2); letter-spacing: 0.1em; text-transform: uppercase; font-weight: 500; }
.modal-tech span::after { content: '-'; margin-left: 16px; color: var(--border-med); }
.modal-tech span:last-child::after { display: none; }
.modal-description { font-size: 1.25rem; line-height: 2; color: var(--text-2); margin-bottom: 80px; font-weight: 400; text-align: center; max-width: 900px; margin-left: auto; margin-right: auto; }
.modal-workflow h3 { font-family: var(--font-head); font-size: 1.8rem; font-weight: 400; color: var(--text-1); margin-bottom: 32px; letter-spacing: -0.01em; text-align: center; }
.modal-workflow h3 i { display: none; }
.workflow-box { background: #ffffff; border: 1px solid var(--border-med); border-radius: var(--r-md); padding: 56px; font-size: 1.1rem; color: var(--text-2); line-height: 2; font-weight: 400; max-width: 900px; margin: 0 auto; text-align: left; box-shadow: var(--shadow-sm); }
.modal-footer { margin-top: 100px; padding-top: 40px; border-top: 1px solid var(--border); text-align: center; font-family: var(--font-mono); font-size: 0.8rem; color: var(--text-3); letter-spacing: 0.2em; text-transform: uppercase; }
.developer-name { color: var(--text-2); font-weight: 500; }

/* -------------------------------------------------------------
   RESPONSIVE DESIGN
------------------------------------------------------------- */
@media (max-width: 1024px) {
  .hero-content, .about-content, .contact-content { grid-template-columns: 1fr; gap: 80px; }
  .hexagon-wrapper, .profile-pic { width: 350px; height: 350px; }
  .skills-grid, .agentic-grid { grid-template-columns: repeat(2, 1fr); }
  .timeline-item, .edu-item { grid-template-columns: 1fr; gap: 16px; padding: 40px 0; }
  .timeline-item:hover, .edu-item:hover { width: 100%; margin: 0; padding-left: 0; padding-right: 0; background: transparent; box-shadow: none; border-bottom-color: var(--border); }
  .cert-card { grid-template-columns: 1fr; gap: 24px; }
  .cert-image-placeholder { height: 200px; }
}
@media (max-width: 768px) {
  .nav-menu { position: absolute; top: 100%; right: 0; width: 100%; background: rgba(255,255,255,0.98); backdrop-filter: blur(20px); flex-direction: column; padding: 40px; border-bottom: 1px solid var(--border); transform: translateY(-150%); transition: transform 0.6s var(--ease-spring); }
  .nav-menu.active { transform: translateY(0); }
  .hamburger { display: flex; }
  .skills-grid, .agentic-grid, .projects-grid { grid-template-columns: 1fr; }
  .hexagon-wrapper, .profile-pic { width: 280px; height: 280px; }
  .section-title { font-size: 2.5rem; }
  .hero-title { font-size: 3rem; }
  .modal-hero { height: 40vh; }
  .modal-body { padding: 0 24px 60px; margin-top: -8vh; }
  .modal-close { top: 20px; right: 20px; width: 48px; height: 48px; }
  .workflow-box { padding: 32px 24px; }
}
"""

with open("D:\\My_projects\\portfolio\\generate_css.py", "w", encoding="utf-8") as f:
    f.write(css_content)

print("Light Luxury CSS generator created!")
