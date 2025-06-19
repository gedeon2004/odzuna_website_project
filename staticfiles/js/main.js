document.addEventListener('DOMContentLoaded', () => {
    console.log('ODZUNA - Initializing advanced interactions');
    
    /**
     * Menu Mobile Avancé avec Animation GSAP
     */
    const menuState = {
        isOpen: false,
        toggle() {
            this.isOpen = !this.isOpen;
            this.animateMenu();
            this.animateHamburger();
        }
    };

    const menuToggle = document.querySelector('.mobile-menu-toggle');
    const navMenu = document.querySelector('.nav-menu');
    const menuBars = document.querySelectorAll('.menu-bar');

    if (menuToggle && navMenu) {
        // Animation GSAP pour le menu
        const menuTimeline = gsap.timeline({ paused: true })
            .fromTo(navMenu, 
                { x: '-100%', opacity: 0 },
                { x: '0%', opacity: 1, duration: 0.4, ease: 'power3.out' }
            )
            .from('.nav-item', {
                y: 20,
                opacity: 0,
                stagger: 0.1,
                duration: 0.3,
                ease: 'back.out'
            }, 0.2);

        menuToggle.addEventListener('click', () => {
            menuState.toggle();
            menuState.isOpen ? menuTimeline.play() : menuTimeline.reverse();
        });

        // Animation des barres du hamburger
        const animateHamburger = () => {
            if (menuState.isOpen) {
                gsap.to(menuBars[0], { rotate: 45, y: 8, duration: 0.3 });
                gsap.to(menuBars[1], { opacity: 0, duration: 0.2 });
                gsap.to(menuBars[2], { rotate: -45, y: -8, duration: 0.3 });
            } else {
                gsap.to(menuBars, { rotate: 0, y: 0, opacity: 1, duration: 0.3 });
            }
        };
    }

    /**
     * Animation des cartes services avec Intersection Observer + GSAP
     */
    const serviceCards = document.querySelectorAll('.service-card');
    
    const cardObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                gsap.to(entry.target, {
                    y: 0,
                    opacity: 1,
                    duration: 0.6,
                    ease: 'back.out(1.2)',
                    stagger: 0.1
                });
                cardObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    serviceCards.forEach(card => {
        gsap.set(card, { y: 50, opacity: 0 });
        cardObserver.observe(card);

        // Effet 3D au hover
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            const angleX = (y - centerY) / 20;
            const angleY = (centerX - x) / 20;

            gsap.to(card, {
                rotateX: angleX,
                rotateY: angleY,
                transformPerspective: 1000,
                ease: 'power1.out',
                duration: 0.5
            });
        });

        card.addEventListener('mouseleave', () => {
            gsap.to(card, {
                rotateX: 0,
                rotateY: 0,
                duration: 0.8,
                ease: 'elastic.out(1, 0.5)'
            });
        });
    });

    /**
     * Effet Parallax Avancé pour la Hero Section
     */
    const heroSection = document.querySelector('.hero-section');
    if (heroSection) {
        const heroContent = heroSection.querySelector('.hero-content');
        
        window.addEventListener('scroll', () => {
            const scrollY = window.scrollY;
            gsap.to(heroContent, {
                y: scrollY * 0.3,
                ease: 'none'
            });
        });
    }

    /**
     * Scroll Progress Indicator
     */
    const progressBar = document.querySelector('.nav-progress-bar');
    if (progressBar) {
        window.addEventListener('scroll', () => {
            const scrollTop = document.documentElement.scrollTop;
            const scrollHeight = document.documentElement.scrollHeight;
            const clientHeight = document.documentElement.clientHeight;
            const progress = (scrollTop / (scrollHeight - clientHeight)) * 100;
            
            gsap.to(progressBar, {
                width: `${progress}%`,
                duration: 0.3,
                ease: 'power1.out'
            });
        });
    }

    /**
     * Système d'onglets avec Transition FLIP
     */
    const tabButtons = document.querySelectorAll('.tab-button');
    const tabContents = document.querySelectorAll('.tab-content');
    let activeTab = document.querySelector('.tab-button.active');

    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            if (button === activeTab) return;

            // Animation FLIP (First, Last, Invert, Play)
            const oldContent = document.querySelector(`#${activeTab.dataset.tab}-tab`);
            const newContent = document.querySelector(`#${button.dataset.tab}-tab`);
            
            // 1. First: Get initial state
            const first = oldContent.getBoundingClientRect();
            
            // 2. Change state
            activeTab.classList.remove('active');
            button.classList.add('active');
            oldContent.classList.remove('active');
            newContent.classList.add('active');
            
            // 3. Last: Get final state
            const last = newContent.getBoundingClientRect();
            
            // 4. Invert: Calculate delta
            const deltaX = first.left - last.left;
            const deltaY = first.top - last.top;
            const deltaWidth = first.width / last.width;
            const deltaHeight = first.height / last.height;
            
            // 5. Play: Animate from inverted to final
            gsap.fromTo(newContent, 
                {
                    x: deltaX,
                    y: deltaY,
                    scaleX: deltaWidth,
                    scaleY: deltaHeight,
                    opacity: 0
                },
                {
                    x: 0,
                    y: 0,
                    scaleX: 1,
                    scaleY: 1,
                    opacity: 1,
                    duration: 0.6,
                    ease: 'power3.out',
                    clearProps: 'all'
                }
            );

            gsap.to(oldContent, {
                opacity: 0,
                duration: 0.3,
                ease: 'power1.in'
            });

            activeTab = button;
        });
    });

    /**
     * Initialisation du Glide.js pour le slider témoignages
     */
    const testimonialsSlider = document.querySelector('.testimonials-slider');
    if (testimonialsSlider) {
        new Glide(testimonialsSlider, {
            type: 'carousel',
            perView: 1,
            autoplay: 4000,
            animationDuration: 800,
            breakpoints: {
                768: { perView: 1 },
                1024: { perView: 2 }
            }
        }).mount();
    }

    /**
     * Effet de vague animée dans le footer
     */
    const wavePath = document.querySelector('.footer-wave path');
    if (wavePath) {
        const waveTimeline = gsap.timeline({ repeat: -1 });
        waveTimeline
            .to(wavePath, {
                attr: { d: "M0,0V46.29c47.79,22.2,103.59,32.17,158,28,70.36-5.37,136.33-33.31,206.8-37.5C438.64,32.43,512.34,53.67,583,72.05c69.27,18,138.3,24.88,209.4,13.08,36.15-6,69.85-17.84,104.45-29.34C989.49,25,1113-14.29,1200,52.47V0Z" },
                duration: 8,
                ease: 'none'
            })
            .to(wavePath, {
                attr: { d: "M0,0V15.81C13,36.92,27.64,56.86,47.69,72.05,99.41,111.27,165,111,224.58,91.58c31.15-10.15,60.09-26.07,89.67-39.8,40.92-19,84.73-46,130.83-49.67,36.26-2.85,70.9,9.42,98.6,31.56,31.77,25.39,62.32,62,103.63,73,40.44,10.79,81.35-6.69,119.13-24.28s75.16-39,116.92-43.05c59.73-5.85,113.28,22.88,168.9,38.84,30.2,8.66,59,6.17,87.09-7.5,22.43-10.89,48-26.93,60.65-49.24V0Z" },
                duration: 8,
                ease: 'none'
            });
    }

    /**
     * Gestion des entrées utilisateur avancée
     */
    document.addEventListener('keydown', (e) => {
        // Fermer le menu avec ESC
        if (e.key === 'Escape' && menuState.isOpen) {
            menuState.toggle();
            menuTimeline.reverse();
        }
    });

    // Optimisation des événements
    const debouncedResize = debounce(() => {
        console.log('Window resized - recalculating animations');
    }, 200);

    window.addEventListener('resize', debouncedResize);

    // Fonction debounce helper
    function debounce(func, wait) {
        let timeout;
        return function() {
            const context = this, args = arguments;
            clearTimeout(timeout);
            timeout = setTimeout(() => func.apply(context, args), wait);
        };
    }
});

// Web Components pour les éléments réutilisables
class OdzunaCard extends HTMLElement {
    constructor() {
        super();
        // Implémentation du shadow DOM pour encapsulation
    }
}

customElements.define('odzuna-card', OdzunaCard);