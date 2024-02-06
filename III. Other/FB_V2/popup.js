document.getElementById("clear-btn").addEventListener("click", () => {
  document.getElementById("analysis-results").innerHTML = "";
});

document.getElementById("close-btn").addEventListener("click", () => {
  const popup = document.getElementById("analysis-popup");
  popup.style.display = "none";
});

// Add code to make the popup draggable and resizable

function makeDraggable(element) {
  let posX = 0,
    posY = 0,
    dragX = 0,
    dragY = 0;
  element.onmousedown = dragMouseDown;

  function dragMouseDown(e) {
    e = e || window.event;
    e.preventDefault();
    dragX = e.clientX;
    dragY = e.clientY;
    document.onmouseup = closeDrag;
    document.onmousemove = drag;
  }

  function drag(e) {
    e = e || window.event;
    e.preventDefault();
    posX = dragX - e.clientX;
    posY = dragY - e.clientY;
    dragX = e.clientX;
    dragY = e.clientY;
    element.style.top = element.offsetTop - posY + "px";
    element.style.left = element.offsetLeft - posX + "px";
  }

  function closeDrag() {
    document.onmouseup = null;
    document.onmousemove = null;
  }
}

function makeResizable(element) {
  // Add code to make the popup resizable
}

const popup = document.getElementById("analysis-popup");
makeDraggable(popup);
makeResizable(popup);
