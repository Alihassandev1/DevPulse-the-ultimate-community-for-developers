let cropData = {
    file: null,
    img: null,
    zoom: 100,
    offsetX: 0,
    offsetY: 0,
    isDragging: false
};

// Open crop modal
function openCropModal(event) {
    const file = event.target.files[0];
    if (!file) return;

    cropData.file = file;

    const reader = new FileReader();
    reader.onload = function (e) {
        const img = new Image();
        img.onload = function () {
            cropData.img = img;
            document.getElementById('imageToCrop').src = e.target.result;
            document.getElementById('imageToCrop').style.transform = 'scale(1)';
            cropData.zoom = 100;
            cropData.offsetX = 0;
            cropData.offsetY = 0;
            updatePreview();

            const cropModal = new bootstrap.Modal(document.getElementById('cropModal'));
            cropModal.show();
        };
        img.src = e.target.result;
    };
    reader.readAsDataURL(file);

    // Add drag functionality
    const imageToCrop = document.getElementById('imageToCrop');
    imageToCrop.addEventListener('mousedown', startDrag);
    document.addEventListener('mousemove', drag);
    document.addEventListener('mouseup', endDrag);
}

// Zoom update
function updateZoom(value) {
    cropData.zoom = value;
    document.getElementById('zoomValue').textContent = value;
    const imageToCrop = document.getElementById('imageToCrop');
    imageToCrop.style.transform = `scale(${value / 100})`;
    imageToCrop.style.transformOrigin = 'center center';
    updatePreview();
}

// Drag functionality
function startDrag(e) {
    cropData.isDragging = true;
    cropData.startX = e.clientX;
    cropData.startY = e.clientY;
}

function drag(e) {
    if (!cropData.isDragging) return;

    const dx = e.clientX - cropData.startX;
    const dy = e.clientY - cropData.startY;

    cropData.offsetX += dx;
    cropData.offsetY += dy;

    cropData.startX = e.clientX;
    cropData.startY = e.clientY;

    updatePreview();
}

function endDrag() {
    cropData.isDragging = false;
}

// Update preview
function updatePreview() {
    const canvas = document.getElementById('previewCanvas');
    const ctx = canvas.getContext('2d');

    ctx.fillStyle = 'rgba(0, 0, 0, 0.5)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    if (!cropData.img) return;

    const size = 150;
    const centerX = size / 2;
    const centerY = size / 2;

    ctx.save();
    ctx.beginPath();
    ctx.arc(centerX, centerY, centerX - 5, 0, Math.PI * 2);
    ctx.clip();

    const imgScale = cropData.zoom / 100;
    const scaledWidth = cropData.img.width * imgScale;
    const scaledHeight = cropData.img.height * imgScale;

    const x = (size - scaledWidth) / 2 + cropData.offsetX;
    const y = (size - scaledHeight) / 2 + cropData.offsetY;

    ctx.drawImage(cropData.img, x, y, scaledWidth, scaledHeight);
    ctx.restore();
}

// Save and upload cropped image
function saveCroppedImage() {
    const canvas = document.getElementById('previewCanvas');

    canvas.toBlob(function (blob) {
        const form = new FormData();
        form.append('profile_image', blob, 'profile.png');

        // Get CSRF token
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        fetch('{% url "post:profile" profile.username %}', {
            method: 'POST',
            body: form,
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': csrfToken,
            }
        })
            .then(response => {
                console.log('Response status:', response.status);
                if (!response.ok) {
                    throw new Error('HTTP error, status: ' + response.status);
                }
                return response.json();
            })
            .then(data => {
                console.log('Response data:', data);
                if (data.status === 'success') {
                    // Update display with new image
                    const reader = new FileReader();
                    reader.onload = function (e) {
                        const display = document.getElementById('profileImageDisplay');
                        if (display.tagName === 'IMG') {
                            display.src = data.image_url + '?t=' + Date.now();
                        } else {
                            const img = document.createElement('img');
                            img.src = data.image_url + '?t=' + Date.now();
                            img.className = 'profile-avatar';
                            img.id = 'profileImageDisplay';
                            img.alt = 'Profile Picture';
                            display.parentNode.replaceChild(img, display);
                        }
                    };
                    reader.readAsDataURL(blob);

                    bootstrap.Modal.getInstance(document.getElementById('cropModal')).hide();
                    alert('Profile photo updated successfully!');
                } else {
                    alert('Error: ' + (data.message || 'Unknown error'));
                }
            })
            .catch(error => {
                console.error('Error uploading image:', error);
                alert('Upload failed: ' + error.message);
            });
    }, 'image/png');
}