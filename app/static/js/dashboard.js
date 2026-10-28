const token = localStorage.getItem("access_token");

if (!token) {
    window.location.href = "/login";
}

const form = document.getElementById("aiTripForm");
const loading = document.getElementById("loading");
const itinerary = document.getElementById("itinerary");

document
    .getElementById("logoutBtn")
    .addEventListener("click", () => {

        localStorage.removeItem("access_token");

        window.location.href = "/login";

    });

form.addEventListener("submit", async (e) => {

    e.preventDefault();

    loading.innerHTML =
        "<i class='fa-solid fa-spinner fa-spin'></i> Generating your AI itinerary...";

    itinerary.innerHTML = "";

    const destination =
        document.getElementById("destination").value.trim();

    const days =
        parseInt(document.getElementById("days").value);

    const budget =
        parseFloat(document.getElementById("budget").value);

    const travelers =
        parseInt(document.getElementById("travelers").value);

    const interests =
        document.getElementById("interests").value.trim();

    try {

        const response = await fetch("/ai/generate", {

            method: "POST",

            headers: {

                "Content-Type": "application/json",

                "Authorization": `Bearer ${token}`

            },

            body: JSON.stringify({

                destination,
                days,
                budget,
                travelers,
                interests

            })

        });

        const data = await response.json();

        loading.innerHTML = "";

        if (!response.ok) {

            itinerary.innerHTML = `

                <div class="empty">

                    <i class="fa-solid fa-circle-exclamation"></i>

                    <h3>${data.detail || "Failed to generate itinerary."}</h3>

                </div>

            `;

            return;

        }

        // Render Markdown beautifully
        itinerary.innerHTML = marked.parse(data.itinerary);

    }

    catch (error) {

        console.error(error);

        loading.innerHTML = "";

        itinerary.innerHTML = `

            <div class="empty">

                <i class="fa-solid fa-triangle-exclamation"></i>

                <h3>Server Error</h3>

                <p>Please try again later.</p>

            </div>

        `;

    }

});