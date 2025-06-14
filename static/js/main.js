document.addEventListener('DOMContentLoaded', function() {
    // Branch toggle functionality
    const branchButtons = document.querySelectorAll('.branch-toggle button');
    const serviceCards = document.querySelectorAll('.service-card');
    
    branchButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Update active button
            branchButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            
            const selectedBranch = button.dataset.branch;
            
            // Filter service cards
            serviceCards.forEach(card => {
                if (selectedBranch === 'all' || card.dataset.branch === selectedBranch) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
    
    // Animate service cards on scroll
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.1 });
    
    serviceCards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'all 0.5s ease';
        observer.observe(card);
    });
});

// Mobile menu toggle
document.querySelector('.mobile-menu-toggle').addEventListener('click', function() {
    document.querySelector('.nav-links').classList.toggle('active');
});

// Close dropdowns when clicking outside
document.addEventListener('click', function(event) {
    if (!event.target.matches('.dropdown *')) {
        const dropdowns = document.querySelectorAll('.dropdown-menu');
        dropdowns.forEach(function(dropdown) {
            dropdown.style.display = 'none';
        });
    }
});

// Handle dropdown click
document.querySelectorAll('.dropdown > a').forEach(function(link) {
    link.addEventListener('click', function(e) {
        if (window.innerWidth <= 992) {
            e.preventDefault();
            const dropdown = this.nextElementSibling;
            dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
        }
    });
});