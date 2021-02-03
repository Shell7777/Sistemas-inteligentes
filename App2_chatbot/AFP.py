from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import comparisons, response_selection
from chatterbot.trainers import ListTrainer

chatbot = ChatBot(
    "PeruvianBotUPNMasNaa",

    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    database_uri='mongodb://localhost:27017/chatparcial2b',
    
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

trainer = ListTrainer(chatbot)
trainer.train([
    'Hola',
    'Hola, que deseas sabes ?',
    
    'subcidios del peru',
    'Ok,¿Sobre cual subsidio quieres saber?',
    
    'Bono para hogares en condición de pobreza o pobreza extrema',
    'el bono de S/ 380 para hogares en condición de pobreza o pobreza extrema, que se encuentran en los ámbitos geográficos con mayor riesgo sanitario durante el estado de emergencia por el coronavirus (COVID-19).',
    
    'Bono independiente',
    'El apoyo económico de 760 soles que se brinda a los trabajadores independientes cuyos hogares están calificados como No pobres por el Sistema de Focalización de Hogares (SISFOH).',
    
    'Bono rural',
    'No Problem! Have a Good Day!',
    
    'Subsidios para empresas generadoras de empleo',
    'si eres empleador del sector privado, se te entregará un bono salarial del 35% por cada trabajador con rentas de quinta categoría que gane hasta S/ 1,500. Si cumples los requisitos, regístrate hasta el 13 de abril.',
    
    'Bono Familiar Universal',
    ' este bono de S/ 760 es un subsidio que se asigna al hogar a través de un perceptor. El perceptor es un integrante del hogar beneficiado, a quien se identifica y se asigna una modalidad para la entrega del bono',
    
    'Líneas de apoyo económico',
    'el Ministerio de Cultura pone a disposición de los ciudadanos líneas de apoyo dirigidas a trabajadores y organizaciones culturales, así como a portadores del patrimonio inmaterial.'
    ])

while True:
    try:
        user_input = Statement(input())
        if (user_input.text) =="calculaAFP":
            print ('BOT: Ingrese su cantidad abonada')
            saldo = int(input())        
            print ('Bot:Su monto de retiro es ' ,(saldo*0.10))
            break
        
        else :   
            bot_response = chatbot.get_response(user_input)
            print('Bot:',bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break