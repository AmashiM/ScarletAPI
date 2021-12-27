
# ScarletAPI

This is a wrapper for the ScarletAPI

<br />

# Installation

```
pip install git+https://github.com/AmashiSenpai/ScarletAPI.git
```
<sub>_I know easy right?_</sub>

<hr />
<br />

# Docs
these are the docs

## Initialize Scarlet
```py
scarlet = Scarlet()
```

now we need a user to pass in to start working with the api
<br />
this should be a one time thing

```py
user: 'ScarletUser' = await Scarlet.create(username, password, email)
```
Example:
```py
user = await Scarlet.create(
    username="Amashi",
    password="*******",
    email="example@gmail.com"
)
user.export_to_file(outfile=".user.json")

scarlet.set_user(user)
```
We export this data naturally to a json so that we can get the data later on
<br />

If we were to then want to later initialize the scarlet instance with the user object in place we can do so.
```py

```

<hr />

## AI Shit

```py
ai_token=os.environ["AI_TOKEN"]

scarlet.set_user(ScarletUser.from_file(".user.json"))

print(scarlet.current_user)

res = await scarlet.sentience("Hello Bitch", ai_token=ai_token)
print(res.message)
```


# Other Info

this shit uses typings for everything and all the responses are typed out
