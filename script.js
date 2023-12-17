
const bodyElements = [
  document.getElementById("home"),
  document.getElementById("about"),
  document.getElementById("projects"),
  document.getElementById("education"),
  document.getElementById("contact")
];

const navElements = [
  document.getElementById("homeNav"),
  document.getElementById("aboutNav"),
  document.getElementById("projectsNav"),
  document.getElementById("educationNav"),
  document.getElementById("contactNav")
]


window.onload = function() {
  highlightNav();
}

window.onscroll = function() {
  moveNav();
  highlightNav();
}

function moveNav() {
  var navbar = document.getElementById("nav");
  var scrollPos = window.scrollY;
  var windowHeight = window.innerHeight;

  var navbarOffset = 95 - scrollPos/windowHeight*100;

  if (navbarOffset < 5) {
    navbarOffset = 5;
  }

  navbar.style.top = (navbarOffset) + '%';
}

function highlightNav() {
  var found = false;

  var windowHeight = window.innerHeight;

  for (var i = 0; i < bodyElements.length; i++) {
    if (!found && checkVisible(bodyElements[i], windowHeight/3)) {
      found = true;
      navElements[i].style.color = "transparent";
    } else if (navElements[i].style.color == "transparent") {
      navElements[i].style.color = "inherit";
    }
  }
}

function checkVisible(elm, threshold, mode) {
  threshold = threshold || 0;
  mode = mode || 'visible';

  var rect = elm.getBoundingClientRect();
  var viewHeight = Math.max(document.documentElement.clientHeight, window.innerHeight);
  var above = rect.bottom - threshold < 0;
  var below = rect.top - viewHeight + threshold >= 0;

  return mode === 'above' ? above : (mode === 'below' ? below : !above && !below);
}

