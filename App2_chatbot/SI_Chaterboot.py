from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot  import comparisons, response_selection

chatbot = ChatBot(
        'Experto en viajes',
        storage_adapter = 'chatterbot.storage.MongoDatabaseAdapter',
        database_uri = 'mongodb://localhost:27017/sichatbot',
        input_adapter = 'chatterbot.input.TerminalAdapter',
        ouput_adapter = 'chatterbot.ouput.OutputAdapter',
        ouput_format = 'text',
        logic_adaptaer=[
            {
                "import_path":"chatterbot.logic.BestMatch",
                "statement_comparasion_function":"chatterbot.comparisons.levenshtein_distance",
                "response_selection_method": response_selection.get_most_frequent_response,
                "default_response":"Disculpa, no te he entendido. Se mas específico?",
                "maximun_similarity_threshold" : 0.51
                
            },
            {
                "import_path" : "chatterbot.logic.SpecificResponseAdapter",
                "input_text" :"quiero Reservar un crucero",
                "output_text" :" Puedes reservarlo en https://wwww.google.com",
                
                
            }
        ],
        preprocessors=[
          'chatterbot.preprocessors.clean_whitespace'  
        ],
    read_only = True
    )

DEFAUTL_SESSION_ID = '18.06.2014'

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("./cruceros.yml")
while True:
    try:
        user_input = Statement(input())
        bot_response = chatbot.get_response(user_input)
        print(bot_response)
    except (KeyboardInterrupt,EOFError,SystemError):
        break

