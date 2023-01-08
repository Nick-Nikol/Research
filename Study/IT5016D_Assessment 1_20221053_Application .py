print("Prepare your ingredients and your ribs\n"
      "Remove Silver side from ribs\n"
      "Combine your Mixture\n"
      "Spread Mixture on the ribs\n"
      "Pre heat the BBQ to 82c\n")

bbq_temp = int(input("What is the current BBQ temperature"))
while bbq_temp != 82:
      if bbq_temp > 82:
            print("decrease the temperature")
            bbq_temp = int(input("What is the current BBQ Temp"))
      else:
            print("increase the temperature")
            bbq_temp = int(input("What is the current BBQ Temp"))

print("Place the meat on the BBQ bone down")
print("Wait for 3 hours")
print("Meat should be 71c")

rib_temp = int(input("What is the current RIBS temperature"))
while rib_temp != 71:
      if rib_temp > 71:
            print("Transfer to the baking sheet")
            rib_temp = int(input("What is the current RIBS Temp"))
      else:
            print("Recheck after 10min")
            rib_temp = int(input("What is the current RIBS Temp"))

print("Transfer to the baking sheet on the table")
print("Apply your souce")
print("Wrap Ribs in Tin foel")

print("Increase BBQ temp to 107c")

bbq_temp2 = int(input("What is the current BBQ temperature"))
while bbq_temp2 != 107:
      if bbq_temp2 > 107:
            print("decrease the temperature")
            bbq_temp2 = int(input("What is the current BBQ Temp"))
      else:
            print("increase the temperature")
            bbq_temp2 = int(input("What is the current BBQ Temp"))

print("Place the meat on the BBQ bone down")
print("Wait for 2 hours")
print("Meat should be 107c")

rib_temp2 = int(input("What is the current RIBS temperature"))
while rib_temp2 != 107:
      if rib_temp2 > 107:
            print("Take it off and Rest for 30min")
            rib_temp2 = int(input("What is the current RIBS Temp"))
      else:
            print("Recheck after 10min")
            rib_temp2 = int(input("What is the current RIBS Temp"))


print("Take it off and Rest for 30min")
print("Enjoy!!")