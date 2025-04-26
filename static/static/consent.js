// إنشاء بانر الكوكيز
const banner = document.createElement('div');
banner.id = 'cookie-banner';
banner.style.cssText = `
  position: fixed;
  bottom: 0;
  width: 100%;
  background: #f1f1f1;
  color: #333;
  padding: 15px;
  font-size: 16px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  z-index: 9999;
  text-align: center;
  word-wrap: break-word;
`;

// نص الرسالة
const message = document.createElement('div');
message.textContent = 'We use cookies to improve your experience. Do you consent to cookies?';

// زر القبول
const acceptBtn = document.createElement('button');
acceptBtn.textContent = 'Accept';
acceptBtn.style.cssText = `
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
`;

// زر الرفض
const declineBtn = document.createElement('button');
declineBtn.textContent = 'Decline';
declineBtn.style.cssText = `
  background-color: #f44336;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
`;

// وضع الأزرار في صف واحد
const buttonContainer = document.createElement('div');
buttonContainer.style.cssText = `
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  justify-content: center;
`;
buttonContainer.appendChild(acceptBtn);
buttonContainer.appendChild(declineBtn);

// إضافة النص والأزرار للبانر
banner.appendChild(message);
banner.appendChild(buttonContainer);

// وظائف الأزرار
acceptBtn.onclick = () => {
  localStorage.setItem('cookieConsent', 'accepted');
  banner.style.display = 'none';
  enableTracking();
};

declineBtn.onclick = () => {
  localStorage.setItem('cookieConsent', 'declined');
  banner.style.display = 'none';
};

// تفعيل Google Tag Manager إذا وافق
function enableTracking() {
  const gtagScript = document.createElement('script');
  gtagScript.src = "https://www.googletagmanager.com/gtag/js?id=G-PDD8WTVWD4"; // ← غير الكود لكودك الصحيح
  document.head.appendChild(gtagScript);

  gtagScript.onload = () => {
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-PDD8WTVWD4'); // ← غير الكود هنا لكودك
  };
}

// دارك مود تلقائي حسب المتصفح
function applyDarkMode() {
  if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    banner.style.background = '#333';
    banner.style.color = '#fff';
    acceptBtn.style.backgroundColor = '#388E3C';
    declineBtn.style.backgroundColor = '#D32F2F';
  }
}

// تحقق إذا المستخدم قبل أو لا
const consent = localStorage.getItem('cookieConsent');
if (!consent) {
  document.body.appendChild(banner);
  applyDarkMode();
} else if (consent === 'accepted') {
  enableTracking();
}