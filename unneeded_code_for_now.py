# def openai_text_gen(prompt):
#     """This function uses the OpenAI API to generate text based on user input."""
#     response = client.chat.completions.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {
    #             "role": "system",
    #             "content": "You are a dungeon master for a Fantasy tabletop RPG. Your job is to create adventure scenarios for the user based on their input and track their weapons, health and damage.",
    #         },
    #         {"role": "user", "content": prompt},
    #     ],
    # )
    # return response.choices[0].message.content

# class Scene:
#     def __init__(self, description, choices=None):
#         self.description = description
#         self.choices = choices  # Dictionary of the choices text and references to next possible scenes

#     def present(self):
#         print(self.description)
#         if self.choices:  # If the scene has multiple options for the user
#             for i, (choice_text) in enumerate(self.choices.items()):
#                 print(f"{i+1}. {choice_text}")

#     def get_next_scene(self, choice_index):
#         if not self.choices:
#             return None
#         return self.choices.get(list(self.choices.keys())[choice_index - 1])

# def generate_choices(prompt):
#     """This function uses the OpenAI API to generate text based on user input."""
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "user", "content": prompt},
#         ],
#     )
#     choices = {}
#     for choice_text in response.choices[0].message.content.split("\n"):
#         if "find a weapon" in choice_text.lower():
#             weapon_name = ...  # Extract weapon name from choice text
#             weapon_damage = ...  # Determine damage based on weapon type
#             weapon = Weapon(weapon_name, weapon_damage, ...)  # Create new weapon
#             choices[choice_text] = lambda: Player.equip_melee_weapon(weapon)
#         elif "find ammo" in choice_text.lower():
#             ammo_amount = ...  # Extract ammo amount from choice text
#             choices[choice_text] = increase_ammo(ammo_amount)
#     return choices

# def actions_generator(description):
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are a scene creator for a Fantasy text-based RPG. Your job is to create scenes for a user to interact with.",
#             },
#             {
#                 "role": "user",
#                 "content": f'based on the scene described in {description}, generate possible actions for the scene for the user.'
#             },
#         ],
#     )
#     scene = response.choices[0].message.content
#     return scene

# def exits_generator(description):
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are a scene creator for a Fantasy text-based RPG. Your job is to create scenes for a user to interact with.",
#             },
#             {
#                 "role": "user",
#                 "content": f'based on the scene described in {description}, generate possible exits for the scene.'
#             },
#         ],
#     )
#     scene = response.choices[0].message.content
#     return scene

# def description_generator(previous_scene):
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are a scene creator for a Fantasy text-based RPG. Your job is to create scenes for a user to interact with.",
#             },
#             {
#                 "role": "user",
#                 "content": f'Create an adventure fantasy scene for the user to interact with. Write out the description for the scene. Take into account the previous scene: {previous_scene}'
#             },
#         ],
#     )
#     scene = response.choices[0].message.content
#     return scene

# def scene_generator2(previous_scene=None):
#     user_input = input("What option do you select? ")
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are a dungeon master for a Fantasy tabletop RPG. Your job is to create adventure scenarios for the user based on their input and track their weapons, health and damage. The scenarios can include health potions, swords, bows and arrows and monsters. Provide 3 or 4 discrete options for continuation for the player. Generate a new scene, every time the player responds.",
#             },
#             {"role": "user", "content": user_input},
#         ],
#     )
#     scene = response.choices[0].message.content
#     # if "potion" in scene.lower():
#     #     #interact with potion option
#     #     scene_generator(scene)
#     # elif "sword" in scene.lower():
#     #     #interact with sword option
#     #     scene_generator(scene)
#     # elif "bow" or "arrow" in scene.lower():
#     #     #interact with bow and arrow option
#     #     scene_generator(scene)
#     # elif "monster" in scene.lower():
#     #     #interact with monster option
#     #     scene_generator(scene)
#     return scene
