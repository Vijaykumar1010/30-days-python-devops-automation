// Demo-only client-side login. Do not use hardcoded credentials in production.
const DEMO_EMAIL = "fitness@example.com";
const DEMO_PASSWORD = "Fit@123";

const loginForm = document.getElementById("loginForm");
const loginView = document.getElementById("loginView");
const dashboardView = document.getElementById("dashboardView");
const errorMessage = document.getElementById("errorMessage");
const logoutButton = document.getElementById("logoutButton");

loginForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value;

  if (email === DEMO_EMAIL && password === DEMO_PASSWORD) {
    errorMessage.textContent = "";
    loginView.classList.add("hidden");
    dashboardView.classList.remove("hidden");
  } else {
    errorMessage.textContent = "Incorrect email or password. Please try again.";
  }
});

logoutButton.addEventListener("click", () => {
  dashboardView.classList.add("hidden");
  loginView.classList.remove("hidden");
  loginForm.reset();
});
