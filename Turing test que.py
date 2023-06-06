input_text = input("Hello")
def turing_test(input_text):
    if "Hi" in input_text or "Hello" in input_text:
        return print("Can you tell me a joke?")
    elif "a question?" in input_text or "Doubt" in input_text:
        return print("Can you explain the theory of relativity to me?")
    elif "Are you Free" in input_text:
            return print("Can you play a game of chess with me?")
    elif "What's your name?" in input_text:
        return print("I'm Naga")
    elif "Any personal experience" in input_text:
        return print("Can you tell me a story about a personal experience you've had?")
    elif "Aim in life" in input_text:
        return print("To become a data analyst")
    elif "A technical question" in input_text:
        return print("Can you explain how a computer program works?")
    elif "What is your favorite color?" in input_text:
        return print("Light green")
    elif "Any thing intresting question?" in input_text:
        return print("Can you give me your opinion on a controversial topic?")
    elif "Are you fluent in english then " in input_text:
        return print("Can you give me a definition of a word from the dictionary?")
    elif "I want a help" in input_text:
        return print("Can you give me a current news update on a topic of my choice?")
    elif "What is your favorite food?" in input_text:
        return print("Ladies finger")
    elif "What is your favorite hobby?" in input_text:
        return print("Playing games")
    else:
        return print("I am sorry, I don't understand what you are asking.")
    

x = turing_test("Hello")
x = turing_test("Are you a robot?")