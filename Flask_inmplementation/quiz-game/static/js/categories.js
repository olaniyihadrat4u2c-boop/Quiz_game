let selectedCategory = null;

// Icons for each category (falls back to ⚡)
const CATEGORY_ICONS = {
    "General Knowledge": "🌍",
    "Science": "🔬",
    "Technology": "💻",
    "Movies & TV": "🎬",
    "Video Games": "🎮",
    "Space": "🚀",
    "Music": "🎵",
    "Internet & Memes": "😂"
};

async function loadCategories() {
    const loading = document.getElementById("loading");
    const errorDiv = document.getElementById("error");
    const list = document.getElementById("category-list");

    try {
        const response = await fetch("/api/categories");
        const data = await response.json();

        loading.classList.add("hidden");
        list.innerHTML = "";

        data.categories.forEach(cat => {
            // Support both old format (string) and new format ({name, count})
            const name = typeof cat === "string" ? cat : cat.name;
            const count = typeof cat === "object" ? cat.count : null;
            const icon = CATEGORY_ICONS[name] || "⚡";

            const card = document.createElement("div");
            card.className = "category-card";
            card.dataset.name = name;
            card.innerHTML = `
                <span class="icon">${icon}</span>
                <div class="name">${name}</div>
                ${count ? `<div class="count">${count} questions</div>` : ""}
            `;
            card.onclick = () => selectCategory(name, card);
            list.appendChild(card);
        });
    } catch (err) {
        loading.classList.add("hidden");
        errorDiv.textContent = "Could not load categories.";
        errorDiv.classList.remove("hidden");
    }
}

function selectCategory(name, cardEl) {
    selectedCategory = name;

    // highlight selected card
    document.querySelectorAll(".category-card").forEach(c => {
        c.classList.remove("selected");
    });
    cardEl.classList.add("selected");

    // show setup form
    document.getElementById("setup").classList.remove("hidden");
}

document.getElementById("start-btn").addEventListener("click", async () => {
    if (!selectedCategory) return;

    const num = document.getElementById("num-questions").value;
    const errorDiv = document.getElementById("error");
    errorDiv.classList.add("hidden");

    try {
        const response = await fetch("/api/quiz/start", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                category: selectedCategory,
                number_of_questions: parseInt(num)
            })
        });

        const data = await response.json();

        if (!response.ok) {
            errorDiv.textContent = data.error || "Could not start quiz";
            errorDiv.classList.remove("hidden");
            return;
        }

        sessionStorage.setItem("quiz_id", data.quiz_id);
        sessionStorage.setItem("category", data.category);

        window.location.href = "/quiz";
    } catch (err) {
        errorDiv.textContent = "Error starting quiz.";
        errorDiv.classList.remove("hidden");
    }
});

loadCategories();