document.addEventListener("DOMContentLoaded", () => {
  const FORMAL_FALLACIES = [
    "affirming the consequent",
    "denying the antecedent",
    "equivocation",
    "fallacy of composition",
    "fallacy of division",
    "false cause",
    "slippery slope",
  ];
  const INFORMAL_FALLACIES = [
    "ad hominem",
    "appeal to authority",
    "appeal to emotion",
    "appeal to popularity",
    "appeal to tradition",
    "begging the question",
    "circular reasoning",
    "fallacy of the beard",
    "false dilemma",
    "hasty generalization",
    "red herring",
    "strawman argument",
    "tu quoque",
  ];

  const formalSelect = document.getElementById("formal-fallacies");
  const informalSelect = document.getElementById("informal-fallacies");

  FORMAL_FALLACIES.forEach((fallacy) => {
    const option = document.createElement("option");
    option.value = fallacy;
    option.text = fallacy;
    formalSelect.add(option);
  });

  INFORMAL_FALLACIES.forEach((fallacy) => {
    const option = document.createElement("option");
    option.value = fallacy;
    option.text = fallacy;
    informalSelect.add(option);
  });

  formalSelect.addEventListener("change", () => {
    const selectedOption = formalSelect.options[formalSelect.selectedIndex];
    if (selectedOption.value) {
      createSelectedFallacy("formal-fallacies", selectedOption.text);
      formalSelect.remove(formalSelect.selectedIndex);
    }
  });

  informalSelect.addEventListener("change", () => {
    const selectedOption = informalSelect.options[informalSelect.selectedIndex];
    if (selectedOption.value) {
      createSelectedFallacy("informal-fallacies", selectedOption.text);
      informalSelect.remove(informalSelect.selectedIndex);
    }
  });

  document.getElementById("analyze-btn").addEventListener("click", async () => {
    const selectedText = document.getElementById("selected-text").value;
    chrome.runtime.sendMessage({ action: "analyzeText", selectedText });
    window.close();
  });
});

function createSelectedFallacy(fallacyType, fallacyText) {
  const selectedFallaciesContainer = document.querySelector(".selected-fallacies");
  const fallacyElement = document.createElement("div");
  fallacyElement.classList.add("fallacy");
  fallacyElement.dataset.type = fallacyType;
  fallacyElement.textContent = fallacyText;

  fallacyElement.addEventListener("click", () => {
    const selectElement = document.getElementById(fallacyType);
    const option = document.createElement("option");
    option.value = fallacyText;
    option.text = fallacyText;
    selectElement.add(option);

    selectedFallaciesContainer.removeChild(fallacyElement);
  });

  selectedFallaciesContainer.appendChild(fallacyElement);
}
