// Wait until the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    form.addEventListener("submit", function (e) {
        e.preventDefault(); // Prevent actual form submission

        const name = document.getElementById("name").value.trim();
        const email = document.getElementById("email").value.trim();
        const pet = document.getElementById("pet").value.trim();
        const message = document.getElementById("message").value.trim();

        // Basic validation
        if (!name || !email || !pet || !message) {
            alert("Please fill in all the fields before submitting.");
            return;
        }

        // Show confirmation message
        alert(`Thank you, ${name}! Your request to adopt ${pet} has been received. We will contact you shortly.`);

        // Optionally, reset form
        form.reset();
    });
});
