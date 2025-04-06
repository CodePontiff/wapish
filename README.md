# 📌 wapish WhatsApp phising Form Generator  

## ⚠️ Disclaimer
## 🚨 For educational purposes only. Do not use for phishing, fraud, or any malicious activities. Misuse of this script is strictly prohibited.

## 🚀 What is the WhatsApp Preview Link Feature?  
The **WhatsApp Preview Link** feature allows users to see a **preview of a shared URL**, before clicking on it, also i think it's enabled by default . When a link is sent, WhatsApp automatically **fetches metadata** (title, description, and thumbnail) and displays a preview.  

While this enhances the user experience, **attackers can manipulate this feature** to craft deceptive URLs that look safe but actually contain sensitive data.  

---

## 🔧 About This Script  
wa.me can redirect user into whatsapp app automatictly with some message like this:
https://api.whatsapp.com/send?phone=${phoneNumber}&text=hello
This **Python script** generates an **HTML form** that collects user credentials (**email, username, password**) and **automatically redirects** the user to **WhatsApp with a pre-filled message** containing this information.  

the attacker can use this to trick users into exposing their details via a manipulated preview link.

---

## 🛠️ Features  
✅ Generates a **custom registration form**  
✅ Allows setting a **custom Ngrok URL & WhatsApp number**  
✅ Automatically redirects users to **WhatsApp with a pre-filled message**  
✅ **Command-line friendly** with customizable output file  
✅ **custom phising form** manualy 

---

## 📌 Installation & Usage  
### 1️⃣ **Clone the Repository**  
```sh
git clone https://github.com/CodePontiff/wapish.git
cd wapish
start ngrok service "ngrok http 80"
start apache2 service if you want run this locally (not recommended)
python wapish.py -u https://you-ngrok-urlngrok-free.app -ph whatsapp_phone_number -o test.html
```
