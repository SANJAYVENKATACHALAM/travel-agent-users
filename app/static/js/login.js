const form = document.getElementById("loginForm");
const message = document.getElementById("message");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    message.innerText = "";

    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;

    try {

        const response = await fetch("/auth/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email,
                password
            })
        });

        const data = await response.json();

        if (!response.ok) {
            message.innerText = data.detail || "Login failed";
            return;
        }

        // Store JWT Token
        localStorage.setItem(
            "access_token",
            data.access_token
        );

        // Redirect
        window.location.href = "/dashboard";

    } catch (error) {

        console.error(error);

        message.innerText = "Unable to connect to server.";

    }
});