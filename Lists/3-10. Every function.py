phone_brands = []
phone_brands.append("Apple")
phone_brands.append("Smasnug")
phone_brands.append("Huawei")
phone_brands.append("Xiaomi")


let_go = phone_brands.pop(0)

phone_brands.insert(1, "Lg")

phone_brands.remove("Xiaomi")

print(sorted(phone_brands))

phone_brands.sort()

phone_brands.reverse()



print(f"The {let_go} iPhone was too expensive.")

print(f"I have {len(phone_brands)} phones left.")
