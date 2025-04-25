document.addEventListener("DOMContentLoaded", function () {
    const banner = document.createElement("div");
    banner.id = "cookie-banner";
    banner.innerHTML = `
      <p>We use cookies to improve your experience. Do you consent to cookies?</p>
      <div class="cookie-buttons">
        <button id="acceptCookies">Accept</button>
        <button id="rejectCookies">Decline</button>
      </div>
    `;
    document.body.appendChild(banner);
  
    document.getElementById("acceptCookies").onclick = function () {
      localStorage.setItem("cookiesAccepted", "true");
      document.getElementById("cookie-banner").remove();
      // Consent granted
      gtag("consent", "update", {
        ad_storage: "granted",
        analytics_storage: "granted"
      });
    };
  
    document.getElementById("rejectCookies").onclick = function () {
      localStorage.setItem("cookiesAccepted", "false");
      document.getElementById("cookie-banner").remove();
      // Consent denied
      gtag("consent", "update", {
        ad_storage: "denied",
        analytics_storage: "denied"
      });
    };
  
    if (localStorage.getItem("cookiesAccepted") === null) {
      banner.style.display = "flex";
    }
  });