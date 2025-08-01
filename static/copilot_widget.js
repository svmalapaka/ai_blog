document.addEventListener('DOMContentLoaded', () => {
  const input = document.getElementById('userInput');
  const messageContainer = document.getElementById('messages');

  if (!input || !messageContainer) {
    console.warn('Chat elements not found on page.');
    return;
  }

  window.sendMessage = function () {
    const msg = input.value.trim();
    if (!msg) return;

    // Show user's message
    messageContainer.innerHTML += `<div class="user-message"><strong>You:</strong> ${msg}</div>`;

    // Show assistant is thinking...
    messageContainer.innerHTML += `<div class="assistant-message"><em>Assistant is typing...</em></div>`;
    messageContainer.scrollTop = messageContainer.scrollHeight;

    // Send message to backend
    fetch('/api/respond', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: msg })
    })
      .then(res => res.json())
      .then(data => {
        // Show assistant's reply
        messageContainer.innerHTML += `<div class="assistant-message"><strong>Assistant:</strong> ${data.reply}</div>`;
        messageContainer.scrollTop = messageContainer.scrollHeight;
      })
      .catch(err => {
        // Fallback message
        messageContainer.innerHTML += `<div class="assistant-message"><strong>Assistant:</strong> Sorry, something went wrong.</div>`;
        console.error('Chat fetch error:', err);
      });

    // Reset input
    input.value = '';
    input.focus();
  };
});