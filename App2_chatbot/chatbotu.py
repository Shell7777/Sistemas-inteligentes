from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import comparisons, response_selection

chatbot = ChatBot(
    "Experto_cruceros",

    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    database_uri='mongodb://localhost:27017/chatupn',
    
    input_adapter="chatterbot.input.TerminalAdapter",
    
    output_adapter="chatterbot.output.OutputAdapter",
    output_format="text",

    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method": response_selection.get_most_frequent_response,
			'default_response': 'Disculpa, no te he entendido bien, sólo soy experto en viajes. ¿Puedes ser más específico?.',
            'maximum_similarity_threshold': 0.51			
        },
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'Quiero reservar un crucero',
            'output_text': 'Puedes reservarlo ahora en: https://www.logitravel.com/cruceros/'
        },
    ],
    
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],
    
    read_only=True,
)
DEFAULT_SESSION_ID = '18.06.2014'

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("./cruceros.yml")

while True:
    try:
        user_input = Statement(input())

        bot_response = chatbot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break