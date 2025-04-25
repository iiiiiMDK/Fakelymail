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
      banner.style.boxShadow = "0 -2px 10px rgba(0,0,0,0.1)";
      banner.innerHTML = `
        <span style="margin-right: 10px;">We use cookies to enhance your experience. Do you consent to the use of cookies?</span>
        <button id="acceptConsent" style="padding:8px 16px; margin:0 5px; background:#4CAF50; color:white; border:none; border-radius:4px; cursor:pointer;">Accept</button>
        <button id="declineConsent" style="padding:8px 16px; margin:0 5px; background:#e74c3c; color:white; border:none; border-radius:4px; cursor:pointer;">Decline</button>
      `;
      document.body.appendChild(banner);
  
      document.getElementById('acceptConsent').onclick = function () {
        localStorage.setItem('consentGiven', 'true');
        enableAnalytics();
        banner.remove();
      };
  
      document.getElementById('declineConsent').onclick = function () {
        localStorage.setItem('consentGiven', 'false');
        banner.remove();
      };
    } else if (localStorage.getItem('consentGiven') === 'true') {
      enableAnalytics();
    }
  
    function enableAnalytics() {
      const script = document.createElement('script');
      script.async = true;
      script.src = "https://www.googletagmanager.com/gtag/js?id=G-PD08MTWD4J"; // غيّر هنا لكود موقعك
      document.head.appendChild(script);
  
      window.dataLayer = window.dataLayer || [];
      function gtag(){ dataLayer.push(arguments); }
      gtag('js', new Date());
      gtag('config', 'G-PD08MTWD4J'); // وغير هذا بعد لكودك
    }
  });
  