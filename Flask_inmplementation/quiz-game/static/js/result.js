const quizId = sessionStorage.getItem("quiz_id");

if (!quizId) {
    window.location.href = "/";
}

async function loadResult() {
    const box = document.getElementById("result-box");
    const errorDiv = document.getElementById("error");

    try {
        const response = await fetch("/api/quiz/" + quizId + "/result");
        const data = await response.json();

        if (!response.ok) {
            box.innerHTML = "";
            errorDiv.textContent = data.error || "Could not load results";
            errorDiv.classList.remove("hidden");
            return;
        }

        box.innerHTML = `
            <p><strong>Score:</strong> ${data.score} / ${data.total_questions}</p>
            <p><strong>Percentage:</strong> ${data.percentage}%</p>
            <p><strong>Strikes:</strong> ${data.strikes}</p>
        `;
    } catch (err) {
        box.innerHTML = "";
        errorDiv.textContent = "Error loading results.";
        errorDiv.classList.remove("hidden");
    }
}

loadResult();
