document.addEventListener('DOMContentLoaded', function () {
    if (!localStorage.getItem('cookieConsent')) {
      const banner = document.createElement('div');
      banner.id = 'cookie-banner';
      banner.style.cssText = `
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background: #ffffff;
        border-top: 1px solid #ccc;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
        padding: 15px;
        text-align: center;
        font-size: 14px;
        z-index: 9999;
        opacity: 0;
        transition: opacity 0.8s ease;
        display: flex;
        flex-direction: column;
        align-items: center;
      `;
  
      banner.innerHTML = `
        <span style="margin-bottom:10px;">We use cookies to enhance your experience. Do you consent to the use of cookies?</span>
        <div>
          <button id="acceptCookies" style="padding:8px 16px; margin:5px; background:#4CAF50; color:white; border:none; border-radius:4px; cursor:pointer;">Accept</button>
          <button id="declineCookies" style="padding:8px 16px; margin:5px; background:#e74c3c; color:white; border:none; border-radius:4px; cursor:pointer;">Decline</button>
        </div>
      `;
  
      document.body.appendChild(banner);
  
      setTimeout(() => {
        banner.style.opacity = 1;
      }, 100);
  
      document.getElementById('acceptCookies').addEventListener('click', function () {
        localStorage.setItem('cookieConsent', 'accepted');
        enableAnalytics();
        hideBanner();
      });
  
      document.getElementById('declineCookies').addEventListener('click', function () {
        localStorage.setItem('cookieConsent', 'declined');
        hideBanner();
      });
  
      function hideBanner() {
        banner.style.opacity = 0;
        setTimeout(() => {
          banner.remove();
        }, 800);
      }
    } else if (localStorage.getItem('cookieConsent') === 'accepted') {
      enableAnalytics();
    }
  
    function enableAnalytics() {
      const analyticsScript = document.createElement('script');
      analyticsScript.async = true;
      analyticsScript.src = "https://www.googletagmanager.com/gtag/js?id=G-PDD8WTVWD4"; // غير G-XXXXXXXXXX لكودك
      document.head.appendChild(analyticsScript);
  
      analyticsScript.onload = function() {
        window.dataLayer = window.dataLayer || [];
        function gtag(){ dataLayer.push(arguments); }
        gtag('js', new Date());
        gtag('config', 'G-PDD8WTVWD4'); // وغير هذا لكودك
      };
    }
  });
  