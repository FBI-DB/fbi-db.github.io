const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if (username === "aiaiadmin" && password === "aiai001") {
        alert("You have successfully logged in.");
        window.location.replace("http://googl1.harlenmtcsw.repl.co/neon.html")
    } else {
        loginErrorMsg.style.opacity = 1;
    }
})
