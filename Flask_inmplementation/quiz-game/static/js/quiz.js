const quizId = sessionStorage.getItem("quiz_id");
const category = sessionStorage.getItem("category");

if (!quizId) {
    window.location.href = "/categories";
}

document.getElementById("category-title").textContent = (category || "QUIZ").toUpperCase();

let selectedAnswer = null;

async function loadQuestion() {
    const container = document.getElementById("question-container");
    const errorDiv = document.getElementById("error");
    const submitBtn = document.getElementById("submit-btn");
    const nextBtn = document.getElementById("next-btn");
    const resultsBtn = document.getElementById("results-btn");
    const feedback = document.getElementById("feedback");

    feedback.classList.add("hidden");
    feedback.classList.remove("correct", "incorrect");
    nextBtn.classList.add("hidden");
    resultsBtn.classList.add("hidden");
    submitBtn.classList.add("hidden");
    selectedAnswer = null;

    try {
        const response = await fetch("/api/quiz/" + quizId + "/question");
        const data = await response.json();

        if (!response.ok) {
            container.innerHTML = `
                <p class="question-text" style="text-align:center;">
                    Quiz Over<br>
                    <span style="font-size:0.9rem;color:var(--text-dim);">${data.reason || data.message || ""}</span>
                </p>`;
            resultsBtn.classList.remove("hidden");
            return;
        }

        document.getElementById("score").textContent = data.score;
        document.getElementById("strikes").textContent = data.strikes;
        document.getElementById("question-number").textContent =
            `QUESTION ${data.question_number} / ${data.total_questions}`;

        let html = `<p class="question-text">${data.question}</p><div class="options">`;

        for (let key in data.options) {
            html += `
                <label class="option" data-value="${key}">
                    <input type="radio" name="answer" value="${key}">
                    <span class="letter">${key}</span>
                    <span>${data.options[key]}</span>
                </label>`;
        }
        html += "</div>";

        container.innerHTML = html;
        submitBtn.classList.remove("hidden");

        // click handlers for options
        document.querySelectorAll(".option").forEach(opt => {
            opt.addEventListener("click", () => {
                document.querySelectorAll(".option").forEach(o => o.classList.remove("selected"));
                opt.classList.add("selected");
                selectedAnswer = opt.dataset.value;
                opt.querySelector("input").checked = true;
            });
        });

    } catch (err) {
        errorDiv.textContent = "Could not load question.";
        errorDiv.classList.remove("hidden");
    }
}

document.getElementById("submit-btn").addEventListener("click", async () => {
    if (!selectedAnswer) {
        alert("Please select an answer first!");
        return;
    }

    const errorDiv = document.getElementById("error");
    const feedback = document.getElementById("feedback");
    const submitBtn = document.getElementById("submit-btn");
    const nextBtn = document.getElementById("next-btn");
    const resultsBtn = document.getElementById("results-btn");

    try {
        const response = await fetch("/api/quiz/" + quizId + "/answer", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ answer: selectedAnswer })
        });

        const data = await response.json();

        if (!response.ok) {
            errorDiv.textContent = data.error || "Error submitting answer";
            errorDiv.classList.remove("hidden");
            return;
        }

        document.getElementById("score").textContent = data.score;
        document.getElementById("strikes").textContent = data.strikes;

        // visual feedback on options
        document.querySelectorAll(".option").forEach(opt => {
            const val = opt.dataset.value;
            if (data.correct && val === selectedAnswer) {
                opt.classList.add("correct");
            } else if (!data.correct) {
                if (val === selectedAnswer) opt.classList.add("incorrect");
                if (data.correct_answer && val === data.correct_answer) {
                    opt.classList.add("correct");
                }
            }
            // disable further clicks
            opt.style.pointerEvents = "none";
        });

        feedback.classList.remove("hidden", "correct", "incorrect");
        if (data.correct) {
            feedback.textContent = "✓ CORRECT";
            feedback.classList.add("correct");
        } else {
            feedback.textContent = data.correct_answer
                ? `✗ WRONG — Answer was ${data.correct_answer}`
                : "✗ WRONG";
            feedback.classList.add("incorrect");
        }

        submitBtn.classList.add("hidden");

        if (data.completed) {
            resultsBtn.classList.remove("hidden");
        } else {
            nextBtn.classList.remove("hidden");
        }

    } catch (err) {
        errorDiv.textContent = "Error submitting answer.";
        errorDiv.classList.remove("hidden");
    }
});

document.getElementById("next-btn").addEventListener("click", () => {
    loadQuestion();
});

document.getElementById("results-btn").addEventListener("click", () => {
    window.location.href = "/result";
});

loadQuestion();