import questionary
from questionary import Style


style = Style([
    ('qmark', 'fg:#673ab7 bold'),       # token in front of the question
    ('question', 'bold'),               # question text
    # submitted answer text behind the question
    ('answer', 'fg:#f44336 bold'),
    # pointer used in select and checkbox prompts
    ('pointer', 'fg:#673ab7 bold'),
    # pointed-at choice in select and checkbox prompts
    ('highlighted', 'fg:#673ab7 bold'),
    # style for a selected item of a checkbox
    ('selected', 'fg:#cc5454 bg:black'),
    ('separator', 'fg:#cc5454'),        # separator in lists
    # user instructions for select, rawselect, checkbox
    ('instruction', ''),
    ('text', ''),                       # plain text
    # disabled choices for select and checkbox prompts
    ('disabled', 'fg:#858585 italic')
])

# style = Style({
#     ('Separator', '#cc5454'),
#     ('QuestionMark', '#673ab7 bold'),
#     ('Selected ', '#cc5454'),  # default
#     ('Pointer', '#673ab7 bold'),
#     ('Instruction', ''),  # default
#     ('Answer', '#f44336 bold'),
#     ('Question ', ''),
# })

# answers = questionary.form(
#     first = questionary.confirm("Would you like the next question?", default=True),
#     second = questionary.select("Select item", choices=["item1", "item2", "item3"])
# ).ask()

# print(answers)

# box.x01 = questionary.path('Select file path?', style=style).ask()
# box.x02 = questionary.confirm("Are you amazed?", style=style).ask()
# box.x03 = questionary.password("What's your secret?", style=style).ask()
# box.x04 = questionary.path(
#     "What's the path to the projects version file?", style=style).ask()
# box.x05 = questionary.confirm("Are you amazed?", style=style).ask()
# box.x06 = questionary.select(
#     "What do you want to do?",
#     choices=[
#         "Order a pizza",
#         "Make a reservation",
#         "Ask for opening hours"
#     ], style=style).ask()
# box.x07 = questionary.checkbox(
#     'Select toppings',
#     choices=[
#         "Cheese",
#         "Tomato",
#         "Pineapple",
#     ], style=style).ask()

# box.x08 = questionary.autocomplete(
#     'Choose ant specie',
#     choices=[
#         'Camponotus pennsylvanicus',
#         'Linepithema humile',
#         'Eciton burchellii',
#         "Atta colombica",
#         'Polyergus lucidus',
#         'Polyergus rufescens',
#     ], style=style).ask()


def question_dict(
    x, y, **kwargs): return {y: questionary.__dict__[x](y, **kwargs, style=style).ask()}


def question(
    x, y, **kwargs): return questionary.__dict__[x](y, **kwargs, qmark='?', style=style).ask()


# answer = select('autocomplete', 'Choose something',
#                 choices=['1111', '22222', '32222'])
