window.addEventListener('DOMContentLoaded', function () {
    if (localStorage.getItem('consentGiven') !== 'true' && localStorage.getItem('consentGiven') !== 'false') {
      const banner = document.createElement('div');
      banner.id = "cookie-banner";
      banner.style.position = "fixed";
      banner.style.bottom = "0";
      banner.style.left = "0";
      banner.style.width = "100%";
      banner.style.background = "#fff";
      banner.style.borderTop = "1px solid #ccc";
      banner.style.padding = "15px";
      banner.style.textAlign = "center";
      banner.style.zIndex = "9999";
      banner.style.opacity = "0";
      banner.style.transition = "opacity 0.8s ease";
      banner.style.boxShadow = "0 -2px 10px rgba(0,0,0,0.1)";
      banner.style.display = "flex";
      banner.style.flexDirection = "column";
      banner.style.alignItems = "center";
      banner.style.justifyContent = "center";
      banner.style.fontSize = "14px";
  
      banner.innerHTML = `
        <span style="margin-bottom:10px;">We use cookies to enhance your experience. Do you consent to the use of cookies?</span>
        <div>
          <button id="acceptConsent" style="padding:8px 16px; margin:5px; background:#4CAF50; color:white; border:none; border-radius:4px; cursor:pointer;">Accept</button>
          <button id="declineConsent" style="padding:8px 16px; margin:5px; background:#e74c3c; color:white; border:none; border-radius:4px; cursor:pointer;">Decline</button>
        </div>
      `;
      document.body.appendChild(banner);
  
      setTimeout(() => {
        banner.style.opacity = "1";
      }, 100); // يخليه يظهر بشكل ناعم
  
      document.getElementById('acceptConsent').onclick = function () {
        localStorage.setItem('consentGiven', 'true');
        fadeOutBanner();
        enableAnalytics();
      };
  
      document.getElementById('declineConsent').onclick = function () {
        localStorage.setItem('consentGiven', 'false');
        fadeOutBanner();
      };
  
      function fadeOutBanner() {
        banner.style.opacity = "0";
        setTimeout(() => {
          banner.remove();
        }, 800);
      }
    } else if (localStorage.getItem('consentGiven') === 'true') {
      enableAnalytics();
    }
  
    function enableAnalytics() {
      const script = document.createElement('script');
      script.async = true;
      script.src = "https://www.googletagmanager.com/gtag/js?id=G-PDD8WTVWD4"; // غيره لكودك
      document.head.appendChild(script);
  
      window.dataLayer = window.dataLayer || [];
      function gtag(){ dataLayer.push(arguments); }
      gtag('js', new Date());
      gtag('config', 'G-PDD8WTVWD4'); // غيره لكودك
    }
  });
  