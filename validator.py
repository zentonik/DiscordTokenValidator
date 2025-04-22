import requests

def check_token(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    res = requests.get("https://discord.com/api/v10/users/@me", headers=headers)

    if res.status_code == 200:
        user = res.json()
        print(f"TOKEN        : {token}")
        print("Valid?       : ✅ Yes")
        print(f"Username     : {user['username']}#{user['discriminator']}")
        print(f"ID           : {user['id']}")
        print(f"Email        : {user.get('email', 'None')}")
        print(f"Phone        : {user.get('phone', 'None')}")
        print(f"MFA Enabled? : {'Yes' if user['mfa_enabled'] else 'No'}")
        print(f"Verified?    : {'Yes' if user['verified'] else 'No'}")

        billing = requests.get("https://discord.com/api/v10/users/@me/billing/payment-sources", headers=headers)
        print(f"Billing?     : {'Yes' if billing.json() else 'No'}")

        nitro = user.get("premium_type", 0)
        nitro_status = {0: "No", 1: "Nitro Classic", 2: "Nitro", 3: "Nitro Basic"}.get(nitro, "Unknown")
        print(f"Nitro?       : {nitro_status}")

    elif res.status_code == 401:
        print(f"TOKEN        : {token}")
        print("Valid?       : ❌ No")
    else:
        print(f"Error: {res.status_code}")

if __name__ == "__main__":
    token = input("Enter token: ").strip()
    check_token(token)
