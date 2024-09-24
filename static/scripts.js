document.addEventListener('DOMContentLoaded', function () {
    const flashMessages = document.querySelectorAll('.flash-message');
    
    flashMessages.forEach(function (message) {
        setTimeout(function () {
            message.classList.add('fade-out');
        }, 3000); // Time before fade-out starts (3 seconds)

        setTimeout(function () {
            message.remove();
        }, 3500); // Slightly longer than the fade-out time
    });
});
