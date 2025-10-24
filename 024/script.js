
const beschreibung = document.getElementById("beschreibung");
beschreibung.textContent = "js js js js js js ";


const heading = document.querySelector("h1");
heading.innerHTML = "Hiiiii – <strong>Strong strong</strong>";


const kacheln = document.querySelectorAll(".kachel");
kacheln.forEach(kachel => {
  kachel.style.backgroundColor = "#f04040ff";
  kachel.classList.add("activated");
});


const imgS = document.querySelector("img");
imgS.src = "https://upload.wikimedia.org/wikipedia/commons/c/ce/Unofficial_JavaScript_logo.svg";
imgS.alt = "alt js js js js";


const statusAnzeige = document.getElementById("status-anzeige");
statusAnzeige.setAttribute("data-initial-status", "ready");



const klickMichBtn = document.getElementById("klick-mich");
const meldungDiv = document.getElementById("meldung");
let counter = 0;

function welcomeEvent(event) {
  counter++;
  console.log("Event-Objekt:", event);
  console.log("Auslöser:", event.target);

  meldungDiv.textContent = `hiii ${counter} click`;

  if (counter >= 5) {
    meldungDiv.textContent = "You clicked 5 times – no further actions.";
    klickMichBtn.removeEventListener("click", welcomeEvent);
  }
}

klickMichBtn.addEventListener("click", welcomeEvent);





document.getElementById("toggle-stil").addEventListener("click", () => {
  meldungDiv.classList.toggle("highlighted");
});
