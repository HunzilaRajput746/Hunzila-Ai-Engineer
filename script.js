/* ══════════════════════════════════════════════════════════════
   HUNZILA NISAR — PREMIUM PORTFOLIO SCRIPTS
   GSAP + ScrollTrigger + Custom Interactions
   ══════════════════════════════════════════════════════════════ */

'use strict';

// ── Mark JS as loaded immediately (so reveal animations work) ──
document.body.classList.add('js-ready');

// ── Register GSAP Plugins ──
gsap.registerPlugin(ScrollTrigger, TextPlugin);

/* ═══════════════════════════════════
   PRELOADER (TERMINAL AI STYLE)
═══════════════════════════════════ */
document.body.style.overflow = 'hidden';

function hidePreloader() {
  const preloader = document.getElementById('preloader');
  if (!preloader) return;
  preloader.classList.add('hidden');
  document.body.style.overflow = '';
  setTimeout(initHeroAnimations, 100);
  setTimeout(checkAllReveals, 300);
}

const progressBar = document.querySelector('.loading-progress');
const progressText = document.querySelector('.loading-text');

if (progressBar && progressText) {
  let progress = 0;
  
  // Phase 1: Booting
  setTimeout(() => { progressText.textContent = "BOOTING AI KERNEL..."; }, 500);
  
  // Phase 2: Loading Models
  setTimeout(() => { progressText.textContent = "LOADING NEURAL WEIGHTS..."; }, 1500);
  
  // Phase 3: Ready
  setTimeout(() => { progressText.textContent = "AGENTIC SYSTEMS ONLINE."; }, 2800);

  const loaderInterval = setInterval(() => {
    progress += Math.random() * 8;
    if (progress > 100) {
      progress = 100;
      clearInterval(loaderInterval);
      setTimeout(hidePreloader, 600); // Hide after reaching 100%
    }
    progressBar.style.width = progress + '%';
  }, 100);
} else {
  // Fallback if elements are missing
  window.addEventListener('load', () => setTimeout(hidePreloader, 2500));
  setTimeout(hidePreloader, 4000);
}

/* Custom cursor removed */
/* ═══════════════════════════════════
   NAVBAR
═══════════════════════════════════ */
const navbar = document.getElementById('navbar');
const hamburger = document.getElementById('hamburger');
const navMenu = document.getElementById('navMenu');

window.addEventListener('scroll', () => {
  if (navbar) {
    navbar.classList.toggle('scrolled', window.scrollY > 80);
  }
  updateActiveNav();
});

if (hamburger && navMenu) {
  hamburger.addEventListener('click', () => {
    navMenu.classList.toggle('active');
  });
}

document.querySelectorAll('.nav-link').forEach(link => {
  link.addEventListener('click', () => {
    if (navMenu) navMenu.classList.remove('active');
  });
});

function updateActiveNav() {
  const sections = document.querySelectorAll('section[id]');
  const scrollPos = window.scrollY + 120;
  sections.forEach(section => {
    const top = section.offsetTop;
    const height = section.offsetHeight;
    const id = section.getAttribute('id');
    const link = document.querySelector(`.nav-link[href="#${id}"]`);
    if (link) {
      if (scrollPos >= top && scrollPos < top + height) {
        document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
        link.classList.add('active');
      }
    }
  });
}

/* ═══════════════════════════════════
   PARTICLES.JS
═══════════════════════════════════ */
if (typeof particlesJS !== 'undefined' && document.getElementById('particles-js')) {
  particlesJS('particles-js', {
    particles: {
      number: { value: 55, density: { enable: true, value_area: 900 } },
      color: { value: ['#8b5cf6', '#06b6d4', '#10b981'] },
      shape: { type: 'circle' },
      opacity: { value: 0.4, random: true, anim: { enable: true, speed: 1, opacity_min: 0.1 } },
      size: { value: 2.5, random: true },
      line_linked: { enable: true, distance: 140, color: '#8b5cf6', opacity: 0.12, width: 1 },
      move: { enable: true, speed: 1.2, direction: 'none', random: true, out_mode: 'out' }
    },
    interactivity: {
      detect_on: 'canvas',
      events: { onhover: { enable: true, mode: 'grab' }, onclick: { enable: true, mode: 'push' }, resize: true },
      modes: { grab: { distance: 180, line_linked: { opacity: 0.4 } }, push: { particles_nb: 2 } }
    },
    retina_detect: true
  });
}

