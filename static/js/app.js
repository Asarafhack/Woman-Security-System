document.getElementById("chatForm").addEventListener("submit", async function (e) {
    e.preventDefault();
    const message = document.getElementById("message").value;

    const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message }),
    });

    const data = await response.json();
    const chatbox = document.getElementById("messages");
    chatbox.innerHTML += `<p>You: ${message}</p><p>System: ${data.prediction}</p>`;
});
