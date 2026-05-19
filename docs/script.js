const STORAGE_PREFIX = "indaba-course-progress-";

const toggles = Array.from(document.querySelectorAll(".progress-toggle"));
const progressBar = document.getElementById("progressBar");
const progressText = document.getElementById("progressText");
const resetButton = document.getElementById("resetProgress");
const lastUpdated = document.getElementById("lastUpdated");

function readState(key) {
  return localStorage.getItem(STORAGE_PREFIX + key) === "true";
}

function writeState(key, value) {
  localStorage.setItem(STORAGE_PREFIX + key, String(value));
}

function clearState() {
  toggles.forEach((toggle) => {
    writeState(toggle.dataset.key, false);
    toggle.checked = false;
  });
  renderProgress();
}

function renderProgress() {
  const completed = toggles.filter((toggle) => toggle.checked).length;
  const total = toggles.length;
  const percent = total === 0 ? 0 : (completed / total) * 100;

  progressBar.style.width = `${percent}%`;
  progressText.textContent = `${completed} of ${total} modules complete`;

  const cards = Array.from(document.querySelectorAll(".module-card"));
  cards.forEach((card) => card.classList.remove("is-next"));

  const nextCard = cards.find((card) => {
    const id = card.dataset.moduleId;
    return !readState(id);
  });

  if (nextCard) {
    nextCard.classList.add("is-next");
  }
}

toggles.forEach((toggle) => {
  const key = toggle.dataset.key;
  toggle.checked = readState(key);

  toggle.addEventListener("change", () => {
    writeState(key, toggle.checked);
    renderProgress();
  });
});

if (resetButton) {
  resetButton.addEventListener("click", clearState);
}

if (lastUpdated) {
  const now = new Date();
  lastUpdated.textContent = `Hub opened: ${now.toLocaleDateString()} ${now.toLocaleTimeString()}`;
}

renderProgress();