/* ═══════════════════════════════════
   TYPING ANIMATION
═══════════════════════════════════ */
const typingEl = document.querySelector('.typing-text');
const phrases = ['AI Engineer', 'Agentic AI Expert'];

let phraseIdx = 0, charIdx = 0, isDeleting = false;

function typeLoop() {
  if (!typingEl) return;
  const current = phrases[phraseIdx];
  if (!isDeleting) {
    typingEl.textContent = current.slice(0, charIdx + 1);
    charIdx++;
    if (charIdx === current.length) {
      isDeleting = true;
      setTimeout(typeLoop, 2500);
      return;
    }
  } else {
    typingEl.textContent = current.slice(0, charIdx - 1);
    charIdx--;
    if (charIdx === 0) {
      isDeleting = false;
      phraseIdx = (phraseIdx + 1) % phrases.length;
    }
  }
  setTimeout(typeLoop, isDeleting ? 45 : 120);
}

/* ═══════════════════════════════════
   HERO ANIMATIONS
═══════════════════════════════════ */
function initHeroAnimations() {
  setTimeout(typeLoop, 300);

  try {
    const tl = gsap.timeline({ defaults: { ease: 'power3.out' } });
    tl.from('.hero-badge', { y: 30, opacity: 0, duration: 0.6 })
      .from('.hero-title .text-line', { y: 60, opacity: 0, duration: 0.8, stagger: 0.15 }, '-=0.3')
      .from('.typing-container', { y: 20, opacity: 0, duration: 0.5 }, '-=0.3')
      .from('.hero-description', { y: 20, opacity: 0, duration: 0.5 }, '-=0.2')
      .from('.hero-cta .btn', { y: 20, opacity: 0, duration: 0.5, stagger: 0.12 }, '-=0.2')
      .from('.social-links .social-icon', { y: 20, opacity: 0, duration: 0.4, stagger: 0.08 }, '-=0.2')
      .from('.hexagon-wrapper', { scale: 0.7, opacity: 0, duration: 0.9, ease: 'back.out(1.5)' }, '-=0.8')
      .from('.float-icon', { scale: 0, opacity: 0, duration: 0.5, stagger: 0.15, ease: 'back.out(2)' }, '-=0.4')
      .from('.scroll-indicator', { y: 20, opacity: 0, duration: 0.5 }, '-=0.2');

    // Floating hero image
    gsap.to('.hexagon-wrapper', { y: -15, duration: 3, yoyo: true, repeat: -1, ease: 'sine.inOut' });
  } catch (e) {
    console.warn('GSAP hero animation error:', e);
  }
}

/* ═══════════════════════════════════
   SCROLL REVEAL — IntersectionObserver
═══════════════════════════════════ */
function checkAllReveals() {
  // Force-reveal elements already in viewport
  document.querySelectorAll('.reveal:not(.visible)').forEach(el => {
    const rect = el.getBoundingClientRect();
    if (rect.top < window.innerHeight + 100) {
      el.classList.add('visible');
    }
  });
}

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, {
  threshold: 0.05,          // Very low – triggers when just 5% visible
  rootMargin: '0px 0px 0px 0px'  // No margin cutoff
});

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

// Also re-check on scroll (belt-and-suspenders approach)
window.addEventListener('scroll', () => {
  document.querySelectorAll('.reveal:not(.visible)').forEach(el => {
    const rect = el.getBoundingClientRect();
    if (rect.top < window.innerHeight - 20) {
      el.classList.add('visible');
    }
  });
}, { passive: true });

