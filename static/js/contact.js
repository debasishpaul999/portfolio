// Simple Contact Form Handler
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    
    if (contactForm) {
        console.log('Contact form loaded');
        
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            console.log('Form submitted');
            
            const submitBtn = contactForm.querySelector('button[type="submit"]');
            const originalText = submitBtn.textContent;
            
            // Get form data
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const message = document.getElementById('message').value.trim();
            
            // Basic validation
            if (!name || !email || !message) {
                showMessage('Please fill in all fields.', 'error');
                return;
            }
            
            // Simple email validation
            if (!email.includes('@') || !email.includes('.')) {
                showMessage('Please enter a valid email address.', 'error');
                return;
            }
            
            // Show loading state
            submitBtn.disabled = true;
            submitBtn.textContent = 'Sending...';
            submitBtn.style.opacity = '0.7';
            
            // Simulate sending (opens email client)
            setTimeout(() => {
                sendEmail(name, email, message);
                
                // Show success message
                showMessage('Thank you! Your message has been sent successfully.', 'success');
                
                // Reset form
                contactForm.reset();
                
                // Reset button
                submitBtn.disabled = false;
                submitBtn.textContent = originalText;
                submitBtn.style.opacity = '1';
                
            }, 1500); // Simulate delay
        });
    }
    
    function sendEmail(name, email, message) {
        // Get the portfolio owner's email from the page
        const profileEmailElement = document.querySelector('a[href^="mailto:"]');
        let toEmail = 'your-email@example.com'; // Default fallback
        
        if (profileEmailElement) {
            toEmail = profileEmailElement.href.replace('mailto:', '');
        }
        
        // Create email content
        const subject = `Portfolio Message from ${name}`;
        const body = `
Name: ${name}
Email: ${email}

Message:
${message}

---
This message was sent from your portfolio website.
        `.trim();
        
        // Create mailto link
        const mailtoLink = `mailto:${toEmail}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
        
        // Open email client in new tab
        window.open(mailtoLink, '_blank');
        
        console.log('Email client opened with pre-filled message');
    }
    
    function showMessage(text, type) {
        // Remove existing messages
        const existingMessages = document.querySelectorAll('.form-message');
        existingMessages.forEach(msg => msg.remove());
        
        // Create message element
        const messageDiv = document.createElement('div');
        messageDiv.className = 'form-message';
        messageDiv.textContent = text;
        
        // Style based on type
        if (type === 'success') {
            messageDiv.style.cssText = `
                background: #d1fae5;
                color: #065f46;
                border: 2px solid #10b981;
                padding: 1rem;
                border-radius: 8px;
                margin: 1rem 0;
                text-align: center;
                font-weight: 600;
            `;
        } else {
            messageDiv.style.cssText = `
                background: #fee2e2;
                color: #991b1b;
                border: 2px solid #ef4444;
                padding: 1rem;
                border-radius: 8px;
                margin: 1rem 0;
                text-align: center;
                font-weight: 600;
            `;
        }
        
        // Add to form
        contactForm.appendChild(messageDiv);
        
        // Remove after 5 seconds
        setTimeout(() => {
            messageDiv.remove();
        }, 5000);
    }
    
    // Add input validation styling
    const inputs = document.querySelectorAll('#contactForm input, #contactForm textarea');
    inputs.forEach(input => {
        input.addEventListener('input', function() {
            this.style.borderColor = '';
        });
    });
});