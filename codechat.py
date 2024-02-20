from mlxfiles.utils import load, generate
import os

current_directory = os.getcwd()
current_directory+='/models'
directories = [folder for folder in os.listdir(current_directory)
               if os.path.isdir(os.path.join(current_directory, folder))]
chat2 = [
    "<s> [INST] You are a highly intelligent assistant that gives long thought out answers. [/INST] Ok, I am a highly intelligent assistant. I will make sure that I give long thought out answers to whatever questions you ask.</s> ",
    ]
chat1 = [
    {"role": "system", "content": "You are a helpful and honest code assistant. Please, provide all answers to programming questions in the coding language referenced by user"},
    ]

def pick_model():
    print('Choose your model: ')
    while True:
        for directory in directories:
            user_input = input(f"Type 'yes' to select or 'no' for the next model: {directory}\n")
            if user_input.lower() == 'yes':
                return directory
            
def pick_instruct(name):
    if 'mixtral' in name:
        return 2
    elif 'mistral' in name:
        return 2
    else:
        return 1

if __name__ == "__main__":
    load_model = pick_model()
    print(f'Loading {load_model}...')
    num = pick_instruct(load_model.lower())
    load_model = 'models/'+load_model
    model, tokenizer = load(load_model)
    temp = 0.0
    max_toks = 500
    print('----\nTemperature set to 0.0, max token output set to 500\n----')

    #inputs = tokenizer.apply_chat_template(chat, tokenize=False)
    while True:
        user_input = input("**************\n**NEW PROMPT**\n************\nEnter a prompt or type `menu' for more options:\n")

        if user_input.lower() == 'menu':
            user_input = input("----MENU----\n'exit' to exit,\n'change' to change models,\n'temp' to change temp,\n'toks' to change max toks,\n'clear' to clear context:\n")
            if user_input.lower() == 'exit':
                break
            elif user_input.lower() == 'change':
                load_model = pick_model()
                load_model = 'models/'+load_model+'/'
                #model, tokenizer = load(load_model)
                num=2
            elif user_input.lower() == 'temp':
                temp = input("Enter a temperature float (n.n): ")
            elif user_input.lower() == 'toks':
                max_toks = int(input("Enter the maximum tokens for output: "))
            elif user_input.lower() == 'clear':
                    chat2 = [
                        "<s> [INST] You are a highly intelligent assistant that give long thought out answers. [/INST] Ok, I am a highly intelligent assistant. I will make sure that I give long thought out answers to whatever questions you ask.</s> ",
                        ]
        else:
            if num == 1:
                chat1.append({"role": "user", "content": f"{user_input}"})
            elif num == 2:
                chat2.append(f"[INST] {user_input} [/INST]")
            if num == 1:
                inputs = tokenizer.apply_chat_template(chat1, tokenize=False)
            elif num == 2:
                inputs=''
                for x in chat2:
                    inputs += x
            response = generate(model, tokenizer, prompt=inputs, verbose=False, max_tokens=max_toks)
            print('\n')
            print(response)
            print('\n')
            if num == 1:
                if len(chat1)>2:
                    del chat1[1]
                    del chat1[2]
                    chat1.append({"role": "assistant", "content": f"{response}"})
                else:
                    chat1.append({"role": "assistant", "content": f"{response}"})
            elif num == 2:
                inputs=''
                if len(chat2)>2:
                    del chat2[1]
                    del chat2[2]
                    chat2.append(response)
                else:
                    chat2.append(response)