/* ═══════════════════════════════════
   SKILL BAR ANIMATIONS
═══════════════════════════════════ */
const skillBars = document.querySelectorAll('.skill-progress');
const skillObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const bar = entry.target;
      const progress = bar.getAttribute('data-progress');
      setTimeout(() => { bar.style.width = progress + '%'; }, 200);
      skillObserver.unobserve(bar);
    }
  });
}, { threshold: 0.1 });

skillBars.forEach(bar => skillObserver.observe(bar));

/* ═══════════════════════════════════
   COUNTER ANIMATION
═══════════════════════════════════ */
const counters = document.querySelectorAll('.stat-number');
const counterObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const el = entry.target;
      const target = parseInt(el.getAttribute('data-target'));
      let current = 0;
      const increment = target / 60;
      const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
          el.textContent = target;
          clearInterval(timer);
        } else {
          el.textContent = Math.floor(current);
        }
      }, 25);
      counterObserver.unobserve(el);
    }
  });
}, { threshold: 0.5 });

counters.forEach(c => counterObserver.observe(c));

/* -------------------------------------------------------------
   GSAP SCROLL ANIMATIONS (Framer Motion Feel)
------------------------------------------------------------- */
try {
  // Fix animation conflict: remove .reveal from elements managed by GSAP
  document.querySelectorAll('.agentic-card, .timeline-item, .cert-card, .project-card, .passion-card').forEach(el => {
      el.classList.remove('reveal');
      el.style.opacity = '1';
      el.style.transform = 'none';
      el.style.transition = 'none';
  });

  // Agentic cards spring pop-in (Framer Motion feel)
  gsap.utils.toArray('.agentic-card').forEach((card, i) => {
    gsap.from(card, {
      scrollTrigger: { trigger: card, start: 'top 92%' },
      scale: 0.8, opacity: 0, duration: 1.2,
      delay: i * 0.1, ease: 'elastic.out(1, 0.75)'
    });
  });

  // Passion cards spring pop-in
  gsap.utils.toArray('.passion-card').forEach((card, i) => {
    gsap.from(card, {
      scrollTrigger: { trigger: card, start: 'top 92%' },
      scale: 0.8, opacity: 0, duration: 1.2,
      delay: (i % 3) * 0.1, ease: 'elastic.out(1, 0.75)'
    });
  });

  // Timeline items spring in alternating
  gsap.utils.toArray('.timeline-item').forEach((item, i) => {
    gsap.from(item, {
      scrollTrigger: { trigger: item, start: 'top 88%' },
      x: i % 2 === 0 ? -60 : 60, opacity: 0,
      duration: 1.2, ease: 'elastic.out(1, 0.75)'
    });
  });

    // Cert cards — premium stagger flip-in (Framer Motion card reveal)
    gsap.utils.toArray('.cert-card').forEach((card, i) => {
      gsap.fromTo(card,
        { opacity: 0, y: 50, rotateY: 15, scale: 0.88 },
        {
          scrollTrigger: { trigger: card, start: 'top 90%', once: true },
          opacity: 1, y: 0, rotateY: 0, scale: 1,
          duration: 0.9,
          delay: (i % 4) * 0.12,
          ease: 'cubic-bezier(0.22, 1, 0.36, 1)',
          clearProps: 'transform'
        }
      );
    });
  
  // Projects spring reveal
  gsap.utils.toArray('.project-card').forEach((card, i) => {
    gsap.from(card, {
      scrollTrigger: { trigger: card, start: 'top 90%' },
      y: 60, opacity: 0, duration: 1.2,
      delay: (i % 3) * 0.1, ease: 'elastic.out(1, 0.75)'
    });
  });

} catch (e) {
  console.warn('GSAP ScrollTrigger error:', e);
}

