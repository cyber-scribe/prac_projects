const passwordInput = document.getElementById("password");
const scoreDiv = document.getElementById("score");
const feedbackDiv = document.getElementById("fdbck");

passwordInput.addEventListener("input", () => {
  const pw = passwordInput.value;
  const result = zxcvbn(pw);

  
});