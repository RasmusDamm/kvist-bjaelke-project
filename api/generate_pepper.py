import secrets

pepper = secrets.token_urlsafe(32)

print("Gem denne password pepper sikkert:")
print(f"PASSWORD_PEPPER={pepper}")