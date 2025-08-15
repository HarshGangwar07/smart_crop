// --- Canvas Particle Animation ---
const canvas = document.getElementById('particle-canvas');
const ctx = canvas.getContext('2d');

let particles = [];
const numParticles = 100;

// Set canvas size and handle window resizing
function resizeCanvas() {
    const parent = canvas.parentElement;
    canvas.width = parent.clientWidth;
    canvas.height = parent.clientHeight;
}

window.addEventListener('resize', resizeCanvas);

// Particle class
class Particle {
    constructor(x, y, radius, color, velocity) {
        this.x = x;
        this.y = y;
        this.radius = radius;
        this.color = color;
        this.velocity = velocity;
    }

    draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false);
        ctx.fillStyle = this.color;
        ctx.fill();
        ctx.closePath();
    }

    update() {
        this.draw();
        this.x += this.velocity.x;
        this.y += this.velocity.y;

        // Wall collision
        if (this.x + this.radius > canvas.width || this.x - this.radius < 0) {
            this.velocity.x = -this.velocity.x;
        }
        if (this.y + this.radius > canvas.height || this.y - this.radius < 0) {
            this.velocity.y = -this.velocity.y;
        }
    }
}

// Initialize particles
function init() {
    particles = [];
    for (let i = 0; i < numParticles; i++) {
        const radius = Math.random() * 2 + 1;
        const x = Math.random() * (canvas.width - radius * 2) + radius;
        const y = Math.random() * (canvas.height - radius * 2) + radius;
        const color = 'rgba(255, 255, 255, 0.8)';
        const velocity = {
            x: (Math.random() - 0.5) * 0.5,
            y: (Math.random() - 0.5) * 0.5
        };
        particles.push(new Particle(x, y, radius, color, velocity));
    }
}

// Connect particles with lines
function connectParticles() {
    let opacityValue = 1;
    for (let a = 0; a < particles.length; a++) {
        for (let b = a; b < particles.length; b++) {
            const distance = Math.sqrt(
                Math.pow(particles[a].x - particles[b].x, 2) +
                Math.pow(particles[a].y - particles[b].y, 2)
            );

            if (distance < 100) {
                opacityValue = 1 - (distance / 100);
                const isBlue = a % 3 === 0;
                const isGreen = b % 5 === 0;
                let lineColor = 'rgba(255, 255, 255, ' + opacityValue + ')';
                if (isBlue) lineColor = 'rgba(59, 130, 246, ' + opacityValue + ')'; // blue-500
                if (isGreen) lineColor = 'rgba(16, 185, 129, ' + opacityValue + ')'; // green-500

                ctx.strokeStyle = lineColor;
                ctx.lineWidth = 1;
                ctx.beginPath();
                ctx.moveTo(particles[a].x, particles[a].y);
                ctx.lineTo(particles[b].x, particles[b].y);
                ctx.stroke();
            }
        }
    }
}

// Animation loop
function animate() {
    requestAnimationFrame(animate);
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    particles.forEach(particle => {
        particle.update();
    });
    connectParticles();
}

// Initial setup
resizeCanvas();
init();
animate();