document.addEventListener("DOMContentLoaded", function () {
    const banner = document.createElement("div");
    banner.id = "cookie-banner";
    banner.innerHTML = `
      <div class="cookie-box">
        <p>We use cookies to improve your experience. Do you consent to cookies?</p>
        <div class="cookie-buttons">
          <button id="acceptCookies">Accept</button>
          <button id="rejectCookies">Decline</button>
        </div>
      </div>
    `;
    document.body.appendChild(banner);
  
    const style = document.createElement("style");
    style.textContent = `
      #cookie-banner {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #fff;
        color: #000;
        padding: 15px;
        box-shadow: 0 -2px 5px rgba(0,0,0,0.1);
        z-index: 9999;
        font-family: sans-serif;
      }
  
      .cookie-box {
        display: flex;
        flex-direction: column;
        gap: 10px;
        text-align: center;
      }
  
      .cookie-buttons {
        display: flex;
        justify-content: center;
        gap: 10px;
      }
  
      .cookie-buttons button {
        padding: 8px 16px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-weight: bold;
      }
  
      #acceptCookies {
        background-color: #4caf50;
        color: white;
      }
  
      #rejectCookies {
        background-color: #f44336;
        color: white;
      }
  
      @media (prefers-color-scheme: dark) {
        #cookie-banner {
          background-color: #222;
          color: #eee;
        }
      }
  
      @media screen and (max-width: 600px) {
        .cookie-box {
          font-size: 14px;
        }
        .cookie-buttons {
          flex-direction: column;
        }
      }
    `;
    document.head.appendChild(style);
  
    function hideBanner() {
      banner.remove();
    }
  
    document.getElementById("acceptCookies").onclick = function () {
      gtag('consent', 'update', {
        ad_storage: 'granted',
        analytics_storage: 'granted'
      });
      hideBanner();
    };
  
    document.getElementById("rejectCookies").onclick = function () {
      gtag('consent', 'update', {
        ad_storage: 'denied',
        analytics_storage: 'denied'
      });
      hideBanner();
    };
  });