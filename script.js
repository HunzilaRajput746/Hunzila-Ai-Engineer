/* ══════════════════════════════════════════════════════════════
   HUNZILA NISAR — PORTFOLIO INTERACTIONS & FORM BACKEND
   ══════════════════════════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', () => {

    // ── Mobile Navigation Toggle ──
    const mobileToggle = document.getElementById('mobileToggle');
    const navMenu = document.getElementById('navMenu');

    if (mobileToggle && navMenu) {
        mobileToggle.addEventListener('click', () => {
            navMenu.classList.toggle('open');
            const icon = mobileToggle.querySelector('i');
            if (icon) {
                if (navMenu.classList.contains('open')) {
                    icon.classList.remove('fa-bars');
                    icon.classList.add('fa-times');
                } else {
                    icon.classList.remove('fa-times');
                    icon.classList.add('fa-bars');
                }
            }
        });

        // Close menu when clicking nav links
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('open');
                const icon = mobileToggle.querySelector('i');
                if (icon) {
                    icon.classList.remove('fa-times');
                    icon.classList.add('fa-bars');
                }
            });
        });
    }

    // ── Active Navigation on Scroll ──
    const sections = document.querySelectorAll('section[id], header[id]');
    const navLinks = document.querySelectorAll('.nav-link');

    window.addEventListener('scroll', () => {
        let current = '';
        const scrollPosition = window.scrollY + 140;

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    }, { passive: true });

    // ── Typing Effect in Hero ──
    const typingElement = document.getElementById('typingRole');
    if (typingElement) {
        const roles = [
            'AI & Backend Engineer',
            'Agentic AI Developer',
            'Production CRM Architect',
            'Machine Learning Specialist',
            'n8n Automation Architect'
        ];
        let roleIndex = 0;
        let charIndex = 0;
        let isDeleting = false;
        let typingDelay = 100;

        function typeRole() {
            const currentRole = roles[roleIndex];
            
            if (isDeleting) {
                typingElement.textContent = currentRole.substring(0, charIndex - 1);
                charIndex--;
                typingDelay = 50;
            } else {
                typingElement.textContent = currentRole.substring(0, charIndex + 1);
                charIndex++;
                typingDelay = 110;
            }

            if (!isDeleting && charIndex === currentRole.length) {
                typingDelay = 2000;
                isDeleting = true;
            } else if (isDeleting && charIndex === 0) {
                isDeleting = false;
                roleIndex = (roleIndex + 1) % roles.length;
                typingDelay = 500;
            }

            setTimeout(typeRole, typingDelay);
        }

        setTimeout(typeRole, 600);
    }

    // ── Working Contact Form Backend (formsubmit.co) ──
    const contactForm = document.getElementById('portfolioContactForm');
    const submitBtn = document.getElementById('contactSubmitBtn');
    const alertSuccess = document.getElementById('formAlertSuccess');
    const alertError = document.getElementById('formAlertError');

    if (contactForm && submitBtn) {
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            // Reset alerts
            if (alertSuccess) alertSuccess.style.display = 'none';
            if (alertError) alertError.style.display = 'none';

            // Gather inputs
            const name = document.getElementById('formName')?.value || '';
            const email = document.getElementById('formEmail')?.value || '';
            const subject = document.getElementById('formSubject')?.value || 'New Portfolio Contact';
            const message = document.getElementById('formMessage')?.value || '';

            const originalBtnHtml = submitBtn.innerHTML;
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> <span>Sending Message...</span>';

            try {
                const response = await fetch('https://formsubmit.co/ajax/hunzilanisar123@gmail.com', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json'
                    },
                    body: JSON.stringify({
                        name: name,
                        email: email,
                        _subject: `New Portfolio Message from ${name}: ${subject}`,
                        subject: subject,
                        message: message,
                        _template: 'table',
                        _captcha: 'false'
                    })
                });

                if (response.ok) {
                    if (alertSuccess) {
                        alertSuccess.style.display = 'flex';
                    }
                    submitBtn.innerHTML = '<i class="fas fa-check"></i> <span>Message Sent! ✓</span>';
                    submitBtn.style.background = 'linear-gradient(135deg, #10b981, #059669)';
                    contactForm.reset();

                    setTimeout(() => {
                        submitBtn.innerHTML = originalBtnHtml;
                        submitBtn.style.background = '';
                        submitBtn.disabled = false;
                    }, 4000);
                } else {
                    throw new Error('Form submission failed.');
                }
            } catch (err) {
                console.error('Contact Form Error:', err);
                if (alertError) {
                    alertError.style.display = 'flex';
                }
                submitBtn.innerHTML = originalBtnHtml;
                submitBtn.disabled = false;
            }
        });
    }

    // ── Modal Lightbox for Project Screenshots ──
    const modal = document.getElementById('imageModal');
    const modalImg = document.getElementById('modalImage');
    const modalClose = document.getElementById('modalClose');

    if (modal && modalImg && modalClose) {
        document.querySelectorAll('.project-visual-inner').forEach(container => {
            container.addEventListener('click', (e) => {
                // Ignore if clicked on an actual link
                if (e.target.closest('a')) return;
                const img = container.querySelector('img');
                if (img) {
                    modalImg.src = img.src;
                    modalImg.alt = img.alt || 'Project Preview';
                    modal.classList.add('active');
                }
            });
        });

        modalClose.addEventListener('click', () => {
            modal.classList.remove('active');
        });

        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.classList.remove('active');
            }
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && modal.classList.contains('active')) {
                modal.classList.remove('active');
            }
        });
    }

    console.log('%c🚀 Hunzila Nisar — AI Engineer Portfolio Online', 'color: #8b5cf6; font-size:14px; font-weight:bold;');
});
