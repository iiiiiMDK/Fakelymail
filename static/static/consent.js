document.addEventListener("DOMContentLoaded", function () {
  const consent = localStorage.getItem("cookieConsent");

  if (consent === "accepted") {
    // إذا وافق خلاص ما نظهر البنر أبدًا
    return;
  }

  const banner = document.createElement("div");
  banner.id = "cookie-banner";
  banner.style = `
    max-width: 90%;
    margin: auto;
    background: ${window.matchMedia('(prefers-color-scheme: dark)').matches ? '#2f3640' : '#ffffff'};
    color: ${window.matchMedia('(prefers-color-scheme: dark)').matches ? '#dfe6e9' : '#2f3640'};
    padding: 15px;
    border-radius: 8px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.2);
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    text-align: center;
    font-family: Arial, sans-serif;
    z-index: 9999;
    transition: background 0.3s, color 0.3s;
  `;

  banner.innerHTML = `
    <p style="margin-bottom: 10px; font-size: 15px;">
      We use cookies to improve your experience. Do you consent to cookies?
    </p>
    <div style="display: flex; justify-content: center; gap: 10px; flex-wrap: wrap;">
      <button id="acceptCookies" style="
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 14px;
      ">Accept</button>
      <button id="declineCookies" style="
        background-color: #f44336;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 14px;
      ">Decline</button>
    </div>
  `;

  document.body.appendChild(banner);

  document.getElementById("acceptCookies").onclick = function () {
    localStorage.setItem("cookieConsent", "accepted");
    gtag('consent', 'update', {
      ad_storage: 'granted',
      analytics_storage: 'granted'
    });
    banner.remove(); // خلاص نحذفه للأبد.
  };

  document.getElementById("declineCookies").onclick = function () {
    localStorage.setItem("cookieConsent", "declined");
    gtag('consent', 'update', {
      ad_storage: 'denied',
      analytics_storage: 'denied'
    });
    banner.remove(); // نحذفه مؤقت بس لما يدخل يرجع يظهر له
  };
});
