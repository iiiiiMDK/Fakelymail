// إنشاء البانر
const banner = document.createElement('div');
banner.id = 'cookie-banner';
banner.style.cssText = `
  position: fixed;
  bottom: 0;
  width: 100%;
  background: #f1f1f1;
  padding: 15px;
  font-size: 16px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  z-index: 9999;
  word-break: break-word;
`;

// نص الرسالة
const message = document.createElement('div');
message.textContent = "We use cookies to improve your experience. Do you consent to cookies?";

// زر القبول
const acceptBtn = document.createElement('button');
acceptBtn.textContent = 'Accept';
acceptBtn.style.cssText = `
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  border: none;
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
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
`;

// حاوية الأزرار
const buttonContainer = document.createElement('div');
buttonContainer.style.cssText = `
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  justify-content: center;
`;

// إضافة الأزرار للحاوية
buttonContainer.appendChild(acceptBtn);
buttonContainer.appendChild(declineBtn);

// إضافة النص والأزرار للبانر
banner.appendChild(message);
banner.appendChild(buttonContainer);

// تحميل Google Tag Manager إذا وافق المستخدم
function enableTracking() {
  const tagScript = document.createElement('script');
  tagScript.src = "https://www.googletagmanager.com/gtag/js?id=G-PD08MTWD4J"; // غير الكود إلى كودك إذا لازم
  document.head.appendChild(tagScript);

  tagScript.onload = () => {
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-PD08MTWD4J');
  };
}

// تفعيل الدارك مود
function applyDarkMode() {
  if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    banner.style.background = '#333';
    banner.style.color = '#fff';
    acceptBtn.style.backgroundColor = '#4CAF50';
    declineBtn.style.backgroundColor = '#f44336';
  } else {
    banner.style.background = '#f1f1f1';
    banner.style.color = '#000';
    acceptBtn.style.backgroundColor = '#4CAF50';
    declineBtn.style.backgroundColor = '#f44336';
  }
}

// أحداث الضغط على الأزرار
acceptBtn.onclick = () => {
  localStorage.setItem('cookieConsent', 'accepted');
  banner.style.display = 'none';
  enableTracking();
};

declineBtn.onclick = () => {
  localStorage.setItem('cookieConsent', 'declined');
  banner.style.display = 'none';
};

// التحقق عند تحميل الصفحة
const consent = localStorage.getItem('cookieConsent');
if (!consent) {
  document.body.appendChild(banner);
  applyDarkMode();
} else if (consent === 'accepted') {
  enableTracking();
}