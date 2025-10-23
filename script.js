const registerBtn = document.getElementById("registerBtn");
const msg = document.getElementById("registerMsg");

registerBtn.addEventListener("click", async () => {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  const res = await fetch("https://movie-app-pccj.onrender.com/users/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password })
  });

  const data = await res.json();
  msg.textContent = data.message || "Erro ao criar usuário";
});
