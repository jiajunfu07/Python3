from sys import argv

script, user_name = argv
prompt_user = '> '

print(f"I am {script}, hello {user_name}, how are you")
status = input(prompt_user)
print(f"""
{user_name} saied that,
he is {status}.
""")

