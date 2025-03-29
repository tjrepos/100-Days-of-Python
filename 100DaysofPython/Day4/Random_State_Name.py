import random
states_alphabetical = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii",
          "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri",
          "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York",
          "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia",
          "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

state_working = states_alphabetical
print(states_alphabetical[49])
print(states_alphabetical[random.randint(0, 49)])
state_working[0] = "Balaska"
print(state_working[0])
state_working.append("Newland")
print(state_working)
state_working.extend(["New Newland", "Old Zealand"])
print(state_working)