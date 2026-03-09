document.addEventListener("DOMContentLoaded", () => {
    // --- MULTI-SELECT EMOTION LOGIC ---
    const chips = document.querySelectorAll(".chip");
    const hiddenInput = document.getElementById("selectedEmotion");
    let activeEmotions = ["sad"]; // Default

    // Sync initial value
    hiddenInput.value = activeEmotions.join(", ");

    chips.forEach(chip => {
        chip.addEventListener("click", () => {
            const val = chip.dataset.value;

            if (activeEmotions.includes(val)) {
                // Prevent deselecting if it's the only one left
                if (activeEmotions.length > 1) {
                    activeEmotions = activeEmotions.filter(e => e !== val);
                    chip.classList.remove("active");
                }
            } else {
                // Logic: Allow max 2 emotions. If 2 are selected, remove the oldest one.
                if (activeEmotions.length < 2) {
                    activeEmotions.push(val);
                    chip.classList.add("active");
                } else {
                    const removed = activeEmotions.shift(); // Remove first
                    // Find the chip corresponding to the removed value and uncheck it
                    const removedChip = document.querySelector(`.chip[data-value="${removed}"]`);
                    if (removedChip) removedChip.classList.remove("active");
                    
                    activeEmotions.push(val);
                    chip.classList.add("active");
                }
            }
            hiddenInput.value = activeEmotions.join(", ");
        });
    });
});

function updateValues() {
    document.getElementById("strengthValue").innerText = document.getElementById("strength").value;
    document.getElementById("creativityValue").innerText = document.getElementById("creativity").value;
}

// --- GENERATION LOGIC ---
let generatedTextBuffer = "";
let activeController = null;

async function generateStory() {
    const promptText = document.getElementById("prompt").value;
    const emotionRaw = document.getElementById("selectedEmotion").value;
    const strength = document.getElementById("strength").value;
    const creativity = document.getElementById("creativity").value;
    
    const outputDiv = document.getElementById("storyOutput");
    const btn = document.getElementById("generateBtn");
    const saveBtn = document.getElementById("saveBtn");

    if (!promptText.trim()) {
        alert("Please enter a story seed first.");
        return;
    }

    // Cancel any in-progress generation
    if (activeController) {
        activeController.abort();
    }
    activeController = new AbortController();

    // UI Reset
    outputDiv.innerHTML = ""; 
    generatedTextBuffer = "";
    saveBtn.disabled = true;

    btn.disabled = true;
    btn.innerHTML = `<span class="btn-text">Weaving...</span>`;

    try {
        const response = await fetch("/generate", {
            signal: activeController.signal,
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                prompt: promptText,
                emotion: emotionRaw,
                strength: parseInt(strength),
                creativity: parseFloat(creativity)
            })
        });

        if (!response.ok) {
            throw new Error(`Server Error: ${response.statusText}`);
        }

        const reader = response.body.getReader();
        const decoder = new TextDecoder();

        while (true) {
            const { done, value } = await reader.read();
            if (done) break;

            const chunk = decoder.decode(value, { stream: true });

            // Strip markdown formatting and append as safe text (no innerHTML)
            const cleanChunk = chunk
                .replace(/\*\*/g, "")
                .replace(/##/g, "");

            outputDiv.appendChild(document.createTextNode(cleanChunk));
            generatedTextBuffer += chunk; // Keep original formatting for download
            
            // Auto-scroll to bottom
            const editorArea = document.querySelector('.editor-area');
            if(editorArea) editorArea.scrollTop = editorArea.scrollHeight;
        }

        saveBtn.disabled = false;
    } catch (error) {
        if (error.name !== "AbortError") {
            outputDiv.innerHTML = `<div class="empty-state" style="color: #ef4444">
                ⚠️ <strong>Generation Failed</strong><br>
                ${error.message || "Is the backend running?"}
            </div>`;
            console.error(error);
        }
    } finally {
        activeController = null;
        btn.disabled = false;
        btn.innerHTML = `<span class="btn-text">Weave Story</span><span class="btn-icon">✨</span>`;
    }
}

function saveStory() {
    if (!generatedTextBuffer) return;
    const blob = new Blob([generatedTextBuffer], { type: "text/plain" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "story.txt";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}