/* ═══════════════════════════════════
   3D CARD TILT
═══════════════════════════════════ */
document.querySelectorAll('.project-card').forEach(card => {
  card.addEventListener('mousemove', (e) => {
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const cx = rect.width / 2;
    const cy = rect.height / 2;
    const rotX = ((y - cy) / cy) * -5;
    const rotY = ((x - cx) / cx) * 5;
    card.style.transform = `perspective(1000px) rotateX(${rotX}deg) rotateY(${rotY}deg) translateY(-8px)`;
    card.style.transition = 'transform 0.1s ease';
  });
  card.addEventListener('mouseleave', () => {
    card.style.transform = '';
    card.style.transition = 'transform 0.5s cubic-bezier(0.22, 1, 0.36, 1)';
  });
});

/* ═══════════════════════════════════
   MAGNETIC BUTTONS
═══════════════════════════════════ */
document.querySelectorAll('.btn').forEach(btn => {
  btn.addEventListener('mousemove', (e) => {
    const rect = btn.getBoundingClientRect();
    const x = (e.clientX - rect.left - rect.width / 2) * 0.2;
    const y = (e.clientY - rect.top - rect.height / 2) * 0.2;
    btn.style.transform = `translate(${x}px, ${y}px)`;
    btn.style.transition = 'transform 0.1s ease';
  });
  btn.addEventListener('mouseleave', () => {
    btn.style.transform = '';
    btn.style.transition = 'transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1)';
  });
});

/* ═══════════════════════════════════
   SCROLL PARALLAX (Hero fade out)
═══════════════════════════════════ */
window.addEventListener('scroll', () => {
  const scrolled = window.scrollY;
  const heroContent = document.querySelector('.hero-content');
  if (heroContent && scrolled < window.innerHeight) {
    const opacity = 1 - (scrolled / (window.innerHeight * 0.75));
    heroContent.style.opacity = Math.max(0, opacity);
    heroContent.style.transform = `translateY(${scrolled * 0.12}px)`;
  }
}, { passive: true });

/* ═══════════════════════════════════
   SMOOTH SCROLL
═══════════════════════════════════ */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', (e) => {
    e.preventDefault();
    const targetId = anchor.getAttribute('href');
    const target = document.querySelector(targetId);
    if (target) {
      const top = target.getBoundingClientRect().top + window.scrollY - 80;
      window.scrollTo({ top, behavior: 'smooth' });
    }
  });
});

/* ═══════════════════════════════════
   CONTACT FORM
═══════════════════════════════════ */
const form = document.getElementById('contactForm');
if (form) {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const btn = form.querySelector('button[type="submit"]');
    const original = btn.innerHTML;
    btn.innerHTML = '<span>Sending...</span><i class="fas fa-spinner fa-spin"></i>';
    btn.disabled = true;
    setTimeout(() => {
      btn.innerHTML = '<span>Sent! ✓</span>';
      btn.style.background = 'linear-gradient(135deg, #10b981, #059669)';
      form.reset();
      setTimeout(() => {
        btn.innerHTML = original;
        btn.style.background = '';
        btn.disabled = false;
      }, 3000);
    }, 1500);
  });
}

console.log('%c🤖 Hunzila Nisar — AI Engineer & Agentic AI Developer', 'color: #8b5cf6; font-size:14px; font-weight:bold;');
console.log('%cPortfolio loaded successfully ✓', 'color: #10b981; font-size:12px;');

// Click listener for project pages
const projectCards = document.querySelectorAll('.project-card');
projectCards.forEach(card => {
    card.style.cursor = 'pointer';
    card.addEventListener('click', (e) => {
        // Prevent opening if clicking on github/link icons
        if(e.target.closest('.project-link')) return;
        const id = card.getAttribute('data-project-id');
        if(id) {
            window.location.href = 'project.html?id=' + id;
        }
    });
});
