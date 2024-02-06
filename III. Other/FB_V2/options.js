document.getElementById("save-api-key-btn").addEventListener("click", () => {
  const apiKey = document.getElementById("api-key-input").value;
  chrome.storage.local.set({ apiKey }, () => {
    alert("API key saved!");
  });
});
