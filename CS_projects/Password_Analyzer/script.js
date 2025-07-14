const passwordInput = document.getElementById("password");
const scoreDiv = document.getElementById("score");
const feedbackDiv = document.getElementById("fdbck");

passwordInput.addEventListener("input", () => {
  const pw = passwordInput.value;
  const result = zxcvbn(pw);

    const scoreLabels = ["Very Weak", "Weak", "Fair", "Good", "Strong"];
  scoreDiv.textContent = `Score: ${scoreLabels[result.score]} (${result.score}/4)`;
});